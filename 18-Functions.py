def printMyLines () :
    print("!" * 50)
    print("Yoyo")
    print("!" * 50)

def printCustomLines (msgText) :
    print("!" * 50)
    print(msgText)
    print("!" * 50)

def getMeSomething (msg1):
    return msg1 + msg1 + msg1

for i in range(10) :
    printMyLines()

printCustomLines("My Custom Text")
print (getMeSomething("twice "))

def getMeSomething (msg1, msg2):
    return msg1 + msg2 + msg1 + msg2

print (getMeSomething("twice ", "again"))