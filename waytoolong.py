#Codeforces 71A NZ Swammer
lines = int(input())
 
output = []
 
 
for i in range(lines):
    word = input()
    if len(word) >10:
        output.append(word[0]+str(len(word[1:-1])) + word[-1])
        
    else:
        output.append(word)
 
 
print('\n'.join(output))