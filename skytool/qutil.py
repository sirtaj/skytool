
import PyQt4.QtCore as qc
import PyQt4.QtGui as qg
from PyQt4.QtCore import SIGNAL

from contextlib import contextmanager

@contextmanager
def widget_update(widget):
    widget.setUpdatesEnabled(False)
    yield
    widget.setUpdatesEnabled(True)


def qmicro(iterations=500):
     '''Qt fire-and-forget microprocess decorator.
     '''
     def wrap_qmicro(microfn):
         def call_qmicro(qobj, *call_args, **call_kwargs):
             try:
                 call_iter = microfn(qobj, *call_args, **call_kwargs)
             except StopIteration, endex:
                 return
             except:
                 raise

             return QtMicroProcess(qobj, call_iter.next, iterations)
         return call_qmicro
     return wrap_qmicro


class QtMicroProcess(qc.QObject):
     '''A single running microprocess, scheduled in the event loop using
     timer events until completed or error.
     '''
     def __init__(self, parent, next_fn, iterations):
         qc.QObject.__init__(self, parent)
         self.next_fn = next_fn
         self.iterations = iterations
         self.timer_id = self.startTimer(0)

     def timerEvent(self, tev):
         next_fn = self.next_fn
         try:
             for itidx in xrange(self.iterations):
                 next_fn()
             return
         except StopIteration, sex:
             pass
         except Exception, ex:
             print "QMICRO: Unhandled exception:", ex

         try:
             self.killTimer(self.timer_id)
         finally:
             self.deleteLater()


def print_time(fn):
    '''Convenience decorator to print execution time
    '''
    from time import clock
    def run_it(*args, **kwargs):
        start = clock()
        ret = fn(*args, **kwargs)
        print fn, "took", clock() - start, "seconds"
        return ret

    return run_it



class MyThread(qc.QThread):
    '''Basic fire and forget thread that calls thread_fn and calls on_finish when done.

        thread_fn takes no arguments and returns whatever.
        on_finish takes one argument, which is the returned value of thread_fn
        on_error takes one argument, which is the raised exception.
    '''

    def __init__(self, thread_fn, on_finish = None, on_error = None, parent = None):
        super(MyThread, self).__init__(parent)
        self.thread_fn = thread_fn
        self.on_finish = self.null_finish if on_finish is None else on_finish
        self.on_error = self.display_error if on_error is None else on_error

        self.exception = None
        self.return_value = None
        self.one_shot = False

        self.finished.connect( self.handle_finished )
        self.terminated.connect( self.handle_finished )

    def null_finish(self, *args, **kwargs): pass

    def handle_finished(self):
        try:
            if self.exception is not None:
                self.on_error(self.exception)
            else:
                self.on_finish(self.return_value)
        except BaseException, e:
            self.display_error(e)
        finally:
            self.exception = None
            self.return_value = None
            if self.one_shot:
                self.deleteLater()

    def run(self):
        try:
            self.return_value = self.thread_fn()
        except BaseException, e:
            self.exception = e
        finally:
            return

    def display_error(self, exc):
        qg.QMessageBox.critical(
                self.parent(),
                "Unhandled Error: %s" % (exc.__class__.__name__),
                str(exc) )

    @classmethod
    def one_shot(Cls, thread_fn, on_finish = None, on_error = None, parent = None):
        thread = Cls(thread_fn, on_finish, on_error, parent)
        thread.one_shot = True
        thread.start()
        return thread

    @classmethod
    def process(Cls, process_fn):
        '''A decorator to mark a fire and forget threaded process.
        '''
        def wrapped_process(*args, **kwargs):
            def run_process():
                process_fn(*args, **kwargs)

            Cls.one_shot(thread_fn = run_process, on_finish = None, on_error = None, parent = None)

        return wrapped_process

def test_thread():
    import sys
    def process():
        for a in xrange(20): print a
        print "done"
        return 42

    def on_done(v):
        print "returned with:", v

    app = qg.QApplication(sys.argv[1:])
    MyThread.one_shot(process, on_finish = on_done)
    app.exec_()
    import time
    time.sleep(5)

if __name__ == '__main__':
    test_thread()
