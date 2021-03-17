#Codeforces 231A NZ Swammer
while True:
    n = int(input())
    if n in range(1, 1001):
        break
 
 
total_solutions = 0
mini_solutions = 0
for i in range(n):
    solutions = input()
    for num in solutions:
        if num == "1":
            mini_solutions += 1
    if mini_solutions >=2:
        total_solutions += 1
    mini_solutions = 0
 
print(total_solutions)