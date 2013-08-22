

from skygui import Subsystem

import PyQt4.QtGui as qg
import PyQt4.QtCore as qc

from util.qutil import qmicro, widget_update, MyThread


class ModBrowser(Subsystem):
    def start(self):
        #self.plugin_collection.parse_install()
        self.populate_mod_tree()

    def stop(self):
        self.plugin_collection = None

    def populate_mod_tree(self):
        with self.status("Loading ESM/ESP tree..."):
            tree = self.ui.modTreeBrowser

            with widget_update(tree):
                self.model = ModItemModel(tree)
                self.model.set_plugins(self.game.get_plugins())
                tree.setModel(self.model)


class ModItemModel(qg.QStandardItemModel):
    def set_plugins(self, plugins):
        self.plugins = plugins

        next_index = iter(range(len(plugins.by_order))).next

        self.setRowCount(len(plugins.by_order))
        self.setColumnCount(4)
        self.setHorizontalHeaderLabels(['Active', 'Index', 'Filename', 'Modified'])
        self.setSortRole(qc.Qt.UserRole)


        for order, plugin in enumerate(plugins.by_order):
            order_item = qg.QStandardItem((u'%02X' % next_index()) if plugin.active else '')
            order_item.setData(order, qc.Qt.UserRole)

            active_item = qg.QStandardItem()
            active_item.setCheckable(True)
            active_item.setCheckState(qc.Qt.Checked if plugin.active else qc.Qt.Unchecked)
            active_item.setData(1 if plugin.active else 0, qc.Qt.UserRole)

            ts = plugin.modified_date()
            mod_item = qg.QStandardItem(unicode(ts))
            mod_item.setData(ts.toordinal(), qc.Qt.UserRole)

            name_item = qg.QStandardItem(plugin.name)
            name_item.setData(plugin.name, qc.Qt.UserRole)

            for col, item in enumerate([active_item, order_item, name_item, mod_item]):
                self.setItem(order, col, item)
