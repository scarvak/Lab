
# f1 = open("C:\\Users\\jcady\\PycharmProjects\\Proj1\\jusText.txt", "r")

# print (f1.read())
# print (f1.readline())
# print (f1.readline())
# print (f1.read())

f2 = open("jusText.txt", "a") # append to the end of the file
f2.write("\nthis is just write\n")
f2.write("this is another write\n")
f2.writelines(["hi there how are you1",
            "hi there how are you2",
            "hi there how are you3"])

f2.close()

f2 = open("C:\\Users\\jcady\\PycharmProjects\\Proj1\\jusText.txt", "r")
print (f2.read())