import json
import os


def load_data() -> list | None:
    """
    Функция для загрузки файла .json или создание файла если его еще нет в директории
    :return: None
    """
    if not os.path.exists('library.json'):
        return []
    with open('library.json', 'r') as file:
        return json.load(file)


def save_data(data: json) -> None:
    """
    Функция для сохранения списка книг в файл.json
    :param data: Список книг в формате json
    :return: None
    """
    with open('library.json', 'w') as file:
        json.dump(data, file, indent=4)
