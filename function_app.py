import json
from work_file import save_data, load_data


def add_book(
        title: str,
        author: str,
        year: int
) -> str:
    """
    Добавляет ноовую книгу в библиотеку.
    :param title: Название книги
    :param author: Имя автора
    :param year: Год выпуска книги
    :return: string
    """
    books = load_data()
    new_book = {
        'id': len(books) + 1,
        'title': title,
        'author': author,
        'year': year,
        'status': 'в наличии'
    }
    books.append(new_book)
    save_data(books)
    print(f"Книга '{title}' добавлена в библиотеку.")


def delete_book(book_id: int) -> str:
    """
    Удаляет книгу по id
    :param book_id: Идентификатор книги
    :return: string
    """
    books = load_data()

    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            save_data(books)
            print(f"Книга с id {book_id} удалена из библиотеки.")
            return
    print(f"Книга с id {book_id} не найдена")


def get_book(query: str) -> str:
    """
    Поиск книги по названию, имени автора или году издания
    :param query: Название книги, Имя автора, Года издания
    :return: strting
    """
    books = load_data()
    results = [book for book in books if
               query.lower() in book['title'].lower() or query.lower() in book['author'].lower() or query == str(
                   book['year'])]
    if results:
        for book in results:
            print(
                f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, Год: {book['year']}, Статус: {book['status']}")
    else:
        print("Книги не найдены.")


def get_books() -> str:
    """
    Выводит все книги
    :return: string
    """
    books = load_data()
    if books:
        for book in books:
            print(
                f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, Год: {book['year']}, Статус: {book['status']}")
    else:
        print("В библиотеке нет книг.")


def change_book_status(book_id: str, new_status: str) -> str:
    """
    Меняет статус книги на "в наличи" либо "выдана"
    :param book_id: Идентификатор книги
    :param new_status: Новый статус для книги
    :return: string
    """
    books = load_data()
    for book in books:
        if book['id'] == book_id:
            if new_status in ['в наличии', 'выдана']:
                book['status'] = new_status
                save_data(books)
                print(f"Статус книги с id {book_id} изменен на '{new_status}'.")
                return
    print(f"Книга с id {book_id} не найдена.")
