import unittest
from contact import Contact
from contact_book import ContactBook
from exceptions import ContactNotFoundException, ContactExistsException, InvalidContactDataException

class TestContactBook(unittest.TestCase):

    def setUp(self):
        self.contact_book = ContactBook()

    def test_create_contact(self):
        contact = Contact("John Doe", "123-456-7890", "john@example.com")
        self.assertEqual(contact.name, "John Doe")
        self.assertEqual(contact.phone, "123-456-7890")
        self.assertEqual(contact.email, "john@example.com")

    def test_add_contact(self):
        contact = Contact("Jane Smith", "987-654-3210", "jane@example.com")
        self.contact_book.add_contact(contact)
        self.assertEqual(len(self.contact_book.list_contacts()), 1)
        self.assertEqual(self.contact_book.list_contacts()[0].name, "Jane Smith")

    def test_add_existing_contact(self):
        contact = Contact("Alice", "555-555-5555", "alice@example.com")
        self.contact_book.add_contact(contact)

        with self.assertRaises(ContactExistsException):
            self.contact_book.add_contact(contact)

    def test_remove_contact(self):
        contact = Contact("Bob", "444-444-4444", "bob@example.com")
        self.contact_book.add_contact(contact)
        self.contact_book.remove_contact("Bob")
        self.assertEqual(len(self.contact_book.list_contacts()), 0)

    def test_remove_non_existing_contact(self):
        with self.assertRaises(ContactNotFoundException):
            self.contact_book.remove_contact("Non Existing")

    def test_add_contact_with_invalid_data(self):
        invalid_contact = Contact("", "", "")
        with self.assertRaises(InvalidContactDataException):
            self.contact_book.add_contact(invalid_contact)

if __name__ == '__main__':
    unittest.main()