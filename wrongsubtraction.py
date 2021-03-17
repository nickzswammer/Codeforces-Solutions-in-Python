numbers = input().split()
 
n = int(numbers[0])
k = int(numbers[-1])
 
 
for i in range(1, k+1):
    if n % 10 == 0:
        n = n/10
    
    else:
        n -= 1
 
print(int(n))