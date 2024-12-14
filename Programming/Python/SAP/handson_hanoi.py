def hanoi(n):
    res = 0
    if n == 1:
        return 1
    else:
        res = 2*hanoi(n-1)+1
        return res


n = int(input('Enter number of disks: '))
print(hanoi(n))
