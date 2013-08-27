#!/usr/bin/env python

__doc__=\
'''SkyScraper main GUI app.
'''

import PyQt4.QtCore as qc
import PyQt4.QtGui as qg
import PyQt4.uic as uic

import sys, os.path
from contextlib import contextmanager

class App(qc.QObject):
    '''Instantiates the GUI and implements user actions.
    '''
    def __init__(self, parent = None):
        super(App, self).__init__(parent)

        self.started = False
        self.game = None
        self.ui = None

        self.plugins = []

        self.resource_base = self.find_resource_base()
        qg.qApp.aboutToQuit.connect(self.shutdown)
        qg.qApp.lastWindowClosed.connect(qg.qApp.quit)

    ############
    # Lifecycle

    @classmethod
    def main(Cls, plugin_classes = None):
        # init
        qg.qApp = qg.QApplication(sys.argv)
        app = Cls(qg.qApp)

        if plugin_classes:
            for plugin in plugin_classes:
                app.add_plugin(plugin(app))

        #start
        app.run()

        # stop
        app.deleteLater()
        app = None
        print "exit"

    @classmethod
    def main_debug(Cls, plugin_classes = None):
        # init
        first_run = getattr(qg, 'first_run', True)

        if first_run:
            qg.qApp = qg.QApplication(sys.argv)
            qg.first_run = False

        app = Cls(qg.qApp)

        if plugin_classes:
            for plugin in plugin_classes:
                app.add_plugin(plugin(app))

        #start
        app.run()

        # stop
        print "exit"

    def add_plugin(self, plugin):
        self.plugins.append(plugin)

        if self.started:
            plugin.ui = self.ui
            plugin.game = self.game
            plugin.start()

    def run(self):
        from game import Skyrim

        self.game = Skyrim()
        self.started = True

        self.create_gui()

        for plugin in self.plugins:
            plugin.ui = self.ui
            plugin.game = self.game
            plugin.start()

        qg.qApp.exec_()

    def shutdown(self):
        self.started = False

        for plugin in reversed(self.plugins):
            plugin.stop()
            plugin.ui = None
            plugin.game = None

        self.ui = None

    ##############
    # Internal
    GUI_FILE = 'skytool.ui'

    def create_gui(self):
        self.ui = uic.loadUi(self.get_resource('gui/skytool.ui'))
        self.ui.mainTabs.setCurrentIndex(0)
        self.ui.show()

    def find_resource_base(self):
        '''A bad hack to locate the root of the resource path from
        sys.path.'''
        for pth in reversed(sys.path):
            if os.path.exists(os.path.join(pth, "..", 'gui', 'skytool.ui')):
                return os.path.split(pth)[0]

        raise Exception, "Application run base directory not found."

    ##############
    # Subsystem UI support

    def get_resource(self, relative_path):
        '''Returns full path for a relative GUI resource file.
        '''
        path = [self.resource_base] + relative_path.split('/')
        return os.path.join(*path)

    @contextmanager
    def status(self, message):
        self.ui.statusBar().showMessage(message)
        yield
        self.ui.statusBar().clearMessage()


class Subsystem(qc.QObject):
    '''A subsystem plugin. Receives ui and game variables. parent is set to application.
    '''
    def __init__(self, parent):
        super(qc.QObject, self).__init__(parent)

        self.game = None
        self.ui = None

    def start(self):    pass
    def stop(self):     pass

    def status(self, message):
        return self.parent().status(message)

    def get_resource(self, resource_name):
        return self.parent().get_resource(resource_name)


if __name__ == '__main__':
    from databrowser import DataBrowser
    from pluginbrowser import ModBrowser

    App.main([ModBrowser, DataBrowser])
