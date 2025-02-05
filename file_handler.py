import json
from contact import Contact

class FileHandler:
    @staticmethod
    def save_to_file(contact_book, filename):
        with open(filename, 'w') as file:
            contacts_data = [
                {'name': contact.name, 'phone': contact.phone, 'email': contact.email}
                for contact in contact_book.list_contacts()
            ]
            json.dump(contacts_data, file)

    @staticmethod
    def load_from_file(filename):
        contact_book = ContactBook()
        try:
            with open(filename, 'r') as file:
                contacts_data = json.load(file)
                for data in contacts_data:
                    contact = Contact(data['name'], data['phone'], data['email'])
                    contact_book.add_contact(contact)
        except FileNotFoundError:
            print(f"Файл {filename} не найден.")
        except json.JSONDecodeError:
            print("Ошибка чтения файла.")
        return contact_book