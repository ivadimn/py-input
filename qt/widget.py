from PyQt6.QtWidgets import QWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QListView
from PyQt6.QtCore import pyqtSlot
from data_model import DataModel


class Widget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__model = DataModel(self)
        self.__lv = QListView(self)
        self.__lv.setModel(self.__model)

        self.__edt = QLineEdit("New value", self)
        self.__btn_add = QPushButton("Add value", self)
        self.__btn_del = QPushButton("Delete value", self)

        self.__btn_add.clicked.connect(self.add_value)

        vbox = QVBoxLayout(self)
        vbox.addWidget(self.__lv)

        hbox = QHBoxLayout()
        hbox.addWidget(self.__edt)
        hbox.addWidget(self.__btn_add)
        hbox.addWidget(self.__btn_del)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

    @pyqtSlot()
    def add_value(self):
        value = self.__edt.text().strip()
        if len(value) > 0:
            self.__model.add_value(value)