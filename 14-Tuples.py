# Tuples are unmutablle
t1 = (1, 2, 3, 10.23, "254", 3, 2)
t2 = [111]
# t2.append(10)
i = 0
t2 = list(t1)
print (t2)
print (t1)
"""
for t in t1 :
    print (t)
    t2 = t2.insert(i, t)
    # t2[i] = t
    i += 1

t1[1] = 4
print (t2)
"""