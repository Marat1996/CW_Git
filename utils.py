import json

from models.operation import Operation


def get_all_operations(path) -> list[dict]:
    """
    Функция получения операций из файла
    :param path: путь к файлу
    :return: json с орерациями
    """
    with open(path, encoding='utf8') as file:
        return json.load(file)


def get_operations_instances(operations: list[dict]):
    operation_instances = []
    for operation in operations:
        if operation:
            operation_instance = Operation(
                pk=operation["id"],
                date=operation["date"],
                state=operation["state"],
                operation_amount=operation["operationAmount"],
                description=operation["description"],
                from_=operation.get("from", ""),
                to=operation["to"]

            )
            operation_instances.append(operation_instance)
    return operation_instances
