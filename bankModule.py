
class myBank() :

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
=======
class myBank() :

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

