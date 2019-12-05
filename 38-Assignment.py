import requests
import json

# 1. GET list of user emails and print from https://reqres.in/api/users?page=2
# 2. Update List of emails to an external JSON File
# 3. Try POST, PUT, PATCH, DELETE as well

r1 = requests.get("https://reqres.in/api/users?page=2")
if (r1.status_code == 200) :
    d1 = r1.json()['data'] # all Data
    e1 = [emails['email'] for emails in d1] # all Emails

    f1 = open("jData.json", "w")
    f2 = open("jEmail.json", "w")

    json.dump(d1, f1)
    json.dump(e1, f2)
    f1.close()
    f2.close()

    f3 = open("jData.json", "r")
    myData3 = json.load(f3)
    print(myData3)
    print(type(myData3))

else :
    print ("Could'nt connect : Status code ", r1.status_code)

data = requests.get("https://reqres.in/api/users?page=2").json()['data']
emailAddresses = [item['id'] for item in data]

print("\n".join(str(i) for i in data))
print ("\n".join(str(i) for i in emailAddresses))
