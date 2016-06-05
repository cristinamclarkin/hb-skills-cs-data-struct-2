#Sorting

def bubble_sort(lst):
    """returns a sorted list using a optimized bubble sort algorithm
    i.e. using a variable to track if there hasn't been a swap
        >>> bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """

    for i in range(len(lst) - 1):
         # Keeps track of swaps that have been made
        swap = False
        # go through list until the last item
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                # swap position if one is higher
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swap = True
        # if no swap has happened, list is already sorted, break
        if not swap:
            break

    return lst


    

def merge_lists(list1, list2):
    """Given two sorted lists of integers, returns a single sorted list containing all
    integers in the input lists
    >>> merge_lists([1, 3, 9], [4, 7, 11])
    [1, 3, 4, 7, 9, 11]
    """

    #initialize new empty list
    sorted_list = []

    while len(list1) > 0 or len(list2) > 0:
        if list1 == []:
            sorted_list.append(list2.pop(0))
        elif list2 == []:
            sorted_list.append(list1.pop(0))
        #compare first items of each list, add smaller of two items to final sorted list
        elif list1[0] < list2[0]:
            # append and remove first item of list1
            sorted_list.append(list1.pop(0))
        else:
            # append and remove first item of list2
            sorted_list.append(list2.pop(0))

    return sorted_list

    


##########ADVANCED##########
def merge_sort(lst):
    """
    Given a list, returns a sorted version of that list.
    Finish the merge sort algorithm by writing another function that
    that takes in a single unsorted list of integers and uses recursion and the 'merge_lists'
    function you already wrote to return a new sorted list containing all integers from
    thin input list. In other words, the new function should sort a list using merge_lists
    and recursion.
    >>> merge_sort([6, 2, 3, 9, 0, 1])
    [0, 1, 2, 3, 6, 9]
    """
   

    # Break everything down into a list of one
    if len(lst) < 2:  # if length of lst is 1, return lst
        return lst

    mid = int(len(lst) / 2)  # index at half the list
    lst1 = merge_sort(lst[:mid])  # divide list in half
    lst2 = merge_sort(lst[mid:])  # assign other half

    # Compare first items of each pair of lists & interleave

    result_list = []
    while len(lst1) > 0 or len(lst2) > 0:
        # if items left in both lists
        # compare first items of each list
        if lst1 == []:
            result_list.append(lst2.pop(0))
        elif lst2 == []:
            result_list.append(lst1.pop(0))
        elif lst1[0] < lst2[0]:
            # append and remove first item of lst1
            result_list.append(lst1.pop(0))
        else:
            # append and remove first item of lst2
            result_list.append(lst2.pop(0))

    return result_list


    




#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print