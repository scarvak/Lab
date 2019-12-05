class myCar :
    cMake = " "
    cModel = " "
    cYear = " "

    def driveCar(self, vCar) :
        print ("~~~~~~~~~~~ I am driving ~~~~~~~~~~~~ ", vCar)

    def parkCar(self) :
        print ("~~~~~~~~~~~ I am parked ~~~~~~~~~~~~ ")

    def sellCar(self) :
        print ("~~~~~~~~~~~ I am selling ~~~~~~~~~~~~ ")

c1 = myCar()
c1.cMake = "Acura"
c1.driveCar(c1.cMake)
c1.parkCar()
print ("~~~~~~~~~~~~~~~~~~~~")
c2 = myCar()
c2.cMake = "Aston"
c2.driveCar(c2.cMake)
c2.parkCar()
c2.sellCar()