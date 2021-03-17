t = int(input())
 
results = []
 
for i in range(t):
    nk = list(map(int, input().split()))
    a = nk[0]
    b = nk[-1]
 
    if a > b:
        if a % 2 == 0:
            if b % 2 == 0:
                results.append(1)
            else:
                results.append(2)
 
        else:
            if b % 2 == 0:
                results.append(2)
            else:
                results.append(1)
    
    elif a < b:
        if a % 2 == 0:
            if b % 2 == 0:
                results.append(2)
            else:
                results.append(1)
        
        else:
            if b % 2 == 0:
                results.append(1)
            else:
                results.append(2)
 
    else:
        results.append(0)
 
for i in results:
    print(i)