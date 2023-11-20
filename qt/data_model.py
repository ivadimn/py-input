import typing
from PyQt6.QtCore import QAbstractItemModel, QModelIndex, Qt, pyqtSlot


class DataModel(QAbstractItemModel):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__data = list()

    def columnCount(self, parent: QModelIndex = ...) -> int:
        return 1

    def rowCount(self, parent: QModelIndex = ...) -> int:
        return len(self.__data)

    def data(self, index: QModelIndex, role: int = ...) -> typing.Any:
        if role == Qt.ItemDataRole.DisplayRole:
            return self.__data[index.row()]

    def index(self, row: int, column: int, parent: QModelIndex = ...) -> QModelIndex:
        return self.createIndex(row, column, self.__data[row])

    def parent(self, child: QModelIndex) -> QModelIndex:
        return QModelIndex()

    @pyqtSlot()
    def add_value(self, value: str):
        #self.beginResetModel()
        self.__data.append(value)
        #self.endResetModel()
        self.layoutChanged.emit()


