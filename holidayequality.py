n = int(input())
 
balance = list(map(int, input().split()))
total = 0
 
balance.sort()
 
last = balance[-1]
 
for i in balance[:-1]:
    total += last-i
 
print(total)