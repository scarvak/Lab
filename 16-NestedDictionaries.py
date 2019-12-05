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

d = {
    "d1": {
        "name": "mac",
        "ip": "10.20.30.40",
        "status": 1
    },
    "d2" : {
        "name": "linux",
        "ip": "10.20.30.41",
        "status": 3
    },
    "d3": {
        "name": "win",
        "ip": "10.20.30.42",
        "status": 5
    }
}

print (d)
print(d["d2"])
print(d["d1"]["name"])

d["allDevices"] = {
    "1" : "d1",
    "2" : "d2",
    "3" : "d3",
    "4" : "not present"
}
print (d["allDevices"])
print (d)
