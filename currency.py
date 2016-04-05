from currency_converter import *



conversation_rates {
    'USD': 1,
    'EUR': .87,
    'JPN', 1.2
}


currency_symbols {
    '$': 'USD'
    '€': 'EUR'
    '¥', 'YEN'
}


class Currency:

    def __init__(self, currency_code, amount = 0):
        self.currency_code = currency_code
        self.amount = amount


    def __eq__(self, other):
        return self.amount == other.amount and self.currency_code == other.currency_code:


    def __str__(self):
        return str(self.amount) + ' ' + (self.currency_code)


    def __add__(self, other):
        if self.currency_code == other.currency_code:
            return Currency(self.amount + other.amount, self.currency_code)


    def __sub__(self, other):
        if self.currency_code == other.currency_code:
            return Currency(self.amount - other.amount, self.currency_code)


    def __sub__(self, other):
        if self.currency_code == other.currency_code:
            return Currency(self.amount - other.amount, self.currency_code)


    def symbol_converter(self, currency_code):
        if not self.currency_code.isalnum():
             self.amount = self.currency_code.strip('0-9')
            currency_code = ''.join(i for i in currency_code if i.isnum() or i  == '.')



class DifferentCurrencyCodeError(Exception):
    pass



        raise DifferentCurrencyCodeError


    def __mul__(self, other):
        #Must be able to be multiplied by an int or float and return a Currency object.





Currency() must be able to take one argument with a currency symbol embedded in it, like "$1.20" or "€ 7.00", and
figure out the correct currency code. It can also take two arguments, one being the amount and the other being
 the currency code.

    def __lt__(self, other):
            return self.amount + other.amount and self.currency_code == other.currency_code

    def __gt__(self, other):
            return self.amount + other.amount and self.currency_code == other.currency_code

    def __le__(self, other):
            return self.amount + other.amount and self.currency_code == other.currency_code

    def __ge__(self, other):
            return self.amount + other.amount and self.currency_code == other.currency_code


    def __str__(self):
        return str(self.amount) + ' ' + self.currency.code
        #return 'Currency(Amount={}, currency_code=\'{}')'.format(self.amount, self.currency_code)


Must NOT equal another Currency object with different amount or currency code.
Must be able to be added to another Currency object with the same currency code.
Must be able to be subtracted by another Currency object with the same currency code.
Must raise a DifferentCurrencyCodeError when you try to add or subtract two Currency objects with different currency codes.
Must be able to be multiplied by an int or float and return a Currency object.
Currency() must be able to take one argument with a currency symbol embedded in it, like "$1.20" or "€ 7.00", and figure
out the correct currency code. It can also take two arguments, one being the amount and the other being the currency code.
