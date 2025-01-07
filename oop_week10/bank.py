class Bank:
    def __init__(self, id, name, balance):
        self.id = id
        self.name = name
        self.__balance = balance
    def deposit(self,amount):
        if amount >= 100:
            self.__balance += amount
        else :
            print('ยอดเงินไม่ถูกต้อง')

    def withdraw(self, amount):
        if amount >= 100 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print('ยอดเงินไม่ถูกต้อง')
            
    def showbalance(self):
        print(self.__balance)
        return self.__balance
    
id1 = Bank(1,"meen",2500)
id1.deposit(1000)
print(f"คุณ {id1.name} มีเงิน = {id1.showbalance()}")



