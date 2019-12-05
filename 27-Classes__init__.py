class myCars :

    def __init__(self, cMake, cModel, cYear) :
        self.make = cMake
        self.model = cModel
        self.year= cYear

    def whatIsMyCarYear(self):
        return self.year


c1 = myCars("Honda","MDX", "2000")
c2 = myCars("BMW","M5", "2010")
c3 = myCars("Sportster","1", "2022")

print (c1.whatIsMyCarYear())
print (c2.whatIsMyCarYear())
print (c3.whatIsMyCarYear())