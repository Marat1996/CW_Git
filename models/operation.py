from datetime import datetime


class Operation:
    def __init__(
            self,
            pk: int,
            date: str,
            state: str,
            operation_amount: dict,
            description: str,
            from_: str,
            to: str

    ):
        self.pk = pk
        self.date = date
        self.state = state
        self.operation_amount = operation_amount
        self.description = description
        self.from_ = from_
        self.to = to

    def format_operation(self) -> str:
        formatted_date = datetime.strptime(self.date, "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        masked_from = self.mask_account_number(self.from_)
        masked_to = self.mask_account_number(self.to)

        formatted_operation = f"{formatted_date} {self.description}\n" \
                              f"{masked_from} -> {masked_to}\n" \
                              f"{self.operation_amount['amount']} {self.operation_amount['currency']['name']}\n"
        return formatted_operation

    def mask_account_number(self, account_number: str) -> str:
        if account_number.startswith("Счет"):
            # Маскировка первых двух цифр счета
            return f"Счет {'*' * (len(account_number) - 4)}{account_number[-2:]}"
        elif account_number.startswith(("Maestro", "Master", "Visa")):
            # Разбиваем номер карты на части
            card_parts = account_number.split()
            # Маскировка номера карты
            masked_card_number = f"{card_parts[0]} {'*' * 4} {'*' * 4} {card_parts[1][-4:]}"
            return f"{masked_card_number}"
        else:
            # Другие случаи, просто маскируем середину
            return f"{account_number[:6]}{'*' * (len(account_number) - 12)}{account_number[-4:]}"

    def convert_payment(self) -> str:
        if self.description.startswith("Перевод организации"):
            masked_from = self.mask_account_number(self.from_)
            masked_to = self.mask_account_number(self.to)
            return f"{masked_from} -> {masked_to}\n" \
                   f"{self.operation_amount['amount']} {self.operation_amount['currency']['name']}"
        elif self.description.startswith("Открытие вклада"):
            return f"Открытие вклада\n" \
                   f" -> {self.mask_account_number(self.to)}\n" \
                   f"{self.operation_amount['amount']} {self.operation_amount['currency']['name']}"
        # Добавьте другие условия для различных видов платежей, если необходимо
        else:
            return f"{self.description}\n" \
                   f"{self.mask_account_number(self.from_)} -> {self.mask_account_number(self.to)}\n" \
                   f"{self.operation_amount['amount']} {self.operation_amount['currency']['name']}"
