import json


def read_contacts():
    """
    Функция для чтения файла contacts.txt
    """
    try:
        with open("contacts.txt", "r") as file:
            contacts = json.load(file)
            return contacts
    except FileNotFoundError:
        return []


def write_contacts(contacts):
    """
    Функция для записи данных в файл contacts.txt
    Если такого файла нет, он создается автоматически.
    """
    with open("contacts.txt", "w") as file:
        json.dump(contacts, file)


def display_contacts(contacts):
    """
    Функция для вывода всех контактов.
    На странице показывается по 5 контактов.
    """
    page: int = 1
    per_page: int = 5

    while True:
        start_index = (page - 1) * per_page
        end_index = start_index + per_page
        current_page = contacts[start_index:end_index]

        for contact in current_page:
            print(f"Контакт №: {contact['Index']}")
            print(f"Фамилия {contact['Last_name']}")
            print(f"Имя: {contact['First_name']}")
            print(f"Отчество: {contact['Patronymic']}")
            print(f"Название организации: {contact['Name_of_the_organization']}")
            print(f"Рабочий телефон: {contact['Work_phone']}")
            print(f"Личный телефон: {contact['Personal_phone']}")
            print()

        print(f"Страница {page}")

        command = input("Введите 'дальше' для перехода на следующую страницу, 'назад' чтобы вернуться на предыдущую страницу, или 'выход' для выхода из меню: ")

        if command == "дальше":
            if end_index >= len(contacts):
                print("Контактов больше нет.")
                break
            page += 1
        elif command == "назад":
            if page == 1:
                print("Это первая страница.")
            else:
                page -= 1
        elif command == "выход":
            break
        else:
            print("Неправильная команда.")


def add_contact(contacts):
    """
    Функция для добавления нового контакта.
    """
    index = len(contacts) + 1
    last_name = input("Введите фимилию: ")
    first_name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    name_of_the_organization = input("Введите название организации: ")
    work_phone = input("Введите рабочий номер телефона: ")
    personal_phone = input("Введите личный номер телефона: ")

    contact = {
        "Index": index,
        "Last_name": last_name,
        "First_name": first_name,
        "Patronymic": patronymic,
        "Name_of_the_organization": name_of_the_organization,
        "Work_phone": work_phone,
        "Personal_phone": personal_phone
    }

    contacts.append(contact)

    print("Контакт успешно добавлен!.")


def edit_contact(contacts):
    """
    Функция для изменения контакта.
    Для того чтобы изменить контакт необходимо указать его
    порядковый номер-индекс
    """
    index = int(input("Введите номер контакта который хотите изменить: "))

    if index < 1 or index > len(contacts):
        print("Такого контакта не существует.")
    else:
        contact = contacts[index-1]

        last_name = input("Введите новую фимилию: ")
        first_name = input("Введите новое имя: ")
        patronymic = input("Введите новое отчество: ")
        name_of_the_organization = input("Введите новое название организации: ")
        work_phone = input("Введите новый рабочий номер телефона: ")
        personal_phone = input("Введите новый личный номер телефона: ")

        contact["Last_name"] = last_name
        contact["First_name"] = first_name
        contact["Patronymic"] = patronymic
        contact["Name_of_the_organization"] = name_of_the_organization
        contact["Work_phone"] = work_phone
        contact["Personal_phone"] = personal_phone

        print("Контакт успешно изменён!")


def find_contact_by_name_and_phone(contacts):
    """
    Функция для поиска контакта в списке всех контактов.
    Поиск выполняется в данном случае по двум полям:
    1. Фамилии и 2. Номеру личного телефона.
    После поиска данный контакт целиком выводится.
    """
    contacts = read_contacts()

    last_name = input("Введите фамилию: ")
    personal_phone = input("Введите личный телефон: ")
    found_contact = False

    for contact in contacts:
        if contact["Last_name"] == last_name and contact["Personal_phone"] == personal_phone:
            found_contact = True
            print(f"Контакт №: {contact['Index']}")
            print(f"Фамилия {contact['Last_name']}")
            print(f"Имя: {contact['First_name']}")
            print(f"Отчество: {contact['Patronymic']}")
            print(f"Название организации: {contact['Name_of_the_organization']}")
            print(f"Рабочий телефон: {contact['Work_phone']}")
            print(f"Личный телефон: {contact['Personal_phone']}")
            print()
            
    if not found_contact:
        print("Контакт не найден.")


def phone_directory():
    """
    Функция главного меню.
    Всего 5 разделов.
    """
    contacts = read_contacts()

    while True:
        print("Главное меню:")
        print("1. Просмотреть все контакты")
        print("2. Добавить контакт")
        print("3. Изменить контакт")
        print("4. Найти контакт")
        print("5. Сохранить и выйти")

        choice = input("Выберете нужное действие(1-5): ")

        if choice == "1":
            if len(contacts) == 0:
                print("Контакты не найдены.")
            else:
                display_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            if len(contacts) == 0:
                print("Контакты не найдены.")
            else:
                edit_contact(contacts)
        elif choice == "4":
            find_contact_by_name_and_phone(contacts)
        elif choice == "5":
            write_contacts(contacts)
            break
        else:
            print("Ошибочка  (-_-).")


phone_directory()
