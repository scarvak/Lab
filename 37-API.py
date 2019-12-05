import requests
print ("~~~~~~~~~~~~~~~~~~~~~~~~")
res1 = requests.get("https://google.com/")
print (res1)
print (" API Status ", res1.status_code)
print ("  Cookies ", res1.cookies)
print ("Headers ", res1.headers)


print ("~~~~~~~~~~~~~~~~~~~~~~~~")
res2 = requests.get("https://reqres.in/api/users?page=2")
print (res2)
print (" API Status ", res2.status_code)
print ("  Cookies ", res2.cookies)
print ("Headers ", res2.headers)


print ("~~~~~~~~~~~~~~~~~~~~~~~~")
res3 = requests.get("https://reqres.in/api/users/2")
print (res3)
print (" API Status ", res3.status_code)
print ("  Cookies ", res3.cookies)
print ("Headers ", res3.headers)

print ("~~~~~~~~~~~~~~~~~~~~~~~~")

myJSON2 = res2.json()
print (myJSON2)
print (type(myJSON2))

print ("~~~~~~~~~~~~~~~~~~~~~~~~")
myJSON3 = res3.json()
print (myJSON3)
print (type(myJSON3))





