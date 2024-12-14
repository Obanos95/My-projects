def fact(n):
    res = 1
    if n == 1:
        return 1
    else:
        res = n*fact(n-1)
        return res

n = int(input('Enter num: '))
print(fact(n))
