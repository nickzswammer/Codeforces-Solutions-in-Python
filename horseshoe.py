import sys
n = list(map(int, input().split()))
total = 0
seen = []
 
for i in n:
    if i in seen:
        seen.append(i)
        total +=1
    elif i not in seen:
        seen.append(i)    
 
print(total)