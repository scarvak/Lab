# print all status code for 100 users
import requests
import json

bURL = "https://reqres.in/api/users/"
uURL = []

for uID in range(0, 100) :
    uURL.append(bURL + str(uID))

for eachURL in uURL :
    print ("Status for ", eachURL, " is - ", requests.get(eachURL).status_code)

