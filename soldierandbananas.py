bananas = input().split()
 
k = int(bananas[0])
n = int(bananas[1])
w = int(bananas[-1])
 
total = 0
 
for i in range(1, w+1):
    
    total = total + (i*k)
 
if total <= n:
    print(0)
 
else:
    print(total-n)