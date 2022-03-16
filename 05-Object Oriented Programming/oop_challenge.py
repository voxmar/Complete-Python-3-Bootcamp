
class Account:
    # Attributes: owner, balance
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    # methods: deposit and withdraw
    def deposit(self, amount):
        self.balance += amount
        print(f'£{amount} deposited.\nNew balance: £{self.balance}')


    def withdraw(self, amount):
        # test to make sure account can't be overdrawn
        if amount <= self.balance:
            self.balance -= amount
            print(f'£{amount} withdrawn.\nNew balance: £{self.balance}')
        else:
            print(f'Withdrawing £{amount} would cause the account to become overdrawn')

    def __str__(self):
        return f'Account holder:\t\t{self.owner}\nCurrent balance: \t£{self.balance}'


def main():
    acc1 = Account('Mariette', 1500)
    print(acc1)
    print(acc1.owner)
    print(acc1.balance)
    acc1.deposit(50)
    acc1.withdraw(500)
    acc1.withdraw(2000)

if __name__ == '__main__':
    main()
