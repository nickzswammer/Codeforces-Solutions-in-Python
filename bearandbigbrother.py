weights = input().split()
 
 
 
limak = int(weights[0])
bob = int(weights[-1])
 
years = 0
 
 
 
while True:
    if limak > bob:
        print(years)
        break   
    else:
        limak = limak * 3
        bob = bob * 2
        years += 1