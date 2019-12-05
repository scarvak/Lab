myFile = open("C:\\Users\\jcady\\PycharmProjects\\Proj1\\jusText.txt")

print (myFile.read())

print (myFile.read(5))
print (myFile.read(10))
print (myFile.read(15))

myFile.close()

myFile = open("C:\\Users\\jcady\\PycharmProjects\\Proj1\\jusText.txt")

print(myFile.readline())
print(myFile.readline())
print(myFile.readline())


for myText in myFile :
    print ("\n".join(myText))
