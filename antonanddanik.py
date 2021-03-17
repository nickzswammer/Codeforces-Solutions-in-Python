games = int(input())
 
results = input()
 
Danik = 0
Anton = 0
 
 
for i in results:
    if i == "D":
        Danik += 1
    
    else:
        Anton += 1
 
 
if Danik > Anton:
    print("Danik")
 
elif Anton > Danik:
    print("Anton")
 
else:
    print("Friendship")