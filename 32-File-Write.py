f3 = open("jusText.txt", "w")
f3.write("I just deleted it all with this")
f3.close()

lines = ['line1', 'line2']
with open('jusText.txt', 'a') as f:
    f.write("\n")
    f.write('\n'.join(lines))

lines = ['line3', 'line4']

# f4 = open('fileeee.txt', 'r')
# print (f4.read())

with open('rfefsdfsdf.txt', 'a') as f:
    f.write("\n")
    f.writelines("%s\n" % l for l in lines)


f3 = open("jusText.txt", "r")
print (f3.read())