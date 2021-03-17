import math
import sys
socks = list(map(int, input().split()))
 
counts = []
count = 0
 
while socks[0] >= 1 and socks[-1] >= 1:
    socks[0] -=1
    socks[-1] -=1
    count +=1
 
counts.append(count)
 
for i in socks:
    if i != 0:
        counts.append(math.floor(i/2))
        for i in counts:
            print(i, end=' ')
        sys.exit()
 
for i in range(len(socks)):   
    if socks[i] == 0:
        if i == 0:
            if socks[-1] % 2 == 0:
                counts.append(int(socks[-1]/2))
                break
 
            else:
                counts.append(0)
                break
        elif i == 1:
            if socks[-1] % 2 == 0:
                counts.append(int(socks[0]/2))
                break
           
            else:
                counts.append(0)
                break
 
 
for i in counts:
    print(i, end=' ')