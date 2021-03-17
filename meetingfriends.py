nums = list(map(int, input().split()))
nums.sort()
total = 0
 
total = abs(nums[1]-nums[0])
 
total = total + nums[-1]-nums[1]
 
 
print(total)