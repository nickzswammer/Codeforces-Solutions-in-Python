import sys
n = list(input())
 
suit = n[0]
rank = n[-1]
 
cards = list(input())
 
 
for f in cards:
    if f[0] == suit:
        print("YES")
        sys.exit()
 
    elif f[-1] == rank:
        print("YES")
        sys.exit()
 
 
 
print("NO")