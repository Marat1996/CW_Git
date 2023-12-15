

from datetime import datetime


def mask_account_number(account_number: str) -> str:
    if account_number.startswith("Счет"):
        account_digits = "".join(filter(str.isdigit, account_number))
        return f"Счет {account_digits[:4]} {account_digits[4:6]}** **** {account_digits[-4:]}"
    elif account_number.startswith(("Maestro", "Master", "Visa")):
        card_number = "".join(filter(str.isdigit, account_number))
        return f"{account_number[:6]} {card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    else:
        return f"{account_number[:6]}{'*' * (len(account_number) - 12)}{account_number[-4:]}"


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
        masked_from = mask_account_number(self.from_)
        masked_to = mask_account_number(self.to)

        formatted_operation = f"{formatted_date} {self.description}\n" \
                              f"{masked_from} -> {masked_to}\n" \
                              f"{self.operation_amount['amount']} {self.operation_amount['currency']['name']}\n"
        return formatted_operation

    def convert_payment(self) -> str:
        if self.description.startswith("Перевод организации"):
            masked_from = mask_account_number(self.from_)
            masked_to = mask_account_number(self.to)
            return f"{masked_from} -> {masked_to}\n" \
                   f"{self.operation_amount['amount']} {self.operation_amount['currency']['name']}"
        else:
            return f"{self.description}\n" \
                   f"{mask_account_number(self.from_)} -> {mask_account_number(self.to)}\n" \
                   f"{self.operation_amount['amount']} {self.operation_amount['currency']['name']}"
