# print a tree that looks like

"""
            .
           ...
          .....
         .......
        .........
            .
            .
            .
            .
"""

lenOfTree = int(input("Enter Length"))
widthOfTree = int(input("Enter Width"))

"""
i = 1 # counter for number of * to print

# top of tree
for x in range(int(lenOfTree/2)) :
    # we are going 1 line at a time
    aLineText = ""
    for y in range(int(widthOfTree/2 - i/2) + 1 ) :
        aLineText = aLineText + " "
    for z in range(i):
        aLineText = aLineText + "*"
    print (aLineText)
    i = i + 2

# bottom of tree
for a in range(int(lenOfTree/2)) :
    aLineText = ""
    for y in range(int(widthOfTree/2)) :
        aLineText = aLineText + " "
    for z in range(3):
        aLineText = aLineText + "*"
    print(aLineText)

"""

for i in range (lenOfTree) :
    print (" " * (lenOfTree- i - 1) + "*"*(2*i+1))
for j in range(4):
    print(" " * (lenOfTree//2-1) + "**")
