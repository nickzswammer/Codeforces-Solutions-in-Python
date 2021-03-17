answers = []
 
n = int(input())
cards = list(map(int, input().split()))
 
sereja = 0
dima = 0
 
turn = ''
 
length = n
 
while length > 0:
 
    first = cards[0]
    last = cards[-1]
 
    if turn == '' or turn == 'sereja':
        turn = 'dima'
        if first > last:
            sereja += first
            cards.remove(first)
            length -=1
        else:
            sereja += last
            cards.remove(last)
            length -=1
            
    else:
        turn = 'sereja'
        if first > last:
            dima += first
            cards.remove(first)
            length -=1
        else:
            dima += last
            cards.remove(last)
            length -=1
        
answers.append([str(sereja), str(dima)])
 
for i in answers:
    print(' '.join(i))