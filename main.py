from settings import OPERATIONS_PATH
from utils import get_all_operations, get_operations_instances


def main():
    all_operations = get_all_operations(OPERATIONS_PATH)
    operation_instances = get_operations_instances(all_operations)
    print()


if __name__ == '__main__':
    main()