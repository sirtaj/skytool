
import PyQt4.QtCore as qc
import PyQt4.QtGui as qg
import PyQt4.uic as uic

import sys, os.path

from qutil import qmicro

def find_run_base():
    for pth in reversed(sys.path):
        if os.path.exists(os.path.join(pth, 'gui', 'skytool.ui')):
            return pth
    
    raise Exception, "Application run base directory not found."



class DirectoryFilterModel(qg.QSortFilterProxyModel):
    def __init__(self, parent = None):
        super(qg.QSortFilterProxyModel, self).__init__(parent)

    def filterAcceptsRow(self, source_row, source_parent):
        sm = self.sourceModel()
        if not sm.filterAcceptsRow(source_row, source_parent):
            return False
        return sm.hasChildren(sm.index(source_row, 0, source_parent))


class ModFilterModel(qg.QSortFilterProxyModel):
    def __init__(self, game, mod_log, enabled = True, parent = None):
        super(qg.QSortFilterProxyModel, self).__init__(parent)
        self.game = game
        self.mod_log = mod_log
        self.enabled = enabled
        self.base = game.install_path.replace('\\', '/').lower()
        self.base_len = len(self.base)

    def setFilterEnabled(self, enable = True):
        old_val = self.enabled
        self.enabled = enable

        if old_val != enable:
            self.invalidateFilter()

    def filterAcceptsRow(self, source_row, source_parent):
        if not self.enabled:
            return True

        sm = self.sourceModel()

        sub_idx = sm.index(source_row, 0, source_parent)
        filename = str(sm.filePath( sub_idx )).lower()
        if (len(filename) <= self.base_len):
            return True

        if sm.isDir(sub_idx):
            return True

        return filename[self.base_len:] not in self.mod_log.data_files


class GameDataFolderModel(qg.QFileSystemModel):
    pass


class App(qc.QObject):
    def __init__(self):
        super(qc.QObject, self).__init__()

        self.game = None
        self.nexus = None
        
        self.app = None
        self.ui = None


    def run(self):
        from game import Skyrim
        from nexus import Nexus

        self.game = Skyrim()
        self.mods = Nexus(self.game)

        self.mods.parse_install()

        self.run_base = find_run_base()
        self.app, self.ui = self.create_gui(self.run_base)

        self.ui.mainTabs.setCurrentIndex(0)

        self.populate_file_tree()
        self.app.exec_()

    def create_gui(self, run_dir):
        app = qg.QApplication(sys.argv)
        ui = uic.loadUi(os.path.join(run_dir, 'gui', 'skytool.ui'))
        ui.show()

        return app, ui

    def populate_file_tree(self):
        print "start"
        tree = self.ui.dataFileBrowser

        mod = self.df_model = qg.QFileSystemModel(tree)
        root_idx = self.df_model.setRootPath( self.game.install_path )

        mod = self.mf_model = ModFilterModel(self.game, self.mods.mod_log,
                enabled = True, parent = tree)
        mod.setSourceModel( self.df_model )
        root_idx = mod.mapFromSource( root_idx )

        #mod = self.dir_filter = DirectoryFilterModel(tree)
        #mod.setSourceModel( self.mf_model )
        #root_idx = mod.mapFromSource( root_idx )

        tree.setModel(mod)
        tree.setRootIndex(root_idx)
        #tree.adjustHeaderWidth()

    def populate_mod_tree(self):
        tree = self.ui.modTreeBrowser()


if __name__ == '__main__':
    app = App()
    app.run()
