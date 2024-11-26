def divs_func(i): #I wrote this function so that it's easier for me to find the divisors of a number and find their sum
    '''
    Finding divisors of a natural number
    
    : param i: number to find its divisors
    : type i: int
    : returns: list of the number's divisors
    '''
    divs = []
    for j in range(1,(i//2)+1):
        if i%j == 0:
            divs.append(j)
    return divs

def perf_nums(n):
    '''
    Finding perfect numbers

    : param n: MAX number
    : type n: int
    : returns: list of perfect numbers
    '''
    perfnumslist = []
    for i in range(2,n+1):
        if sum(divs_func(i)) == i:
            perfnumslist.append(i)
    return perfnumslist

def friendly_nums(n):
    '''
    Finding numbers-friends

    : param n: MAX number
    : type n: int
    : returns: list of "friends"
    '''
    all_friends = []
    for i in range(2,n+1):
        for j in range(i+1,n+1):
            if sum(divs_func(i)) == j and sum(divs_func(j)) == i:
                all_friends.append([i,j])
    return all_friends

maxnum = int(input('Enter MAX: '))
print(perf_nums(maxnum),'are perfect numbers.')
print(friendly_nums(maxnum),'are pairs of friends.')
