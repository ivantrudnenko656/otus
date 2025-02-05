class ContactNotFoundException(Exception):
    def __init__(self, message="Контакт не найден."):
        self.message = message
        super().__init__(self.message)


class ContactExistsException(Exception):
    def __init__(self, message="Контакт уже существует."):
        self.message = message
        super().__init__(self.message)


class InvalidContactDataException(Exception):
    def __init__(self, message="Данные контакта недействительны."):
        self.message = message
        super().__init__(self.message)