t = int(input())
 
result = []
 
for i in range(t):
    arr = []
    n = int(input())
    mid = n//2
    for i in range(1, n+1):
        arr.append(2**i)
 
    a = arr[-1]+sum(arr[:mid-1])
 
    b = sum(arr[mid-1:-1])
 
    if n == 2:
        result.append(2)
 
    else:
        result.append(abs(b-a))
 
for i in result:
    print(i)