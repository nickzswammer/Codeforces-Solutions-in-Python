n = int(input())
 
result = []
 
for i in range(n):
    length = int(input())
    arr = []
    
    mid = length//2
 
    if length/2 % 2 == 0:
        result.append("YES")
        for i in range(1,length+1):
            if i % 2 == 0:
                arr.append(i)
        
        for i in range(length):
            if i % 2 == 0:
                pass
            else:
                arr.append(i)
        
        sum_even = sum(arr[:mid])
        sum_odd = sum(arr[mid:])
 
        arr[-1] = arr[-1]+(sum_even-sum_odd)
        string_ints = [str(i) for i in arr]
 
        result.append(string_ints)
    else:
        result.append("NO")
 
for i in result:
    if type(i) == list:
        print(' '.join(i))
    else:
        print(i)