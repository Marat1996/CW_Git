from settings import OPERATIONS_PATH
from utils import get_all_operations, get_operations_instances


def main():
    all_operations = get_all_operations(OPERATIONS_PATH)
    operation_instances = get_operations_instances(all_operations)

    for operation_instance in operation_instances[:5]:
        formatted_operation = operation_instance.format_operation()
        print(formatted_operation)
        print()


if __name__ == '__main__':
    main()
