import unittest
from datetime import datetime
from models.operation import Operation


class TestOperation(unittest.TestCase):

    def setUp(self):
        self.sample_operation = Operation(
            pk=1,
            date="2019-07-03T18:35:29.512364",
            state="completed",
            operation_amount={
                "amount": 100,
                "currency": {"name": "USD", "code": "USD"}
            },
            description="Transfer",
            from_="Account 1234",
            to="Account 5678"
        )

    def test_format_operation(self):
        formatted_output = self.sample_operation.format_operation().strip()
        expected_output = (
            "03.07.2019 Transfer\n"
            "Accoun1234 -> Accoun5678\n"
            "100 USD"
        )
        self.assertEqual(formatted_output, expected_output)

    def test_convert_payment_transfer(self):
        converted_payment = self.sample_operation.convert_payment().strip()
        expected_output = (
            "Transfer\n"
            "Accoun1234 -> Accoun5678\n"
            "100 USD"
        )
        self.assertEqual(converted_payment, expected_output)

    def test_convert_payment_other(self):
        self.sample_operation.description = "Deposit"
        converted_payment = self.sample_operation.convert_payment().strip()
        expected_output = (
            "Deposit\n"
            "Accoun1234 -> Accoun5678\n"
            "100 USD"
        )
        self.assertEqual(converted_payment, expected_output)

    def test_convert_payment_deposit(self):
        self.sample_operation.description = "Other"
        converted_payment = self.sample_operation.convert_payment().strip()
        expected_output = (
            "Other\n"
            "Accoun1234 -> Accoun5678\n"
            "100 USD"
        )
        self.assertEqual(converted_payment, expected_output)




if __name__ == '__main__':
    unittest.main()
