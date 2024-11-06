import os

FILE_NAME = "dict.txt"


def load_contacts():
    contacts = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, num, comment = line.strip().split(":")
                contacts[name] = {"number": num, "comment": comment}
    return contacts


def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        for name, info in contacts.items():
            file.write(f"{name}:{info['number']}:{info['comment']}\n")


def show_all_contacts():
    contacts = load_contacts()
    if not contacts:
        print("Справочник пуст.")
    else:
        for name, info in contacts.items():
            print(f"Имя: {name}, Номер: {info['number']}, Комментарий: {info['comment']}")


def create_contact():
    contacts = load_contacts()
    name = input("Введите имя: ")
    if name in contacts:
        print("Контакт с таким именем уже существует.")
        return
    number = input("Введите номер: ")
    comment = input("Введите комментарий: ")
    contacts[name] = {"number": number, "comment": comment}
    save_contacts(contacts)
    print("Контакт добавлен.")


def find_contact():
    contacts = load_contacts()
    name = input("Введите имя для поиска: ")
    if name in contacts:
        info = contacts[name]
        print(f"Имя: {name}, Номер: {info['number']}, Комментарий: {info['comment']}")
    else:
        print("Контакт не найден.")


def edit_contact():
    contacts = load_contacts()
    name = input("Введите имя для редактирования: ")
    if name in contacts:
        number = input("Введите новый номер: ")
        comment = input("Введите новый комментарий: ")
        contacts[name] = {"number": number, "comment": comment}
        save_contacts(contacts)
        print("Контакт обновлен.")
    else:
        print("Контакт не найден.")


def delete_contact():
    contacts = load_contacts()
    name = input("Введите имя для удаления: ")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Контакт удален.")
    else:
        print("Контакт не найден.")


def main():
    while True:
        print(
            "\n1. Показать все контакты\n2. Создать контакт\n3. Найти контакт\n4. Изменить контакт по имени\n5. Удалить контакт по имени\n6. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            show_all_contacts()
        elif choice == "2":
            create_contact()
        elif choice == "3":
            find_contact()
        elif choice == "4":
            edit_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()
