#Codeforces NZ Swammer
 
tests = int(input())
 
answers = []
 
for i in range(tests):
    cards = 1
    dimensions = list(map(int, input().split()))
    w, h, n = dimensions[0], dimensions[1], dimensions[-1]
    yes = True
 
    while cards < n:
        if w % 2 != 0 and h % 2 != 0:
            answers.append("NO")
            yes = False
            break
        if w % 2 == 0:
            w = w/2
            cards *= 2
 
        elif h % 2 == 0:
            h = h/2
            cards *=2
 
    if yes == True:
        answers.append("YES")
 
for i in answers:
    print(i)