nm = list(map(int, input().split()))
 
n = nm[0]
m = nm[-1]
colored = 0
wb = 0
result = []
 
for i in range(n):
    colors = input()
    result.append(colors)
 
for f in result:
    for i in f:
        if i == "W" or i == "B" or i == "G":
            wb +=1
        
        elif i != "W" and i != "B" and i != "G" and i != ' ':
            colored +=1 
 
if colored > 0:
    print("#Color")
 
else:
    print("#Black&White")