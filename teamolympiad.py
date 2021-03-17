n = int(input())
 
students = list(map(int, input().split()))
 
num1 = students.count(1)
num2 = students.count(2)
num3 = students.count(3)
 
count = 0
 
nums = [num1, num2, num3]
nums.sort()
 
result = []
result.append(nums[0])
 
ones = []
twos = []
threes = []
 
for i in range(n):
    if students[i] == 1:
        ones.append(i+1)
    
    elif students[i] == 2:
        twos.append(i+1)
    elif students[i] == 3:
        threes.append(i+1)
    
    
while count < nums[0]:
    res = []
    res.append(ones[count])
    res.append(twos[count])
    res.append(threes[count])
 
    result.append(res)
    count +=1
 
for i in result:
    if type(i) == list:
        strings = list(map(str, i))
        print(' '.join(strings))
  
    else:
        print(i)