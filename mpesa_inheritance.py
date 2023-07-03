class MpesaTransaction:
    def __init__(self, transaction_id, amount):
        self.transaction_id = transaction_id
        self.amount = amount
    def process_transaction(self):
        raise NotImplementedError("Subclass to use this method")
class DepositTransaction(MpesaTransaction):
    def process_transaction(self):
        print(f"Deposit transaction with ID {self.transaction_id} processed. Amount {self.amount}")
class Withdrawal_Transaction(MpesaTransaction):
    def process_transaction(self):
        print(f"Withdrawal transaction with ID {self.transaction_id} processed. Amount {self.amount}")
class Payment_Transaction(MpesaTransaction):
    def __init__(self, transaction_id, amount, recepient):
        super().__init__(transaction_id, amount)
        self.recepient = recepient
    def process_transaction(self):
        print(f"Payment transaction with ID {self.transaction_id} processed. Amount {self.amount}. Recepient {self.recepient}")
deposit = DepositTransaction("DHTY", 2000)
deposit.process_transaction()
withdrawal = Withdrawal_Transaction("FJIT", 3670)
withdrawal.process_transaction()
payment = Payment_Transaction("JOPR", 5680, "David Muli")
payment.process_transaction()