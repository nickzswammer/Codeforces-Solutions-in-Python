nk = list(map(int, input().split()))
 
problems = nk[0]
minutes = nk[-1]
 
time_allowed = 240-minutes
count = 0
time = 0
 
total = 0
 
for i in range(problems):
	if total > time_allowed:
		break
	
	time +=5
	total += time
	if total > time_allowed:
		break
	count +=1
	
	
 
 
print(count)