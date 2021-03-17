t = int(input())
 
results = []
 
for i in range(t):
    sides = int(input())
 
    if sides >= 4:
        if sides % 4 == 0:
            results.append("YES")
        
        else:
            results.append("NO")
 
    else:
        results.append("NO")
 
for i in results:
    print(i)