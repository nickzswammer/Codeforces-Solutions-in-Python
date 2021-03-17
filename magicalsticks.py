t = int(input())
 
results = []
 
for i in range(t):
    desc = int(input())
 
    if desc % 2 == 0:
        results.append(int(desc/2))
    
    else:
        results.append(int((desc+1)/2))
 
for i in results:
    print(i)