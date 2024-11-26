'''The minimum functions and its test programs..'''
def minimum(elt1, elt2):
    '''
    Return the smaller of the two elements as s parameter.

    : param elt1: the first element.
    : type elt1: any
    : param elt 2: tha second element.
    : type elt2: any
    : returns: the smaller of the two elements.
    '''

    if elt1 < elt2:
        return elt1
    else:
        return elt2

def test_min():
    '''Tests the minimum of integers.'''
    assert 1 == minimum(1,2)
    assert -5 == minimum(elt2 = -3, elt1 = -5)

def test_min_chaines():
    '''TEst the minimum of two strings.'''
    assert 'cat' == minimum('cat', 'horse')

if __name__ == '__main__':
    test_min()
    test_min_chaines()
    print('seccessful tests')

