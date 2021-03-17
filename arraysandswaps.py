t = int(input())
 
result = []
 
for i in range(t):
    nk = list(map(int, input().split()))
    n = nk[0]
    k = nk[-1]
 
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())), reverse=True)
 
    for i in range(k):
        c = a[i]
        if a[i] < b[i]:
            a[i] = b[i]
            b[i] = c
 
    result.append(sum(a))
 
 
for i in result:
    print(i)