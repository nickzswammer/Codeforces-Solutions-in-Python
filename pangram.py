n = int(input())
 
word = input().lower()
 
word = ''.join(sorted(word))
 
word = sorted(list(set(word)))
word = ''.join(sorted(word))
 
 
 
alpha = "abcdefghijklmnopqrstuvwxyz"
 
 
if word == alpha:
    print("YES")
 
else:
    print("NO")