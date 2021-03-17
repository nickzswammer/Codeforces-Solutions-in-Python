number = (input())
 
seven = 0
four = 0
 
lucky = True
 
for i in number:
	if i == "7":
		seven += 1
 
	elif i == "4":
		four += 1
 
if seven+four == 7 or seven+four == 4:
	print("YES")
 
else:
	print("NO")