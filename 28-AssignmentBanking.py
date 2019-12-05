# Have a bank .

# have 3 customers (CIN, Name, Balance)

# do some deposits, withdrawal (check for info)

class myBank() :

    myBankName = ""
    myBankLoc = ""
    def __init__(self, vCIN, vName, vBalance):
        self.CIN = vCIN
        self.Name = vName
        self.Balance = vBalance

    def makeDeposit(self, amount):
        self.Balance += amount
        print ("Balance for user ", self.Name, " with CIN ", self.CIN, " is :: ", self.Balance)

    def makeWithdrawal(self, amount):
        self.Balance -= amount
        print ("Balance for user ", self.Name, " with CIN ", self.CIN, " is :: ", self.Balance)

    def getBalance(self):
        vBalance = "Balance for user ", self.Name, " with CIN ", self.CIN, " is :: ", self.Balance
        return vBalance

p1 = myBank("101", "KK", 250000)
p1.makeDeposit(10000)
print (p1.getBalance())
p1.makeWithdrawal(25000)
print (p1.getBalance())