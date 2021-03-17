n = int(input())
 
result = []
m = 0
c = 0
 
for i in range(n):
    dice = list(map(int, input().split()))
    result.append(dice)
 
 
for i in range(n):
    if result[i][0] > result[i][-1]:
        m +=1
    
    elif result[i][-1] > result[i][0]:
        c +=1
 
if m > c:
    print("Mishka")
 
elif c > m:
    print("Chris")
 
else:
    print('Friendship is magic!^^')