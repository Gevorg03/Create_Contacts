"""This file open main window, and let you create contacts"""

import sys
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QIntValidator, QRegExpValidator, QFont, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel, QPushButton
from source.contact_view import CreateTable
from source.contacts import Contacts
from database.db import insert_contact, all_contacts, update_contact


class MyWindow(QMainWindow):
    """This class design main window, and call main functions"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(600, 400)
        self.setWindowTitle("Contacts")
        self.setStyleSheet("background-color:#FFFFFF")
        self.setWindowIcon(QIcon('content/add_contact.png'))
        self.table_view = None

        # get all contacts and keep in list
        self.contact = all_contacts()
        self.lst = []
        for cont in self.contact:
            self.lst.append(list(cont))

        self.create_label()

        self.create_lineedit()

        self.create_button()

    def create_label(self):
        """This function is responsible for create and design labels"""

        self.label_contact_add = QLabel("Create Contacts", self)
        self.label_contact_add.setFont(QFont("Arial", 20))
        self.label_contact_add.resize(205, 22)
        self.label_contact_add.move(200, 13)

        self.label_name = QLabel("Name", self)
        self.label_name.setFont(QFont("Arial", 12))
        self.label_name.move(225, 40)

        self.label_surname = QLabel("Surname", self)
        self.label_surname.setFont(QFont("Arial", 12))
        self.label_surname.move(225, 100)

        self.label_phone_number = QLabel("Phone Number", self)
        self.label_phone_number.setFont(QFont("Arial", 12))
        self.label_phone_number.resize(105, 12)
        self.label_phone_number.move(140, 170)

        self.label_address = QLabel("Address", self)
        self.label_address.setFont(QFont("Arial", 12))
        self.label_address.move(310, 160)

        self.label_message = QLabel(self)
        self.label_message.setFont(QFont("Arial", 12))
        CreateTable.label_message = self.label_message

    def create_lineedit(self):
        """This function is responsible for create and design lineedits"""

        regex = QRegExp("[a-z-A-Z_]+")
        validator = QRegExpValidator(regex)

        self.lineedit_name = QLineEdit(self)
        font_name = self.lineedit_name.font()
        font_name.setPointSize(13)
        self.lineedit_name.setFont(font_name)
        self.lineedit_name.setValidator(validator)  # Only letters can be inputed
        self.lineedit_name.setStyleSheet("border: 1px solid green")
        self.lineedit_name.setMaxLength(15)
        self.lineedit_name.move(225, 65)
        self.lineedit_name.resize(150, 35)

        self.lineedit_surname = QLineEdit(self)
        font_surname = self.lineedit_surname.font()
        font_surname.setPointSize(13)
        self.lineedit_surname.setFont(font_surname)
        self.lineedit_surname.setValidator(validator)
        self.lineedit_surname.setStyleSheet("border: 1px solid green")
        self.lineedit_surname.setMaxLength(15)
        self.lineedit_surname.move(225, 125)
        self.lineedit_surname.resize(150, 35)

        self.lineedit_phone_number = QLineEdit("0", self)
        font_phone_number = self.lineedit_phone_number.font()
        font_phone_number.setPointSize(13)
        self.lineedit_phone_number.setFont(font_phone_number)
        self.lineedit_phone_number.setStyleSheet("border : 1px solid green")
        self.lineedit_phone_number.setMaxLength(9)
        self.lineedit_phone_number.move(140, 185)
        self.lineedit_phone_number.resize(150, 35)
        only_int = QIntValidator()
        self.lineedit_phone_number.setValidator(only_int)  # Only numbers can be inputed

        self.lineedit_address = QLineEdit(self)
        font_address = self.lineedit_address.font()
        font_address.setPointSize(13)
        self.lineedit_address.setFont(font_address)
        self.lineedit_address.setStyleSheet("border: 1px solid green")
        self.lineedit_address.setMaxLength(15)
        self.lineedit_address.move(310, 185)
        self.lineedit_address.resize(150, 35)

    def create_button(self):
        """This function is responsible for create and design <<Add>> and <<View contacts>>
        button"""

        self.btn_add = QPushButton("Add", self)
        self.btn_add.clicked.connect(self.clicked_add)
        self.btn_add.move(80, 245)
        self.btn_add.resize(120, 40)
        self.btn_add.setFont(QFont("Arial", 12))
        self.btn_add.setStyleSheet("border-radius:5; border:1px solid black; \
                                   background-color:#6DF680")

        self.btn_view_contacts = QPushButton("View Contacts", self)
        self.btn_view_contacts.clicked.connect(self.clicked_view)
        self.btn_view_contacts.move(220, 245)
        self.btn_view_contacts.resize(120, 40)
        self.btn_view_contacts.setFont(QFont("Arial", 12))
        self.btn_view_contacts.setStyleSheet("border-radius:5; border:1px solid black; \
                                             background-color:#6DF680")

        self.btn_update_contacts = QPushButton("Update Contact", self)
        self.btn_update_contacts.clicked.connect(self.clicked_update)
        self.btn_update_contacts.move(360, 245)
        self.btn_update_contacts.resize(120, 40)
        self.btn_update_contacts.setFont(QFont("Arial", 12))
        self.btn_update_contacts.setStyleSheet("border-radius:5; border:1px solid black; \
                                                     background-color:#6DF680")

    def clicked_add(self):
        """This function is responsible for add contact in database"""
        name = self.lineedit_name.text()
        surname = self.lineedit_surname.text()
        phone_number = self.lineedit_phone_number.text()
        address = self.lineedit_address.text()

        is_repeted = None
        for element in self.lst:
            if phone_number == element[2]:
                is_repeted = "repeted"

        if "" in (name, surname, phone_number, address) or len(phone_number) < 9 \
                or (len(name) or len(surname)) < 3:
            self.label_message.setText("Please, enter all fields correctly")
            self.label_message.setStyleSheet("color: red")
            self.label_message.move(190, 310)
            self.label_message.resize(215, 18)
        elif is_repeted == "repeted":
            self.label_message.setText("There is already created contact with this phone number")
            self.label_message.setStyleSheet("color: red")
            self.label_message.move(100, 310)
            self.label_message.resize(400, 18)
        else:
            self.label_message.setText("Sucessfully added")
            self.label_message.setStyleSheet("color: green")
            self.label_message.move(230, 310)
            self.label_message.resize(215, 18)

            self.lineedit_name.setText("")
            self.lineedit_surname.setText("")
            self.lineedit_phone_number.setText("0")
            self.lineedit_address.setText("")

            contact = Contacts(name, surname, phone_number, address)
            insert_contact(contact)  # add contact in database

    def clicked_view(self):
        """This function opens second page"""

        self.table_view = CreateTable()
        CreateTable.table_view = self.table_view
        self.table_view.show()

    def clicked_update(self):
        """This function update contact with phone number"""

        name = self.lineedit_name.text()
        surname = self.lineedit_surname.text()
        phone_number = self.lineedit_phone_number.text()
        address = self.lineedit_address.text()
        if "" in (name, surname, phone_number, address) or len(phone_number) < 9 \
                or (len(name) or len(surname)) < 3:
            self.label_message.setText("Please, enter all fields correctly")
            self.label_message.setStyleSheet("color: red")
            self.label_message.move(190, 310)
            self.label_message.resize(215, 18)
        else:
            self.label_message.setText("")

            is_updated = None
            for element in self.lst:
                if element[2] == phone_number:
                    cont = Contacts(name, surname, phone_number, address)
                    update_contact(cont, name, surname, address)
                    is_updated = "updated"
                    self.label_message.setText("Sucessfully updated")
                    self.label_message.setStyleSheet("color: green")
                    self.label_message.move(230, 310)
                    self.label_message.resize(220, 18)

            if is_updated is None:
                self.label_message.setText("Please, enter correct phone number")
                self.label_message.setStyleSheet("color: red")
                self.label_message.move(170, 310)
                self.label_message.resize(260, 18)


def window():
    """This function opens main page"""
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


window()
