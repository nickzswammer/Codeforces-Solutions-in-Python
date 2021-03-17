n = int(input())
tetrahedron = 4
cube = 6
octahedron = 8
dodecahedron = 12
icosahedron = 20
 
total = 0
 
for i in range(n):
    sides = input().lower()
    if sides == "tetrahedron":
        total += tetrahedron
    
    elif sides == "cube":
        total += cube
    
    elif sides == "octahedron":
        total += octahedron
    
    elif sides == "dodecahedron":
        total += dodecahedron
 
    elif sides == "icosahedron":
        total += icosahedron
 
print(total)