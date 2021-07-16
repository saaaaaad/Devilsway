import random

file = open("vendor")
lines = file.readlines()
macs = []

for line in lines:
    first = line[0:9]
    vmac = first.split()
    mac = ""
    for i in vmac:
        mac += i + ":"

    macs.append(mac)

mac=""
for i in range(0,2):
    no1=random.randint(0,len(macs))
    mac = mac+macs[no1]
l = len(mac)-1
mac = mac[0:l]
print(mac)


