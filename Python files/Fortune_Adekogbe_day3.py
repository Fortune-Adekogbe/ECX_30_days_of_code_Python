def bin_search(List, Num):
    '''
    This function takes in a list with a predefined number of elements and target number.
    It returns a boolean indicating whether the target number is found in the list or not.
    '''
    assert type(List)==list , 'You have not entered a list'
    assert type(Num) is int, 'The element to be found has to be an integer.'
    List = sorted(List)
    x = len(List)
    while len(List) > 1:
        pos = len(List) // 2
        if Num > List[pos]:
            List = List[pos:]
        elif Num == List[pos]:
            return True
        else:
            List = List[:pos]
    return False


print(bin_search(list(range(0, 99999,2)), 555))

