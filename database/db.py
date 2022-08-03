"""This file create db and table and is connected with sql"""

import sqlite3

conn = sqlite3.connect('database/contacts.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS contacts (
            name text4,
            surname text4,
            phone_number text4,
            address text4
)""")


def all_contacts():
    """This function return all contacts with list"""

    connection = sqlite3.connect('database/contacts.db')
    cur = connection.cursor()
    with connection:
        cur.execute("SELECT * FROM contacts")
        contact = cur.fetchall()
        lst = []
        for cont in contact:
            lst.append(cont)
        return lst


def insert_contact(contact):
    """This function insert a contact in table"""

    connection = sqlite3.connect('database/contacts.db')
    cur = connection.cursor()
    with connection:
        cur.execute("INSERT INTO contacts VALUES (:name, :surname, :phone_number, :address)",
                    {'name': contact.name, 'surname': contact.surname,
                     'phone_number': contact.phone_number, 'address': contact.address})


def update_contact(contact, name, surname, address):
    """This function update the contact"""

    connection = sqlite3.connect('database/contacts.db')
    cur = connection.cursor()
    with connection:
        cur.execute("""UPDATE contacts SET name = :name, surname = :surname, address = :address
                    WHERE phone_number = :phone_number""",
                    {'name': name, 'surname': surname, 'phone_number': contact.phone_number,
                     'address': address})


def delete_contact(phone_number):
    """This function delete the contact"""

    connection = sqlite3.connect('database/contacts.db')
    cur = connection.cursor()
    with connection:
        cur.execute("DELETE from contacts WHERE phone_number = :phone_number",
                    {'phone_number': phone_number})


conn.commit()
conn.close()
