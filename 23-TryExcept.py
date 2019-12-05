
print("This is the start")

try :
    print ("Start try")
    myFile = open("C:\\Users\\jcady\\PycharmProjects\\Proj1\\jusText.txt")
    print (myFile.read())
    print ("End Try")
except :
    print("Start Except")
    print("Exception/Error occurred")
    myFile = open("C:\\Users\\jcady\\PycharmProjects\\Proj1\\jusText.txt")
    print (myFile.read())
    print ("Reopened")
    print("End Except")

print("This is the end")