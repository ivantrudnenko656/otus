# phonebook.py
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class Phonebook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        self.contacts.append(Contact(name, phone))

    def search_contact(self, query):
        return [contact for contact in self.contacts if query in contact.name or query in contact.phone]

    def update_contact(self, old_name, new_name, new_phone):
        for contact in self.contacts:
            if contact.name == old_name:
                contact.name = new_name
                contact.phone = new_phone
                return True
        return False

    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name != name]

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            for contact in self.contacts:
                f.write(f"{contact.name},{contact.phone}\n")

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                name, phone = line.strip().split(',')
                self.add_contact(name, phone)

# phonebook.py

class ContactAlreadyExists(Exception):
    """Исключение для случая, когда контакт уже существует."""
    pass

class ContactNotFound(Exception):
    """Исключение для случая, когда контакт не найден."""
    pass

class InvalidInput(Exception):
    """Исключение для некорректного ввода."""
    pass

class Contact:
    def __init__(self, name, phone):
        if not name or not phone:
            raise InvalidInput("Имя и телефон не могут быть пустыми.")
        self.name = name
        self.phone = phone

class Phonebook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        if any(contact.name == name for contact in self.contacts):
            raise ContactAlreadyExists("Контакт с таким именем уже существует.")
        self.contacts.append(Contact(name, phone))

    def search_contact(self, query):
        return [contact for contact in self.contacts if query in contact.name or query in contact.phone]

    def update_contact(self, old_name, new_name, new_phone):
        for contact in self.contacts:
            if contact.name == old_name:
                contact.name = new_name
                contact.phone = new_phone
                return True
        raise ContactNotFound("Контакт не найден.")

    def delete_contact(self, name):
        if not self.search_contact(name):
            raise ContactNotFound("Контакт не найден.")
        self.contacts = [contact for contact in self.contacts if contact.name != name]

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            for contact in self.contacts:
                f.write(f"{contact.name},{contact.phone}\n")

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                name, phone = line.strip().split(',')
                self.add_contact(name, phone)

# phonebook.py

class ContactAlreadyExists(Exception):
    """Исключение для случая, когда контакт уже существует."""
    pass

class ContactNotFound(Exception):
    """Исключение для случая, когда контакт не найден."""
    pass

class InvalidInput(Exception):
    """Исключение для некорректного ввода."""
    pass

class Contact:
    def __init__(self, name, phone):
        if not name or not phone:
            raise InvalidInput("Имя и телефон не могут быть пустыми.")
        self.name = name
        self.phone = phone

class Phonebook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        if not name or not phone:
            raise InvalidInput("Имя и телефон не могут быть пустыми.")
        if any(contact.name == name for contact in self.contacts):
            raise ContactAlreadyExists("Контакт с таким именем уже существует.")
        self.contacts.append(Contact(name, phone))

    def search_contact(self, query):
        if not query:
            raise InvalidInput("Поисковый запрос не может быть пустым.")
        results = [contact for contact in self.contacts if query in contact.name or query in contact.phone]
        if not results:
            raise ContactNotFound("Контакт не найден.")
        return results

    def update_contact(self, old_name, new_name, new_phone):
        if not old_name or not new_name or not new_phone:
            raise InvalidInput("Имя и телефон не могут быть пустыми.")
        for contact in self.contacts:
            if contact.name == old_name:
                contact.name = new_name
                contact.phone = new_phone
                return True
        raise ContactNotFound("Контакт не найден.")

    def delete_contact(self, name):
        if not name:
            raise InvalidInput("Имя не может быть пустым.")
        if not self.search_contact(name):
            raise ContactNotFound("Контакт не найден.")
        self.contacts = [contact for contact in self.contacts if contact.name != name]

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            for contact in self.contacts:
                f.write(f"{contact.name},{contact.phone}\n")

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                name, phone = line.strip().split(',')
                self.add_contact(name, phone)