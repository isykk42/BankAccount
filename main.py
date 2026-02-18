from SavingsAccount import SavingsAccount
from CheckingAccount import CheckingAccount


def main():

    # two savings accounts
    s1 = SavingsAccount("Ravi", 2000, 0, "6767677", "021000021", 0.03)
    s2 = SavingsAccount("Thanh", 98000, 0, "7676766", "021000021", 0.02)

    s1.deposit(200)
    earned = s1.apply_interest()
    print("Interest:", earned)
    s1.print_customer_information()

    s2.apply_interest()
    s2.print_customer_information()


if __name__ == "__main__":
    main()