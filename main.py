from function_app import add_book, change_book_status, get_book, delete_book, get_books

if __name__ == "__main__":
    while True:
        print("\nВыберите действие:")
        print("1. Добавить к4игу")
        print("2. Удалить книгу")
        print("3. Поиск книги")
        print("4. Отобразить все книги")
        print("5. Изменить статус книги")
        print("6. Выход")
        choice = input("Введите номер действия: ")
        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания книги: ")
            add_book(title, author, year)
        elif choice == '2':
            book_id = int(input("Введите id книги: "))
            delete_book(book_id)
        elif choice == '3':
            query = input("Введите запрос для поиска (название, автор или год): ")
            get_book_by_id(query)
        elif choice == '4':
            get_books()
        elif choice == '5':
            book_id = int(input("Введите id книги: "))
            new_status = input("Введите новый статус ('в наличии' или 'выдана'): ")
            change_book_status(book_id, new_status)
        elif choice == '6':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
