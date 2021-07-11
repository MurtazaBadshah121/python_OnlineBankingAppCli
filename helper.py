class Account(object):

    def __init__(self, number, owner, balance, limit=1000.0):
        self.__number = number
        self.__owner = owner
        self.__balance = balance
        self.__limit = limit

    def view_balance(self):
        print("The current balance of your account is {}".format(self.balance))

    def view_account(self):
        print("The current account holder is {}".format(self.owner))

    def deposit(self, amount):
        self.__balance += amount

    def transfer_money(self, amount, account):
        self.withdraw(amount)
        account.deposit(amount)


# -----------Coding the getters and setter for the account-------------------

    @property
    def balance(self):
        return self.__balance

    @property
    def owner(self):
        return self.__owner

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, limit):
        self.__limit = limit


#-----------------Setting the private methods -----------------------------

    def __can_withdraw(self, amount_withdraw):
        available_withdraw = self.__balance + self.__limit
        return amount_withdraw <= available_withdraw

    def withdraw(self, amount_withdraw):
        if self.__can_withdraw(amount_withdraw):
            self.__balance -= amount_withdraw
        else:
            print("The value {} is higher than the limit".format(amount_withdraw))

#------------------Static method ------------------------------------------

    @staticmethod
    def code_banks():
        return {'Royal Bank of Canada': '003', 'Scotia Bank': '002', 'Bank of Montreal': '001'}