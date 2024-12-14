'''
dem_tuple = (1,2,4j,'hello')
dem_sets = {1,2,3,4,5,5,6,7}
print(dem_sets)
dem_sets.add('hey')
print(dem_sets)
dem_sets.update("12","Salam alekum")
print(dem_sets)
r = dem_sets.copy()
print(r)
r.clear()
print(r)
'''
'''
A, B, C = {2}, {3}, {5}
for i in range(2,101):
    if i%2 == 0:
        A.add(i)
    if i%3 == 0:
        B.add(i)
    if i%5 == 0 or i%7 == 0:
        C.add(i)

print(A & B)
print(A | C)
print(B - C)
print(A ^ B)
print(A | B | C)
'''

s = {1,2,3,4,5,6}.union({3,4,5,6,6,7,8,9})
print(s)
