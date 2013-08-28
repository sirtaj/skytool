#!/usr/bin/env python

__doc__=\
'''Tree Browse/Query for Skyrim data directory.
'''

from skygui import Subsystem

import PyQt4.QtCore as qc
import PyQt4.QtGui as qg

from util.qutil import qmicro, widget_update, MyThread


class DataBrowser(Subsystem):
    '''Instantiates the GUI and implements user actions.
    '''
    def __init__(self, parent):
        super(Subsystem, self).__init__(parent)
        self.mods = None

    def start(self):
        from files import UnionCollection
        self.mods = UnionCollection(self.game)

        MyThread.one_shot(  self.load_collection,
                            on_finish = lambda v: self.populate_file_tree(),
                            parent = self.ui)

    def stop(self):
        self.mods = None

    #################

    def load_collection(self):
        from nexus import NexusMods
        self.mods.add_collection(NexusMods(self.game))
        self.mods.parse_install()

    #@qmicro(iterations=1)
    def populate_file_tree(self):
        with self.status("Loading data tree..."):
            tree = self.ui.dataFileBrowser
            tree_model = qg.QFileSystemModel( tree )

            def show_load_message(d, show_msg = self.ui.statusBar().showMessage):
                show_msg("Loaded %s" % unicode(d), 500)

            tree_model.directoryLoaded.connect( show_load_message )

            root_idx = tree_model.setRootPath( self.game.install_path )

            tree_model = ModFilterModel(self.game,
                                        self.mods,
                                        tree_model,
                                        parent = tree)
            root_idx = tree_model.mapFromSource( root_idx )

            with widget_update(tree):
                tree.setModel(tree_model)
                tree.setRootIndex(root_idx)


class DumbFileModel:
    def __init__(self, game):
        self.game = game
        self.dirs = {}
        self.files = {}

    def populate_item(self, parent):
        model = qg.QStandardItemModel(parent)
        root_item.path = self.game.install_path

        for root, dirs, files in os.walk(self.game.install_path):
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

        # attach methods
        self.fast_filter = fast_filter
        self.filterAcceptsRow = self.null_filter
        self.setFilterEnabled(enabled)
        self.setSourceModel(fs_source)

    def null_filter(self, source_row, source_parent):
        return True

    def setFilterEnabled(self, enable = True):
        if enable == self.enabled: return

        self.enabled = enable
        self.filterAcceptsRow = self.fast_filter if enable else self.null_filter
        self.invalidateFilter()
