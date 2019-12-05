# storing sets of data

# devices

l1 = ["mac", "10.20.30.40", 1]
t1 = ("mac", "10.20.30.40", 1)

d1 = {
    "name" : "mac",
    "ip" : "10.20.30.40",
    "status" : 1
}

d2 = {
    "name" : "linux",
    "ip" : "10.20.30.41",
    "status" : 3
}

print (d1["name"])
print (d1["ip"])
print (d1["status"])

d1["status"] = 2
print (d1["status"])
print ("Len is " , len(d1))

d1["date"] ="12/2/2019"
d1.pop("status")
for i in d1 :
    print (i, d1[i])

for x, y in d1.items() :
    print (x, y)