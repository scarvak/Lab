
s1 = " Hi this is Python learning "
s2 = 10

print (s1)
print (s2)
print (s1, s2)

print (s1[10])

print ("Hi this is line 1\n" 
     "and line 2\n"
    "and line3")

s3 = s1.upper()

print (s3)
s3 = s3.strip()
print (s3)

lenS1 = len(s1)

print ("s1 length is " + str(lenS1))
print ("s1 length is " , lenS1)

# String, int, float, boolean

boo1 = True
boo2 = False

if boo1 :
    print ("ok boo1")
else :
    print("not k boo1")

print(s1.index("P"))

s4 = s1.replace("learning", "programming")
print(s4)
print(s1)

s4 = s1.upper()
if s4.isupper() :
    print("upper")
else :
    print ("not upper")