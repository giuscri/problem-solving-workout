class account:
    def __init__(self, initial_amount):
        self.amount = initial_amount
    def balance(self):
        return self.amount
    def withdraw(self, amount):
        self.amount -= amount
    def deposit(self, amount):
        self.amount += amount

class safe_account(account):
    def __init__(self, initial_amount):
        self._amount = initial_amount
    def safe_get(self):
        print('[Safe getting]')
        return self._amount
    def safe_set(self, amount):
        print('[Safe setting]')
        assert amount >= 0, \
           'Not admitted operation: ' \
           'the final balance {} must be positive'.format(amount)
        self._amount = amount
    amount = property(safe_get, safe_set)

class account_with_calculated_balance:
    def __init__(self, initial_amount):
        self._deposits = initial_amount
        self._withdrawals = 0
    def deposit(self, amount):
        self._deposits += amount
    def withdraw(self, amount):
        self._withdrawals += amount

    def calculate_balance(self):
        return self._deposits - self._withdrawals
    def zero_balance(self):
        self._deposits = 0
        self._withdrawals = 0
    balance = property(calculate_balance, None, zero_balance)

class ssafe_account(account):
    class d:
        def __get__(self, instance, owner):
            return instance._amount
        def __set__(self, instance, amount):
            assert amount >= 0, \
               'Not admitted operation: ' \
               'the final balance {} must be positive'.format(amount)
            instance._amount = amount

    def __init__(self, initial_amount):
        self._amount = initial_amount
    
    amount = d()

class aaccount_with_calculated_balance:
    def __init__(self, initial_amount):
        self._deposits = initial_amount
        self._withdrawals = 0
    def deposit(self, amount):
        self._deposits += amount
    def withdraw(self, amount):
        self._withdrawals += amount

    class d:
        def __get__(self, instance, owner):
            return instance._deposits - instance._withdrawals
        def __delete__(self, instance):
            self._deposits, self._withdrawals = 0, 0

    balance = d()

class sssafe_account(account):
    def __setattr__(self, attribute, amount):
        assert amount >= 0, \
           'Not admitted operation: ' \
           'the final balance {} must be positive'.format(amount)
        self.__dict__[attribute] = amount

class aaaccount_with_calculated_balance:
    def __init__(self, initial_amount):
        self._deposits = initial_amount
        self._withdrawals = 0
    def deposit(self, amount):
        self._deposits += amount
    def withdraw(self, amount):
        self._withdrawals += amount

    def __getattr__(self, attribute):
        if attribute == 'balance':
            return self._deposits - self._withdrawals
        else: raise AttributeError(attribute)
    def __delattr__(self, attribute):
        if attribute == 'balance':
            self._deposits, self._withdrawals = 0, 0
        else: raise AttributeError(attribute)
