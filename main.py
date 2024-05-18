# Scenario
# - Implement a class representing an account exception,
# - Implement a class representing a single bank account,
# - This class should control access to the account number and account balance attributes by implementing the properties:
# - it should be possible to read the account number only, not change it. In case someone tries to change the account number, raise an alarm by raising an exception;
# - it should not be possible to set a negative balance. In case someone tries to set a negative balance, raise an alarm by raising an exception;
# - when the bank operation (deposit or withdrawal) is above 100.000, then additional message should be printed on the standard output (screen) for auditing purposes;
# - it should not be possible to delete an account as long as the balance is not zero;
# 
# - test your class behavior by:
#       - setting the balance to 1000;
#       - trying to set the balance to -200;
#       - trying to set a new value for the account number;
#       - trying to deposit 1.000.000;
#       - trying to delete the account attribute containing a non-zero balance.

############################################################################################################

class accountException(Exception):
    pass

import random
class bankAccount():
    def __init__(self):
        self.__number = "B123-BANK-"+"".join(random.choices("123456789",k=22))
        self.__bal = 0
    @property
    def accNumber(self):
        return self.__number
        
    @accNumber.getter
    def accNumber(self):
        return self.__number
    @accNumber.setter
    def accNumber(self,val):
        raise accountException("You can't modify your bank account number")
        
        
    @property    
    def accBal(self):
        return self.__bal
    
    @accBal.getter
    def accBal(self):
        return self.__bal
        
    @accBal.setter
    def accBal(self,amount):
        if amount <0: raise accountException("You can't have a negative value") 
        elif amount >100000: print( "Your bank account is above $100 000, An audition is required")
        self.__bal = amount
    
    @accBal.deleter
    def accBal(self):
        if self.__bal: raise accountException("Your account have balance, it can't be deleted")
        print(f"Bank account {self.accNumber} deleted")
        del self
        
    def deposit(self,amount):
        if amount<0: raise accountException("You can't deposit a negative amount")
        self.accBal += amount
    
    def withdrawal(self,amount):
        if amount<0: raise accountException("You can't withdraw a negative amount")
        self.accBal += amount
acc = bankAccount()

acc.accBal = 1000
print(f"Account Balance: {acc.accBal}")

try:
    acc.accBal = -200
except accountException as e:
    print(f"Account Exception: {e}")
print(f"Account Balance: {acc.accBal}")

try:
    acc.accNumber = "B123-BANK-6249168728167214597578"
except accountException as e:
    print(f"Account Exception: {e}")
print(f"Account Number: {acc.accNumber}")

acc.deposit(1000000)
print(f"Account Balance: {acc.accBal}")

try:
    del acc.accBal
except accountException as e:
    print(f"Account exception: {e}")