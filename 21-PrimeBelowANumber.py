
def allPrimeLessThan(y) :
    for i in range (2, y) :
        isItPrime(i)

def isItPrime(x) :
    flag = 1

    for i in range(2, x // 2):
        if ((x % i) == 0):
           # print("NOT PRIME :: ", x)
            flag = 0
            return "PRIME"
            break

    if ((flag == 1) and x != 4):
        print("Prime Number :::::: ", x)
        return "Not PRIME"

allPrimeLessThan(1000)