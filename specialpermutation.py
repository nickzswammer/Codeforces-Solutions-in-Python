 
t = int(input())
 
answers = []
 
for i in range(t):
    n = int(input())
 
    array = list(range(1, n+1))
    
    for i in range(n):
        array[i] = str(array[i])
 
    first = array[0]
    array.pop(0)
 
    array.append(first)
 
    answers.append(array)
        
 
for i in answers:
    print(' '.join(i))