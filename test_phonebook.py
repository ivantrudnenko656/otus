import unittest
import os
from phonebook import Phonebook


class TestPhonebook(unittest.TestCase):

    def setUp(self):
        self.phonebook = Phonebook()

    def test_add_contact(self):
        self.phonebook.add_contact("John Doe", "123456789")
        self.assertEqual(len(self.phonebook.contacts), 1)
        self.assertEqual(self.phonebook.contacts[0].name, "John Doe")
        self.assertEqual(self.phonebook.contacts[0].phone, "123456789")

    def test_search_contact_by_name(self):
        self.phonebook.add_contact("John Doe", "123456789")
        self.phonebook.add_contact("Jane Smith", "987654321")
        results = self.phonebook.search_contact("John")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "John Doe")

    def test_search_contact_by_phone(self):
        self.phonebook.add_contact("John Doe", "123456789")
        results = self.phonebook.search_contact("123456789")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "John Doe")

    def test_update_contact(self):
        self.phonebook.add_contact("John Doe", "123456789")
        success = self.phonebook.update_contact("John Doe", "Johnny Doe", "987654321")
        self.assertTrue(success)
        self.assertEqual(self.phonebook.contacts[0].name, "Johnny Doe")
        self.assertEqual(self.phonebook.contacts[0].phone, "987654321")

    def test_delete_contact(self):
        self.phonebook.add_contact("John Doe", "123456789")
        self.phonebook.delete_contact("John Doe")
        self.assertEqual(len(self.phonebook.contacts), 0)

    def test_save_and_load_file(self):
        self.phonebook.add_contact("John Doe", "123456789")
        self.phonebook.save_to_file("test_contacts.txt")

        new_phonebook = Phonebook()
        new_phonebook.load_from_file("test_contacts.txt")

        self.assertEqual(len(new_phonebook.contacts), 1)
        self.assertEqual(new_phonebook.contacts[0].name, "John Doe")
        self.assertEqual(new_phonebook.contacts[0].phone, "123456789")

    def tearDown(self):
        # Удаление файла после теста
        if os.path.exists("test_contacts.txt"):
            os.remove("test_contacts.txt")


if __name__ == '__main__':
    unittest.main()

import unittest
from phonebook import Phonebook, ContactAlreadyExists, ContactNotFound, InvalidInput


class TestPhonebookExceptions(unittest.TestCase):

    def setUp(self):
        self.phonebook = Phonebook()

    def test_add_contact_with_empty_name(self):
        with self.assertRaises(InvalidInput):
            self.phonebook.add_contact("", "123456789")

    def test_add_contact_with_empty_phone(self):
        with self.assertRaises(InvalidInput):
            self.phonebook.add_contact("John Doe", "")

    def test_add_existing_contact(self):
        self.phonebook.add_contact("John Doe", "123456789")
        with self.assertRaises(ContactAlreadyExists):
            self.phonebook.add_contact("John Doe", "987654321")

    def test_update_non_existing_contact(self):
        with self.assertRaises(ContactNotFound):
            self.phonebook.update_contact("Non Existing", "New Name", "123456")

    def test_delete_non_existing_contact(self):
        with self.assertRaises(ContactNotFound):
            self.phonebook.delete_contact("Non Existing")

    def test_create_contact_with_invalid_data(self):
        with self.assertRaises(InvalidInput):
            Contact("", "123456789")
        with self.assertRaises(InvalidInput):
            Contact("John Doe", "")


if __name__ == '__main__':
    unittest.main()

import unittest
from phonebook import Phonebook, ContactAlreadyExists, ContactNotFound, InvalidInput


class TestPhonebookBoundaryConditions(unittest.TestCase):

    def setUp(self):
        self.phonebook = Phonebook()

    def test_add_empty_contact(self):
        with self.assertRaises(InvalidInput):
            self.phonebook.add_contact("", "123456789")
        with self.assertRaises(InvalidInput):
            self.phonebook.add_contact("John Doe", "")

    def test_search_non_existing_contact(self):
        with self.assertRaises(ContactNotFound):
            self.phonebook.search_contact("Non Existing")

    def test_search_with_empty_query(self):
        with self.assertRaises(InvalidInput):
            self.phonebook.search_contact("")

    def test_delete_empty_name(self):
        with self.assertRaises(InvalidInput):
            self.phonebook.delete_contact("")

    def test_delete_non_existing_contact(self):
        with self.assertRaises(ContactNotFound):
            self.phonebook.delete_contact("Non Existing")

    def test_update_with_empty_fields(self):
        self.phonebook.add_contact("John Doe", "123456789")
        with self.assertRaises(InvalidInput):
            self.phonebook.update_contact("John Doe", "", "987654321")
        with self.assertRaises(InvalidInput):
            self.phonebook.update_contact("John Doe", "Jane Doe", "")

    def test_update_non_existing_contact(self):
        with self.assertRaises(ContactNotFound):
            self.phonebook.update_contact("Non Existing", "New Name", "123456")


if __name__ == '__main__':
    unittest.main()

import unittest
from phonebook import Phonebook, ContactAlreadyExists, ContactNotFound, InvalidInput


class TestPhonebookParameterizedTests(unittest.TestCase):

    def setUp(self):
        self.phonebook = Phonebook()

    def test_add_contact_formats(self):
        test_cases = [
            ("John Doe", "123-456-7890"),  # стандартный формат
            ("Jane Smith", "987654321"),  # без дефисов
            ("Alice Wonderland", "+1-800-555-0199"),  # формат с кодом страны
            ("Bob", "555.123.4567"),  # формат с точками
            ("Carol O'Connell", "(555) 123-4567"),  # формат с круглой скобкой
        ]

        for name, phone in test_cases:
            with self.subTest(name=name, phone=phone):
                self.phonebook.add_contact(name, phone)
                self.assertTrue(
                    any(contact.name == name and contact.phone == phone for contact in self.phonebook.contacts))

    def test_search_contact_formats(self):
        self.phonebook.add_contact("John Doe", "123-456-7890")
        self.phonebook.add_contact("Jane Smith", "987654321")
        test_cases = [
            ("John Doe", 1),  # Поиск по полному имени
            ("Jane", 1),  # Поиск по части имени
            ("123-456-7890", 1),  # Поиск по номеру телефона с дефисами
            ("987654321", 1),  # Поиск по номеру телефона без дефисов
            ("Alice", 0),  # Поиск по несуществующему имени
        ]

        for query, expected_count in test_cases:
            with self.subTest(query=query, expected_count=expected_count):
                results = self.phonebook.search_contact(query)
                self.assertEqual(len(results), expected_count)

    def test_update_contact_formats(self):
        self.phonebook.add_contact("John Doe", "123-456-7890")
        self.phonebook.add_contact("Jane Smith", "987654321")

        update_cases = [
            ("John Doe", "Johnny", "123-456-7890"),  # изменение имени
            ("Jane Smith", "Jane Doe", "987654321"),  # изменение имени
            ("John Doe", "Johnathan Doe", "111-222-3333"),  # изменение имени и телефона
        ]

        for old_name, new_name, new_phone in update_cases:
            with self.subTest(old_name=old_name, new_name=new_name, new_phone=new_phone):
                self.phonebook.update_contact(old_name, new_name, new_phone)
                updated_contact = self.phonebook.search_contact(new_name)
                self.assertEqual(len(updated_contact), 1)
                self.assertEqual(updated_contact[0].phone, new_phone)

    def test_delete_contact(self):
        self.phonebook.add_contact("John Doe", "123-456-7890")
        self.phonebook.add_contact("Jane Smith", "987654321")

        delete_cases = [
            ("John Doe", 1),  # удаление существующего контакта
            ("Non Existent", 0),  # удаление несуществующего контакта
        ]

        for name, expected_count in delete_cases:
            with self.subTest(name=name, expected_count=expected_count):
                if expected_count == 1:
                    self.phonebook.delete_contact(name)
                results = self.phonebook.contacts
                self.assertEqual(len(results), expected_count)


if __name__ == '__main__':
    unittest.main()