t = int(input())
 
results = []
 
for i in range(t):
    nk = list(map(int, input().split()))
    
    a = nk[0]
    b = nk[1]
    c = nk[2]
 
    n = nk[-1]
 
    greatest = [a, b, c]
    greatest.sort()
 
    num = (greatest[-1]- greatest[0]) + (greatest[-1] - greatest[1])
 
 
 
    if (n - num) % 3 == 0:
        if num > n:
            results.append("NO")
        else:
            results.append("YES")
 
    else:
        results.append("NO") 
 
for i in results:
    print(i)