def shift_left(lst, n, fill_value=0):
    """Shifts all elements in a list n places to the left, and fills in the
    vacant list positions with fill_value. This should not return a new
    list; instead it should change the incoming list, lst, in place.

    numbers = [1, 2, 3, 4]
    shift_left(numbers, 2)  # no return value
    print(numbers) # --> [3, 4, 0, 0]

    :param lst: list to be shifted
    :type lst: list
    :param n: the number of places to shift each element
    :type n: int
    :param fill_value: the value filled in for the vacant spaces left after
    the shift
    :type fill_value: any
    :return: does not return a value
    :rtype: None
    """
    if(n>0):
        for i in range(len(lst)):
            if(i+n<len(lst)):
                lst[i]=lst[i+n];
            else:
                lst[i]=fill_value;

def shifted_left(lst, n, fill_value=0):
    """Creates a new list in which all elements from the original list
    passed in are shifted n places to the left, with the remaining vacant
    list positions filled in with fill_value. The new list is returned

    numbers = [1, 2, 3, 4]
    shifted_numbers = shifted_left(numbers, 2)
    print(shifted_numbers) # --> [3, 4, 0, 0]

    :param lst: list to be shifted
    :type lst: list
    :param n: the number of places to shift each element
    :type n: int
    :param fill_value: the value filled in for the vacant spaces left after
    the shift
    :type fill_value: any
    :return: new list with values shifted
    :rtype: list
    """
    new_list=[];
    for i in range(len(lst)):
        new_list.append(0);
    if(n>0):
        for i in range(len(lst)):
            if(i+n<len(lst)):
                new_list[i]=lst[i+n];
            else:
                new_list[i]=fill_value;
    #just copy the original list
    else:
        for i in range(len(lst)):
            new_list[i]=(lst[i]);
    return new_list;

def shift_right(lst, n, fill_value=0):
    """Shifts all elements in a list n places to the right, and fills in the
    vacant list positions with fill_value. This should not return a new
    list; instead it should change the incoming list, lst, in place.

    numbers = [1, 2, 3, 4]
    shift_right(numbers, 2)  # no return value
    print(numbers) # --> [0, 0, 1, 2]

    :param lst: list to be shifted
    :type lst: list
    :param n: the number of places to shift each element
    :type n: int
    :param fill_value: the value filled in for the vacant spaces left after
    the shift
    :type fill_value: any
    :return: does not return a value
    :rtype: None
    """
    #must be positive n
    if(n>0):
        #go backwards
        for i in range(len(lst)-1, -1, -1):
            if(i-n>=0):
                lst[i]=lst[i-n];
            else:
                lst[i]=fill_value;



def shifted_right(lst, n, fill_value=0):
    """Creates a new list in which all elements from the original list
    passed in are shifted n places to the right, with the remaining vacant
    list positions filled in with fill_value. The new list is returned

    numbers = [1, 2, 3, 4]
    shifted_numbers = shifted_right(numbers, 2)
    print(shifted_numbers) # --> [0, 0, 1, 2]

    :param lst: list to be shifted
    :type lst: list
    :param n: the number of places to shift each element
    :type n: int
    :param fill_value: the value filled in for the vacant spaces left after
    the shift
    :type fill_value: any
    :return: new list with values shifted
    :rtype: list
    """
    new_list=[];
    for i in range(len(lst)):
        new_list.append(0);
    #must be positive n
    if(n>0):
        #go backwards
        for i in range(len(lst)-1, -1, -1):
            if(i-n>=0):
                new_list[i]=lst[i-n];
            else:
                new_list[i]=fill_value;
    #just copy the original list
    else:
        for i in range(len(lst)):
            new_list[i]=lst[i];
    return new_list;

def fill(lst, fill_value=0):
    """Fills an existing list, lst, with the value, fill_value.

    numbers = [1, 2, 3, 4]
    fill(numbers)
    print(numbers) # [0, 0, 0, 0]

    :param lst: the list to be filled with values
    :type lst: list
    :param fill_value: the value to fill the list with
    :type fill_value: any
    :return: does not return a value
    :rtype: None
    """
    for i in range(len(lst)):
        lst[i]=fill_value;

def filled(lst, fill_value=0):
    """Creates a new list with the same length as the list passed in, lst,
    and fills it with the value, fill_value.

    numbers = [1, 2, 3, 4]
    filled_list = fill(numbers)
    print(filled_list) # [0, 0, 0, 0]

    :param lst: the list to use as the basis for the length of the new list
    :type lst: list
    :param fill_value: the value to fill the new list with
    :type fill_value: any
    :return: the new list filled with fill_value
    :rtype: list
    """
    lst=[fill_value for n in lst];
    return lst;

def mean(lst):
    """Calculates and returns the average of all numbers in incoming list, lst.

    print(mean([12, 4, 14])) # --> 10

    :param lst: list of numeric types
    :type lst: list
    :return: the average of all numbers in lst
    :rtype: float
    """
    tot = 0;
    for i in range(len(lst)):
        tot += lst[i];
    avg = tot/len(lst);
    return avg;

def median(lst):
    """Calculates the median of incoming list, lst.

    :param lst: list of numeric types
    :type lst: list
    :return: the median of all numbers in lst
    :rtype: int or float
    """
    if(len(lst)%2 == 1):
        return lst[(len(lst)//2)];
    else:
        return (lst[len(lst)//2]+(lst[len(lst)//2]-1))/2;

def std_dev(lst):
    """Calculates the standard deviation of the sample for the incoming list, lst.

    :param lst: list of numeric types
    :type lst: list
    :return: the standard devation of numbers in incoming list, lst
    :rtype: float
    """
    avg = mean(lst);
    lst = [(w-avg)**2 for w in lst];
    numer = sum(lst);
    return ((numer/(len(lst)-1))**.5);

if __name__ == '__main__':
    print("shift_left\n=====");
    numbers = [1, 2, 3, 4]
    shift_left(numbers, 2)
    print(numbers)
    numbers = [1, 2, 3, 4]
    shift_left(numbers, 5)
    print(numbers)
    numbers = [1, 2, 3, 4]
    shift_left(numbers, -5)
    print(numbers)
    numbers = [1, 2, 3, 4]
    shift_left(numbers, 1, None)
    print(numbers)
    print("\nshifted_left\n=====")
    numbers = [1, 2, 3, 4]
    print(shifted_left(numbers, 2))
    print(shifted_left(numbers, 5))
    print(shifted_left(numbers, -5))
    print(shifted_left(numbers, 1, None))
    print("\nshift_right\n=====")
    numbers = [1, 2, 3, 4]
    shift_right(numbers, 2)
    print(numbers)
    numbers = [1, 2, 3, 4]
    shift_right(numbers, 5)
    print(numbers)
    numbers = [1, 2, 3, 4]
    shift_right(numbers, -5)
    print(numbers)
    numbers = [1, 2, 3, 4]
    shift_right(numbers, 1, None)
    print(numbers)
    print("\nshifted_right\n=====")
    numbers = [1, 2, 3, 4]
    print(shifted_right(numbers, 2))
    print(shifted_right(numbers, 5))
    print(shifted_right(numbers, -5))
    print(shifted_right(numbers, 1, None))
    print("\nfill\n=====")
    numbers = [1, 2, 3, 4]
    fill(numbers)
    print(numbers)
    numbers = [1, 2, 3, 4]
    fill(numbers, fill_value=None)
    print(numbers)
    print("\nfilled\n=====")
    numbers = [1, 2, 3, 4]
    print(filled(numbers))
    print(filled(numbers, fill_value=None))
    print(mean([1, 2, 3, 4, 5]))
    print("\nmedian\n=====")
    print(mean([7, 11, 9, 18, 15, 12]))
    print(median([1, 2, 3, 4]))
    print(median([1, 2, 3]))
    print(median([1, 2]))
    print("\nstd_dev\n=====")
    print(std_dev([7, 11, 9, 18, 15, 12]))
