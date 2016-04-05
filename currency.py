from currency_converter import *

class Currency:
    def __init__(self, currency_code, amount):
        self.currency_code = currency_code
        self.amount = amount


    def __str__(self):
        return str(self.amount) + ' ' + se.currency.code
        #return 'Currency(Amount={}, currency_code=\'{}')'.format(self.amount, self.currency_code)


    def __eq__(self, other):
        if self.amount == other.amount and self.currency_code == other.currency_code:
            return True
        else:
            return False

        #if self.amount == other.amount:
            # if self.amount == other.amount:
            #     return True
            #
            # else:
            #   return False
    # else:
    #     return False

    # def __ne__(self, other):
    #      return self.amount == other.amount and self.currency_code == other.currency_code


    def __add__(self, other):
            return self.amount + other.amount and self.currency_code == other.currency_code


    def __sub__(self, other):
        return self.amount - other.amount

    def """Must raise a DifferentCurrencyCodeError when you try to add or subtract two
        Currency objects with different currency codes."""

        class DifferentCurrencyCodeError(Exception)

        raise DifferentCurrencyCodeError:


    def Must be able to be multiplied by an int or float and return a Currency object.



    Currency() must be able to take one argument with a currency symbol embedded in it, like "$1.20" or "€ 7.00", and figure out the correct
    currency code. It can also take two arguments, one being the amount and the other being the currency code.



Must NOT equal another Currency object with different amount or currency code.
Must be able to be added to another Currency object with the same currency code.
Must be able to be subtracted by another Currency object with the same currency code.
Must raise a DifferentCurrencyCodeError when you try to add or subtract two Currency objects with different currency codes.
Must be able to be multiplied by an int or float and return a Currency object.
Currency() must be able to take one argument with a currency symbol embedded in it, like "$1.20" or "€ 7.00", and figure
out the correct currency code. It can also take two arguments, one being the amount and the other being the currency code.
    #five.dollars.amount = int(input())
    # def __add__(self, value):
    # return '{} plus {}'.format(self.value, value)

    # def __eq__(self):


    # def __eq__(self, other):
    #     return self.value == other.value
    #     Must equal another Currency object with the same amount and currency code.
