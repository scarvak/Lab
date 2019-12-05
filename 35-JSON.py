import json

j1 = '{ "id" : 1, "name" : "AA", "email" : "a@a.com" }'

print (type(j1))
print ((j1))

myData = json.loads(j1) # works for a set of JSON Data to be read from
print (type(myData))
print (myData)

print (myData["id"])
print (myData["name"])
print (myData["email"])

f1 = open("j1.json", "r")

myData2 = json.load(f1) # for reading out of a JSON file\
print (type(myData2))
print (myData2)


# Change and export to json string
myData["id"] = 3
# print (myData)

jString = json.dumps(myData)

print (jString)

f2 = open("j2.json", "r")
myData3 = json.load(f2)
print (myData3)

print ("Total are ", myData3["total"])
print ("Total pages are ", myData3["total_pages"])
print ("Print Data ", myData3["data"])
for item in myData3["data"] :
    print (item)

print ("1st First Name ", myData3["data"][0]["first_name"])
print ("2nd First Name ", myData3["data"][1]["first_name"])

myData3["data"][1]["first_name"] = "Lion"
f3 = json.dumps(myData3)
print (type(f3))
print (f3)
