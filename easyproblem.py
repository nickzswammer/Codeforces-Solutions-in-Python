n = int(input())
 
responses = input().split()
count = 0
 
for i in responses:
    if i == "1":
        print("HARD")
        break
    else:
        count +=1
 
if count == len(responses):
    print("EASY")