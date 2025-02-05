from contact import Contact

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def list_contacts(self):
        return self.contacts

    def find_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def remove_contact(self, name):
        contact = self.find_contact(name)
        if contact:
            self.contacts.remove(contact)


from contact import Contact
from exceptions import ContactNotFoundException, ContactExistsException, InvalidContactDataException


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        # Проверка на существование контакта с таким же именем
        if self.find_contact(contact.name):
            raise ContactExistsException

        # Проверка на корректность данных
        if not contact.name or not contact.phone or not contact.email:
            raise InvalidContactDataException

        self.contacts.append(contact)

    def list_contacts(self):
        return self.contacts

    def find_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def remove_contact(self, name):
        contact = self.find_contact(name)
        if not contact:
            raise ContactNotFoundException
        self.contacts.remove(contact)