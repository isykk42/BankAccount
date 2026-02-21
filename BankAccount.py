class BankAccount:

    title = "Bank Account"

    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

        self.__account_number = account_number
        self._routing_number = routing_number

    def deposit(self, amount):
        self.current_balance += amount

    def withdraw(self, amount):
        if self.current_balance - amount < self.minimum_balance:
            print("Remaining balance is less than the minimum balance.")
        else:
            self.current_balance -= amount

    def print_customer_information(self):
        print(BankAccount.title)
        print("Customer:", self.customer_name)
        print("Current Balance:", self.current_balance)
        print("Minimum Balance:", self.minimum_balance, "\n")

    def get_account_number(self):
        return self.__account_number

