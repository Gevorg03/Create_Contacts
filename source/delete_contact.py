"""This file is used to delete contact from table"""

from functools import partial
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QIcon, QRegExpValidator, QFont
from PyQt5.QtWidgets import QLabel, QLineEdit, QComboBox, QWidget, QPushButton
from source import contact_view
from database.db import delete_contact, all_contacts


class DeleteContact(QWidget):
    """This class show Lineedit to input the contact name to delete"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(300, 200)
        self.setWindowTitle("Delete Contact")
        self.setStyleSheet("background-color: #FFFFFF")
        self.setWindowIcon(QIcon('content/add_contact.png'))

        self.init_ui()

    def init_ui(self):
        """This function create label, lineedit and button"""

        self.label_txt = QLabel("Enter the name of contact for delete", self)
        self.label_txt.setFont(QFont("Arial", 11))
        self.label_txt.resize(240, 20)
        self.label_txt.move(5, 5)

        regex = QRegExp("[a-z-A-Z_]+")
        validator = QRegExpValidator(regex)
        self.lineedit_name = QLineEdit(self)
        font_name = self.lineedit_name.font()
        font_name.setPointSize(13)
        self.lineedit_name.setFont(font_name)
        self.lineedit_name.setValidator(validator)  # Only letters can be inputed
        self.lineedit_name.setStyleSheet("border: 1px solid green")
        self.lineedit_name.setMaxLength(15)
        self.lineedit_name.move(5, 30)
        self.lineedit_name.resize(240, 35)

        self.btn_delete_contacts = QPushButton("Delete Contact", self)
        self.btn_delete_contacts.clicked.connect(self.clicked_delete)
        self.btn_delete_contacts.move(90, 75)
        self.btn_delete_contacts.resize(120, 40)
        self.btn_delete_contacts.setFont(QFont("Arial", 12))
        self.btn_delete_contacts.setStyleSheet("border-radius:5; border:1px solid black; \
                                                                     background-color:#6DF680")

    def clicked_delete(self):
        """This function delete contact"""

        name = self.lineedit_name.text()
        contact = all_contacts()
        lst = []
        for cont in contact:
            lst.append(list(cont))

        lst_name_surname = [] # the same name's list
        count = 0  # names count
        for element in lst:
            if element[0] == name:
                count += 1
                phone_number = element[2]
                lst_name_surname.append([name, element[1], element[2]])

        if count == 0:
            self.label_txt.setText("There is no such contact")
            self.label_txt.setStyleSheet("color: red")
            self.label_txt.setFont(QFont("Arial", 11))
            self.label_txt.move(5, 0)
            self.label_txt.resize(240, 20)
        elif count == 1:
            # delete automatically
            delete_contact(phone_number)
            self.close()
            obj = contact_view.CreateTable()
            obj.close_table()
        else:
            # ask which contact delete
            self.combo_box = QComboBox(self)
            self.combo_box.resize(200, 25)
            self.combo_box.move(50, 120)
            self.combo_box.show()
            for element in lst_name_surname:
                self.combo_box.addItem(f"{element[0]} {element[1]}")
            self.combo_box.activated.connect(partial(self.check_index, lst_name_surname))

    def check_index(self, lst_name_surname):
        """This function delete selected contact from combobox"""

        index = self.combo_box.currentIndex()
        delete_contact(lst_name_surname[index][2])
        obj = contact_view.CreateTable()
        obj.close_table()
        self.close()
