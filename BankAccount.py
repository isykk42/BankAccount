class BankAccount:

    title = "Bank Account"

    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

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


fart = BankAccount("Meow", 100, 20)
poop = BankAccount("Miau", 200, 50)

fart.print_customer_information()
fart.deposit(75)
fart.print_customer_information()

poop.print_customer_information()
poop.withdraw(75)
poop.print_customer_information()

poop.withdraw(150)
poop.print_customer_information()

