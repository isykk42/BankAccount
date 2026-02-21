from BankAccount import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)

        self.transfer_limit = transfer_limit
        self.transfers_made = 0

    def transfer(self, amount):
        if self.transfers_made >= self.transfer_limit:
            print("Transfer limit reached")
            return

        if self.current_balance - amount < self.minimum_balance:
            print("Insufficient funds")
            return

        self.current_balance -= amount
        self.transfers_made += 1

        print("Transfer successful")
        print(amount, " has been transferred. Your current balance is now ", self.current_balance)
        print("You have used ", self.transfers_made, " transfers, you have ", self.transfer_limit-self.transfers_made, " transfers left.")
