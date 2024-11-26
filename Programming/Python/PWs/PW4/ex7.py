def freq(seq,char):
    '''
    Finding frequency of a character in a sequence

    : param seq: sequence in which we need to find frequency of a character
    : type seq: str, list
    : param char: character whose frequency we need to find
    : type char: str
    : return: frequency of a character
    '''
    frequency = 0
    for i in seq:
        if i == char:
            frequency += 1
    return frequency

def contain(seq,char):
    '''
    Find out if a character is in the sequence

    : param seq: sequence in which we need to find out if a character is present
    : type seq: sequence
    : param char: character which we need to find in the sequence
    : type char: str 
    : return: True if sequence contains the character, else False
    '''
    cont = False
    for i in seq:
        if i == char:
            cont = True
    return cont

def index(seq,char,start):
    '''
    Get the index of a character in the sequence

    : param seq: sequence in which we need to find index of a character
    : type seq: sequence
    : param char: character whose index we need to find
    : type char: str 
    : return: index of a character if it's present in the sequence, else None
    '''
    ind = None
    targind = start
    curind = 0
    for i in seq:
        if ind == None:
            if curind >= targind:
                if i == char:
                    ind = curind
        curind += 1
    return ind

#Test funcs

def test_frequency():
    # Tests
    assert freq('texts', 'e') == 1
    assert freq('texts', 'a') == 0
    assert freq('texts', 's') == 1
    assert freq('texts', 't') == 2
    # limit tests
    assert freq('ttt', 't') == 3
    assert freq('', 'x') == 0

    print('test_frequency: ok')

def test_contain():
    assert contain('l texts', 'e')
    assert contain('l texts', 'x')
    assert contain('l texts', 's')
    assert contain('l texts', 't')
    assert contain('l texts', 'l')
    assert not contain('l texts', 'a')
    assert not contain('l texts', '7')
    assert not contain('', 'x')

    print('test_contain: ok')

def test_index():
    # Tests nominaux
    assert index('texts', 'e', 0) == 1
    assert index('texts', 's', 0) == 4
    assert index('texts', 't', 0) == 0
    assert index('texts', 't', 1) == 3
    assert index('texts', 't', 3) == 3
    assert index('texts', 't', 4) == None

    # Tests aux limites
    assert index('ttt', 't', 0) == 0
    assert index('texts', 'a', 0) == None
    assert index('texts', 't', 40) == None
    assert index('', 'x', 0) == None

    print('test_index: ok')
test_frequency()
test_contain()
test_index()
