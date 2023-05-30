import database

def choose_action(phonebook):
    while True:
        print()
        print('Что вы хотите сделать?')
        user_choice = input('1 - Импортировать данные\n2 - Найти контакт\n3 - Добавить контакт\n4 - Изменить контакт\n5 - Удалить контакт\n6 - Просмотреть все контакты\n0 - Выйти из приложения\n')
        print()
        if user_choice == '1':
            file_to_add = input('Введите название импортируемого файла: ')
            database.import_data(file_to_add, phonebook)
        elif user_choice == '2':
            contact_list = database.read_file_to_dict(phonebook)
            database.find_contact(contact_list)
        elif user_choice == '3':
            database.add_new_contact(phonebook)
        elif user_choice == '4':
            database.change_contact(phonebook)
        elif user_choice == '5':
            database.delete_contact(phonebook)
        elif user_choice == '6':
            database.show_phonebook(phonebook)
        elif user_choice == '0':
            print('До свидания!')
            break
        else:
            print('Неправильно выбрана команда!')
            print()
            continue