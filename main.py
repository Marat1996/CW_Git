from datetime import datetime

from settings import OPERATIONS_PATH
from utils import get_all_operations, get_operations_instances


def main():
    all_operations = get_all_operations(OPERATIONS_PATH)
    operation_instances = get_operations_instances(all_operations)

    sorted_operations = sorted(operation_instances, key=lambda op: datetime.strptime(op.date, "%Y-%m-%dT%H:%M:%S.%f"),
                               reverse=True)

    executed_operations = [op for op in sorted_operations if op.is_executed()]
    last_executed_operations = executed_operations[:5]

    print("\nLast Executed Operations:")
    for operation_instance in last_executed_operations:
        formatted_operation = operation_instance.format_operation()
        print(formatted_operation)
        print()


if __name__ == '__main__':
    main()
