n = int(input())
events = list(map(int, input().split()))
 
available = 0
crimes = 0
total_crimes = 0
 
for i in events:
    if i < 0:
        if available >= 1:
            available -= 1
 
        elif available == 0:
            total_crimes +=1
        
    else:
        available +=i
        
 
print(total_crimes)