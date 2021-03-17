year = int(input())
year += 1
biggerr = [int(x) for x in str(year)]
 
def all_unique(lst):
  return len(lst) == len(set(lst))
 
while True:
    biggerr = [int(x) for x in str(year)]
 
    if all_unique(biggerr):
        print(year)
        break
    else:
        
        year += 1
 