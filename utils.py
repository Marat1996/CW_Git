import json


def get_all_operations(path) -> list[dict]:
    """
    Функция получения операций из файла
    :param path: путь к файлу
    :return: json с орерациями
    """
    with open(path, encoding='utf8') as file:
        return json.load(file)
