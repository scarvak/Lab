# Take uName, Pwd
# Verify with expected
# try upto 3 times

uName = "kk"
uPswd = "1234%"

myTrys = 3

while myTrys > 0 :
    e1 = input("User name? ")
    e2 = input("User pswd? ")
    if myTrys <=0:
        print("trys exceeded")
        break

    if (uName == e1 and uPswd == e2) :
        print ("Logged in")
        break
    else :
        print("Incorrect - Try Again")
    myTrys -= 1

# if myTrys <= 0 :
#   print("Exceeded number of tries")
