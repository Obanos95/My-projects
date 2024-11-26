ex_set = {1,2,3,2} # initialize a number variable with the set which contains 1, 2, 3 and 2.

def set_size(ex_set): 
    '''
    A function to find lenght of a set

    Params:
        ex_set: the set whose lenght we need to find
    
    Return: lenght of the set
    '''
    return len(ex_set)

def checkIf2IsPresent(ex_set): 
    '''
    A function that checks if number 2 is present

    Params:
        ex_set: the set in which we need to find if number 2 is present
    
    Return: True if number 2 is present in the list, False if not
    '''
    assert 2 in ex_set
    if 2 in ex_set: 
        return True
    else:
        return False

def checkIf5IsPresent(ex_set): 
    '''
    A function that checks if number 5 is present

    Params:
        ex_set: the set in which we need to find if number 5 is present
    
    Return: True if number 5 is present in the list, False if not
    '''
    assert (5 in ex_set) == False
    if 5 in ex_set: 
        return True
    else:
        return False

def add11(ex_set):
    '''
    A function that adds 11 to the set

    Params:
        ex_set: the set in which we need to add number 11

    Retunrs: updated set with number 11 in it
    '''
    ex_set.add(11)
    assert ex_set == {1,2,3,11}
    return ex_set

def add2(ex_set):
    '''
    A function that adds 2 to the set

    Params:
        ex_set: the set in which we need to add number 2

    Retunrs: updated set with number 2 in it
    '''
    ex_set.add(2)
    assert ex_set == {1,2,3,11}
    return ex_set

def remove2(ex_set):
    '''
    A function that removes 2 from the set

    Params:
        ex_set: the set from which we need to remove number 2

    Retunrs: updated set without number 2 in it
    '''
    ex_set.remove(2)
    assert ex_set == {1,3,11}
    return ex_set

def is2IsStillInSet():
    print("There's no 2 in the set, because when we tried to add another 2 to the set in function add2 there was a 2 in the set so it didn't add number 2. Then we deleted number to in  remove2 function")

print(set_size(ex_set)) # get the size of the set (the number of elements it contains)
print(checkIf2IsPresent(ex_set)) # check if element 2 is present in the set
print(checkIf5IsPresent(ex_set)) # check if element 5 is present in the set
ex_set = add11(ex_set) # add 11 to the set. What is the size of the set?
print(ex_set)
print(set_size(ex_set))
ex_set = add2(ex_set) # add 2 in the set. What is his size ?
print(ex_set)
print(set_size(ex_set))
ex_set = remove2(ex_set)# remove element 2 from the set. 
print(ex_set)
is2IsStillInSet() # 2 is it still in the set?
print(set_size(ex_set)) # What is the size of the set?

e1,e2 = {1,2,3},{2,3,4,5} # Let e1 and e2 be the following two sets

def intersect(set1,set2):
    return set1.intersection(set2)

def union(set1,set2):
    return set1.union(set2)

def diff(set1,set2):
    return set1.difference(set2)

def symm_diff(set1,set2):
    return set1.symmetric_difference(set2)

def empty_set():
    e = set()
    assert isinstance (e, set)
    return e

print(intersect(e1,e2)) # intersection of e1 and e2
print(union(e1,e2)) # union of e1 and e2
print(diff(e1,e2)) # the elements of e1 that are not in e2?
print(symm_diff(e1,e2)) # the elements which are in e1 or e2 but not in the intersection

e = empty_set()