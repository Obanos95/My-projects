s = [9,1,5,2,1,3]
size = len(s)
print(len(s))
if 2 in s:
    print('2 is present')
else:
    print('2 is not present')

if 4 in s:
    print('4 is present')
else:
    print('4 is not present')

print(s[0])
print(s[-1])

freq1 = 0
for i in s:
    if i == 1:
        freq1 += 1
print(freq1)

del s[2]
print(s)
s.remove(2)
print(s)
s.append(7)
print(s)
s.insert(1,6)
print(s)

x = 1
for i in range(len(s)):
    if s[i] == x:
        s.insert(i,0)
        break
print(s)

sumsq = 0
for i in s:
    sumsq += i**2
print(sumsq)
