def find_zero(L): # returns the index of the 0 
    for x in range(len(L)):
        if x == 0:
            return L.index(x)
    
def bubble(L, left, right): 
    swap = False

    for x in range(right-1): # iterates through list
        for y in range(left, right - x - 1): # iterates through elements
            if L[y] > L[y + 1]: #if the first element is larger, swap them
                swap = True
                temp = L[y]
                L[y] = L[y+1]
                L[y+1] = temp
        if swap == False: # if nothing swapped exit loop
            return
    return L

def selection(L, left, right): 
    for x in range(left, right): # iterates through list
        min = x 
        for y in range(min + 1, right): 
            if L[y] < L[min]: # if list at y is smaller than the list at min value change value
                min = y
        # swap values 
        temp = L[x]
        L[x] = L[min]
        L[min] = temp
    # return list
    return L


def insertion(L, left, right):
    if (right >= 1): # run the rest if there list has one element
        for x in range(left + 1, right): # iterates through elements
            key = L[x]
            y = x - 1 
            
            while y >= 0 and key < L[y]: # while key is smaller and y is a valid index
                L[y+1] = L[y] 
                y -= 1 
            L[y+1] = key 
    return L

def sort_halfsorted(L, sort):
    '''Efficiently sorts a list comprising a series of negative items, a single 0, and a series of positive items
    
        Input
        -----
            * L:list
                a half sorted list, e.g. [-2, -1, -3, 0, 4, 3, 7, 9, 14]
                                         <---neg--->     <----pos----->

            * sort: func(L:list, left:int, right:int)
                a function that sorts the sublist L[left:right] in-place
                note that we use python convention here: L[left:right] includes left but not right

        Output
        ------
            * None
                this algorithm sorts `L` in-place, so it does not need a return statement

        Examples
        --------
            >>> L = [-1, -2, -3, 0, 3, 2, 1]
            >>> sort_halfsorted(L, bubble)
            >>> print(L)
            [-3, -2, -1, 0, 1, 2, 3]
    '''
    copy_L = L[:] 
    idx_zero = find_zero(L)     
    sort(copy_L, 0, idx_zero)        
    sort(copy_L, idx_zero+1, len(L)) 
    return copy_L