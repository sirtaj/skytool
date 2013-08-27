

from skygui import Subsystem

import PyQt4.QtGui as qg
import PyQt4.QtCore as qc

from util.qutil import qmicro, widget_update, MyThread


class PluginBrowser(Subsystem):
    def start(self):
        #self.plugin_collection.parse_install()

        # setup connections
        tree = self.ui.modTreeBrowser
        tree.connect
        #tree.set

        self.populate_mod_tree()

    def stop(self):
        self.plugin_collection = None

    def populate_mod_tree(self):
        with self.status("Loading ESM/ESP tree..."):
            tree = self.ui.modTreeBrowser

            with widget_update(tree):
                self.model = PluginItemModel(tree)
                self.model.set_plugins(self.game.get_plugins())
                tree.setModel(self.model)

                for col_idx in range(len(COLUMNS)):
                    tree.resizeColumnToContents(col_idx)

                tree.adjustSize()


    def selected(self, selected_items):
        pass # TODO


class PluginItemModel(qg.QStandardItemModel):
    def set_plugins(self, plugins):
        self.plugins = plugins

        self.itemChanged.connect(self.updatePluginFromItem)
        self.setSortRole(qc.Qt.UserRole)

        self.setRowCount(len(plugins.by_order))
        self.setColumnCount(len(COLUMNS))

        self.setHorizontalHeaderLabels([c.HEADING for c in COLUMNS])


        try:
            self.filling = True
            for index, load_order, plugin in plugins.iterate_order():
                plugin.index = index
                plugin.load_order = load_order

                for column, factory in enumerate(COLUMNS):
                    item = factory.create_item(index, load_order, plugin)
                    item.plugin = plugin
                    self.setItem(index, column, item)
        finally:
            self.filling = False

    def updatePluginFromItem(self, item):
        if self.filling: return
        COLUMNS[item.column()].update_value(item, item.plugin)


#############################


class Column:
    def create_item(self, index, load_order, plugin):
        pass

    def update_value(self, item, plugin):
        pass

    def reset_value(self, item, plugin):
        pass


class Filename(Column):
    HEADING = 'Filename'

    def create_item(self, index, load_order, plugin):
        item = qg.QStandardItem()
        item.setCheckable(True)
        self.reset_value(item, plugin)
        return item

    def update_value(self, item, plugin):
        print "Update", plugin
        new_filename = unicode(item.data())
        if new_filename == plugin.name:
            return

        try:
            plugin.set_name(new_filename)
        except Exception, exc:
            print "UPDATE FAIL:", repr(exc)
            self.reset_value(item, plugin)
        finally:
            item.setData(plugin.name, qc.Qt.UserRole)

    def reset_value(self, item, plugin):
        item.setData(plugin.name, qc.Qt.UserRole)
        item.setData(plugin.name, qc.Qt.UserRole)
        item.setCheckState(qc.Qt.Checked if plugin.active else qc.Qt.Unchecked)


class LoadOrder(Column):
    HEADING = "Order"

    def create_item(self, index, load_order, plugin):
        item = qg.QStandardItem()
        item.setData(index, qc.Qt.UserRole)

        return item

    def reset_value(self, item, plugin):
        item.setData((u'%02X' % load_order) if plugin.active else '')


class ModTime(Column):
    HEADING = "Modified"
    TIME_FORMAT     = "%Y-%m-%d %H:%M:%S"

    def create_item(self, index, load_order, plugin):
        ts = plugin.modified_date()
        item = qg.QStandardItem(ts.strftime(self.TIME_FORMAT))
        item.setData(ts.toordinal(), qc.Qt.UserRole)

        return item

COLUMNS = [Filename(), LoadOrder(), ModTime()]
