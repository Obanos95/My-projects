def powering(numb, power):
    '''
    Finding the power of a number 

    : param numb: the number to be raised to a power
    : type numb: int
    : param power: the power of the number
    : type power: int
    : return: number "numb" powered by "power"
    '''
    powerednum = 1
    for i in range(power):
        powerednum *= numb
    assert powerednum == pow(numb, power)
    return powerednum

numb = int(input('Enter number: '))
power = int(input('Enter power of the number: '))

print(powering(numb, power))
