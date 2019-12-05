try :
    print ("Started TRY Block")

    # print (x) # Name Error
    # i = 10 / 0
    fPath = "myNewFile.txt"
    f1 = open(fPath, "x")  # create if not exists

    for i in range(10):
        txt = "\n Line " + str(i)
        f1.write(txt)

    f1 = open(fPath, "r")  # write on to file
    print(f1.read())

    # f1.close()

    import os

    os.remove(fPath)

    if os.path.exists(fPath):
        print("File NOT deleted")
    else:
        print("File  deleted")

except NameError :
    print ("A name error occurred")

except FileExistsError :
    print ("A file exists. You cannot create again with the same name")

except FileNotFoundError :
    print ("A file DOES NOT exist. Create one 1st")

except ZeroDivisionError :
    print("Cant divide by ZERO ")

except SyntaxError :
    print("Syntax error")

except PermissionError:
    print("Permission error")

except :
    print("Started Except Block")

    print("Ended Except Block")

finally :
    print ("At the end of all")

print ("Out of Try Except block")

