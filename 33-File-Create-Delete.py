
# print (x)
fPath = "myNewFile.txt"
f1 = open(fPath, "x") # create if not exists

for i in range(10) :
    txt = "\n Line " + str(i)
    f1.write(txt)

f1 = open(fPath, "r") # write on to file
print(f1.read())

f1.close()

import os
os.remove(fPath)

if os.path.exists(fPath) :
    print ("File NOT deleted")
else :
    print("File  deleted")