import json

j1 = '{ "id" : 1, "name" : "AA", "email" : "a@a.com" }'

print (type(j1))
print ((j1))

f1 = open("j2.json", "r")

myData2 = json.load(f1) # for reading out of a JSON file\
print (type(myData2))
print (myData2)