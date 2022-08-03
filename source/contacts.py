"""In this file have created table's variables"""


class Contacts:
    """This class return name, surname, phone number, address from main page to second page"""

    def __init__(self, name, surname, phone_number, address):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.address = address

    def __repr__(self):
        return "Contacts('{}', '{}', {}, '{}')" \
            .format(self.name, self.surname, self.phone_number, self.address)
