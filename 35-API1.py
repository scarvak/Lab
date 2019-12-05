import json

# load() for reading from a file
with open("j1.json") as f :
    data = json.load(f)

# a = json.loads() # loads() for reading from local JSON data in your program

# print ("a is ", a)
print (data)
print (data["n"])
print (data['Age'])

with open("j2.json") as f :
    data = json.load(f)

print (data)
print (data["page"])
print (data['data'])
print (data["data"][0]["id"])
print (data["data"][1])

import requests
res1 = requests.get("https://google.com/")
print (res1)
print (" API Status ", res1.status_code)

res2 = requests.get("https://reqres.in/api/users/2")
print (res2)
print ((res2.json()))
print (" API Status ", res1.status_code)

res3= requests.get("https://reqres.in/api/users/24")
print (res3)
print ((res3.json()))

if res3.status_code == 200 :
    print (" 200 API Status ")
elif res3.status_code == 404 :
    print (" 404 API Status ")

