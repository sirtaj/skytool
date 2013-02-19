
import PyQt4.QtCore as qc
import PyQt4.QtGui as qg
import PyQt4.uic as uic

import sys, os.path

from qutil import qmicro, widget_update, MyThread
from contextlib import contextmanager

def find_resource_base():
    for pth in reversed(sys.path):
        if os.path.exists(os.path.join(pth, "..", 'gui', 'skytool.ui')):
            return os.path.split(pth)[0]
    
    raise Exception, "Application run base directory not found."


class App(qc.QObject):
    def __init__(self, parent = None):
        super(qc.QObject, self).__init__(parent)

        self.game = None
        self.nexus = None
        
        self.ui = None
        self.resource_base = find_resource_base()
        qg.qApp.aboutToQuit.connect(self.shutdown)
        qg.qApp.lastWindowClosed.connect(qg.qApp.quit)

    def resource_file(self, relative_path):
        path = [self.resource_base] + relative_path.split('/')
        return os.path.join(*path)

    def run(self):
        from game import Skyrim
        from nexus import Nexus

        self.game = Skyrim()
        self.mod_collection = Nexus(self.game)

        self.create_gui()
        self.mod_collection.parse_install()
        #self.populate_file_tree()

        MyThread.one_shot(  self.mod_collection.parse_install,
                            on_finish = lambda v: self.populate_file_tree(),
                            parent = self.ui)
        qg.qApp.exec_()

    def shutdown(self):
        #self.ui = None
        #self.nexus = None
        #self.game = None
        pass

    @contextmanager
    def status(self, message):
        self.ui.statusBar().showMessage(message)
        yield
        self.ui.statusBar().clearMessage()

    def create_gui(self):
        self.ui = uic.loadUi(self.resource_file('gui/skytool.ui'))
        self.ui.mainTabs.setCurrentIndex(0)
        self.ui.show()

    #@qmicro(iterations=1)
    def populate_file_tree(self):
        with self.status("Loading data tree..."):
            tree = self.ui.dataFileBrowser

            tree_model = qg.QFileSystemModel(tree)
            tree_model.directoryLoaded.connect(
                lambda d: self.ui.statusBar().showMessage("Loaded %s" % unicode(d), 500))

            root_idx = tree_model.setRootPath( self.game.install_path )

            tree_model = ModFilterModel(self.game,
                                        self.mod_collection.mod_log, 
                                        tree_model,
                                        parent = tree)
            root_idx = tree_model.mapFromSource( root_idx )

            with widget_update(tree):
                tree.setModel(tree_model)
                tree.setRootIndex(root_idx)

    def populate_mod_tree(self):
        tree = self.ui.modTreeBrowser()
        # TODO


class DumbFileModel:
    def __init__(self, game):
        self.game = game
        self.root_path = game.install_path
        self.dirs = {}
        self.files = {}

    def populate_item(self, parent):
        model = qg.QStandardItemModel(parent)
        root_item.path = self.root_path

        for root, dirs, files in os.walk(self.root_path):
            for sub_dir in dirs:
                path = '/'.join(root, sub_dir)


class ModFilterModel(qg.QSortFilterProxyModel):
    '''Filters the source model (assumes it is a QFileSystemModel), removing
    files and directories that are registered as belonging to the mod source.
    '''
    def __init__(self, game, mod_source, fs_source, enabled = True, parent = None):
        super(qg.QSortFilterProxyModel, self).__init__(parent)
        self.game = game
        self.mod_source = mod_source
        self.enabled = False
        self.base = game.install_path.replace('\\', '/').lower()

        def fast_filter(source_row, source_parent,

                            # shortcuts to fs model
                            _index = fs_source.index,
                            _filePath = fs_source.filePath,
                            _isDir = fs_source.isDir,
                            _rowCount = fs_source.rowCount,
                            _fetchMore = fs_source.fetchMore,
                            _hasChildren = fs_source.hasChildren,

                            # shortcuts to mod source
                            _has_dir = self.mod_source.has_dir,
                            _has_file = self.mod_source.has_file,

                            _base_len = len(self.base)):

            sub_idx = _index(source_row, 0, source_parent)
            filename = unicode(_filePath( sub_idx )).lower()

            if (len(filename) <= _base_len):
                return True
            filename = filename[_base_len:]

            if _isDir(sub_idx):
                if not _has_dir(filename):
                    return True
            elif not _has_file(filename):
                return True

            # its a directory that we've modded, but it may have non-mod children.
            row_count = _rowCount(sub_idx)
            if row_count == 0:
                _fetchMore(sub_idx)
                if not _hasChildren(sub_idx):
                    return False
                else:
                    row_count = _rowCount(sub_idx)

            # there are files here, search children.
            for row in xrange(row_count):
                if fast_filter(row, sub_idx):
                    return True

            return False

        self.fast_filter = fast_filter
        self.filterAcceptsRow = self.null_filter
        self.setFilterEnabled(enabled)
        self.setSourceModel(fs_source)

    def null_filter(self, source_row, source_parent): return True

    def setFilterEnabled(self, enable = True):
        if enable == self.enabled: return

        self.enabled = enable
        self.filterAcceptsRow = self.fast_filter if enable else self.null_filter
        self.invalidateFilter()

if __name__ == '__main__':
    if not isinstance(qg.qApp, qg.QApplication):
        qg.qApp = qg.QApplication(sys.argv)
    app = App(qg.qApp)
    app.run()
    app.deleteLater()
    app = None
    print "exit"
