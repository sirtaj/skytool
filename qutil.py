from PyQt4.QtCore import QObject, SIGNAL

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


class QtMicroProcess(QObject):
     '''A single running microprocess, scheduled in the event loop using
     timer events until completed or error.
     '''
     def __init__(self, parent, next_fn, iterations):
         QObject.__init__(self, parent)
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


