# take input(s) from user - number and limit
# display multiplication table

myNum = int(input("Enter the number: "))
myLimit = int(input("Enter the Limit: "))

for i in range(myLimit) :
    print (myNum, " * ", i+1, " is : ", myNum * (i+1))


