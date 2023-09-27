
class Account():



    def __init__ (self, accountNo, name, password, balance = 0, interest_rate = 1):

        self.account_no = accountNo

        self.name = name

        self.password = password

        self.balance = balance

        self.interest_rate = interest_rate


    

    def deposit(self):

        

        amount = int(input("Enter the amount to be deposited: "))

        if(amount<=0):

            return "Invalid Amount"
        


        self.balance += amount

        return f"Amount {amount} successfully deposited\nBalance: {self.balance}"


    def withdraw(self):


        amount = int(input("Enter the amount to be withdrawn: "))

        if(amount<=0):

            return "Invalid amount"


        elif(amount> self.balance):

            return "Insufficient balance"


        pass_word = str(input("Enter the password: "))


        if(pass_word != self.password):

            return "Wrong password"   

        self.balance -= amount

        return f'Amount {amount} successfully withdrawn \nBalance: {self.balance}'

    def credit_interest(self):

       
        self.balance += ((self.balance * self.interest_rate)/1200)

        return f' Interest is credited to your account. \nBalance: {self.balance}'


    def info(self):

        return f'Account No: {self.account_no} \nName: {self.name} \nBalance: {self.balance}'




def test_bank_account ():
      b = Account("Indhu",312320456652,"2002")
      print(b.deposit())
      print(b.withdraw())
      print(b.info())
      print(b.credit_interest())
      print(b.info())
    
test_bank_account()


   



   

