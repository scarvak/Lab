

# i = 10
"""
while i < 20 :
    print (i)
    i += 1
    if i == 18 :
        print ("Get out of here")
        break # coming out of it
"""

i = 1
while i < 20 :
    i += 1
    if i == 18 :
        # print ("do nothin")
        # break # coming out of it
        continue
    print(i)


print ("End of code")