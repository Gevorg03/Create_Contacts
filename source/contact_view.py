"""This file create db and table and is co sql"""

from PyQt5 import QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QHeaderView, \
    QScrollBar, QPushButton
from database.db import all_contacts
from source.delete_contact import DeleteContact


class CreateTable(QWidget):
    """This class provide showing of table"""

    def __init__(self):
        super().__init__()
        self.setFixedSize(600, 400)
        self.setWindowTitle("View contacts")
        self.setStyleSheet("background-color: #FFFFFF")
        self.setWindowIcon(QtGui.QIcon('content/add_contact.png'))
        self.delete_contact = None

        self.create_table()

        self.create_button()

    def create_table(self):
        """This function create and fill table"""

        # Geting all contacts from db, keep in list
        contact = all_contacts()
        lst = []
        for cont in contact:
            lst.append(list(cont))

        # Create and design table
        columns = ['Name', 'Surname', 'Phone number', 'Address']
        self.table_widget = QTableWidget(self)
        self.table_widget.setRowCount(len(lst))
        self.table_widget.setColumnCount(4)
        self.table_widget.setHorizontalHeaderLabels(columns)
        self.table_widget.move(5, 5)
        self.table_widget.resize(590, 350)
        scroll_bar = QScrollBar(self)
        self.table_widget.setVerticalScrollBar(scroll_bar)
        self.table_widget.horizontalHeader().setStretchLastSection(True)
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_widget.show()

        # Filling table
        for i in range(len(lst)):
            for j in range(len(columns)):
                self.table_widget.setItem(i, j, QTableWidgetItem(lst[i][j]))

    def create_button(self):
        """This function is responsible for create and design <<Delte>> button"""

        self.btn_view_contacts = QPushButton("Delete Contact", self)
        self.btn_view_contacts.clicked.connect(self.clicked_delete)
        self.btn_view_contacts.setFixedHeight(30)
        self.btn_view_contacts.move(5, 360)
        self.btn_view_contacts.resize(590, 40)
        self.btn_view_contacts.setFont(QFont("Arial", 12))
        self.btn_view_contacts.setStyleSheet("border-radius:5; border:1px solid black; \
                                                                     background-color:#6DF680")

    def clicked_delete(self):
        """This function open DeleteContact window"""

        self.delete_contact = DeleteContact()
        self.delete_contact.show()

    def close_table(self):
        """This function close CreateTable class"""
        self.table_view.close()
        self.label_message.setText("Sucessfully deleted")
        self.label_message.setStyleSheet("color: green")
        self.label_message.move(230, 310)
        self.label_message.resize(220, 18)
