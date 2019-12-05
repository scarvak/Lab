# Take a variable.
# Put a day in it (Mon, Tue, Wed ... )
# Say if it is weekday or a weekend

myDay = "Sun"
"""
if myDay == "Mon" : 
    print ("Not a weekend")
else :
    if myDay == "Tue" :
        print("Not a weekend")
    else myDay == "Wed" :
        print("Not a weekend")
"""
if myDay == "Tue" :
    print("Not a weekend")

# myDay = input()
myDay = input("Enter the day")

if (myDay == "Mon") :
    print("Not a weekend")
elif (myDay == "Tue") :
    print("Not a weekend")
elif (myDay == "Wed") :
    print("Not a weekend")
elif (myDay == "Thu") :
    print("Not a weekend")
elif (myDay == "Fri") :
    print("Not a weekend")
elif (myDay == "Sat") :
    print("Weekend")
elif (myDay == "Sun") :
    print("Weekend")
else :
    print ("Did'nt recognize your entry")

if (myDay == "Sun" or myDay == "Sat") :
    print("Weekend")
else :
    print("Weekday")
