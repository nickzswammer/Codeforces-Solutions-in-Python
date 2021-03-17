seq= input()
a= seq.split()
n=int(a[0])
m=int(a[1])
 
for i in list(range(n+1)[1:]):
    if i % 2 != 0:
        print(m*"#")
    
    elif i/2 % 2 != 0:
        print((m-1)*"." + "#")
    
    else:
        print("#" + (m-1)*".")
 
 