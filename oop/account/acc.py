class Account:
#want to send filepath parameter from txt,we write self always in oop
    def __init__(self,filepath):
        # we do this so we could use it anywhere in class
        self.filepath=filepath 
        #file handling with with method, file is temporary variable
        with open(filepath,'r') as file:
            #save the value inside the text file
            self.balance=int(file.read())

    # lets add other methods
    def withdraw(self,amount):
         self.balance=self.balance - amount

    def deposit(self,amount):
        self.balance=self.balance + amount

    def commit(self):
        #need to update balance
        with open(self.filepath,'w') as file:
              file.write(str(self.balance))           
#print out object namespace,but didn't get object
#account=Account("balance.txt")
#print(account)
#so we have to point at object look at secind print
#print(account.balance)
#account.withdraw(100)
#print(account.balance)
#account.commit()

#inheritance make sub class

class Checking(Account):
    """THis class generates checking account objects"""

    type="checking"

    def __init__(self,filepath,fee):
        Account.__init__(self,filepath)
        self.fee=fee
    def transfer(self,amount):
        self.balance=self.balance - amount -self.fee

#object instances

jacks_checking=Checking("jack.txt",1)
jacks_checking.transfer(100)
print(jacks_checking.balance)
jacks_checking.commit()
print(jacks_checking.type)

johns_checking=Checking("john.txt",1)
johns_checking.transfer(100)
print(johns_checking.balance)
johns_checking.commit()
print(johns_checking.type)

print(johns_checking.__doc__)