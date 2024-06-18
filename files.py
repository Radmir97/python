def work_with_phonebook():
    choice = show_menu()

    phone_book = read_txt('phon.txt')

    while choice != 8:
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input('Введите фамилию: ')
            print(find_by_lastname(phone_book, last_name))
        elif choice == 3:
            last_name = input('Введите фамилию: ')
            new_number = input('Введите новый номер: ')
            print(change_number(phone_book, last_name, new_number))
        elif choice == 4:
            last_name = input('Введите фамилию: ')
            print(delete_by_lastname(phone_book, last_name))
        elif choice == 5:
            number = input('Введите номер: ')
            print(find_by_number(phone_book, number))
        elif choice == 6:
            user_data = input('Введите новые данные: ')
            add_user(phone_book, user_data)
            write_txt('phon.txt', phone_book)
        elif choice == 7:
            source_file = input('Введите имя исходного файла: ')
            target_file = input('Введите имя целевого файла: ')
            line_number = int(input('Введите номер строки для копирования: '))
            copy_line(source_file, target_file, line_number)

        choice = show_menu()

def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Изменить номер абонента\n"
          "4. Удалить абонента\n"
          "5. Найти абонента по номеру\n"
          "6. Добавить абонента в справочник\n"
          "7. Скопировать строку из одного файла в другой\n"
          "8. Закончить работу")
    choice = int(input())
    return choice

def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']

    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.strip().split(',')))
            phone_book.append(record)

    return phone_book

def write_txt(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as phout:
        for record in phone_book:
            line = ','.join(record.values())
            phout.write(line + '\n')

def copy_line(source_file, target_file, line_number):
    with open(source_file, 'r', encoding='utf-8') as src, open(target_file, 'a', encoding='utf-8') as tgt:
        lines = src.readlines()
        if 0 <= line_number - 1 < len(lines):
            tgt.write(lines[line_number - 1])
        else:
            print(f"Строка {line_number} не найдена в файле {source_file}")

# Placeholder functions for the required functionality
def print_result(phone_book):
    for record in phone_book:
        print(record)

def find_by_lastname(phone_book, last_name):
    for record in phone_book:
        if record['Фамилия'] == last_name:
            return record
    return "Не найдено"

def change_number(phone_book, last_name, new_number):
    for record in phone_book:
        if record['Фамилия'] == last_name:
            record['Телефон'] = new_number
            return "Номер изменен"
    return "Не найдено"

def delete_by_lastname(phone_book, last_name):
    for record in phone_book:
        if record['Фамилия'] == last_name:
            phone_book.remove(record)
            return "Запись удалена"
    return "Не найдено"

def find_by_number(phone_book, number):
    for record in phone_book:
        if record['Телефон'] == number:
            return record
    return "Не найдено"

def add_user(phone_book, user_data):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    record = dict(zip(fields, user_data.split(',')))
    phone_book.append(record)

work_with_phonebook()
