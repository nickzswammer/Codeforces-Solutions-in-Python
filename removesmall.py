n = int(input())
 
results = []
 
for i in range(n):
    t = int(input())
    array = list(map(int, input().split()))
    array.sort()
    new = sorted(array)
    for i in range(len(new)-1):
        if len(new) == 1:
            break
 
        
 
        if array[i+1] - array[i] <= 1:
            new.remove(min(array[i+1], array[i]))
 
    if len(new) == 1:
        results.append("YES")
    
    else:
        results.append("NO")
 
 
for i in results:
    print(i)
        