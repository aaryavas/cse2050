'''def partition(L, left, right):
    'partition L about L[right -1]'
    
    partition([76,5,4,3,2,1], 0, 7)
    partition L about L[6]
    
    #get everything smalle to the left
    #everything equal or bigger to the right 
    #swap your pivot
    #return new index o fpiv
    '''
import random, timeit, sys
def is_sorted(L): return not any(L[i] > L[i+1] for i in range(len(L)-1))

def quicksort(L, left right = None):#will sort list in place
    "Sorts L in-place using quicksort"
    
    if right is None: right = len(L)
    
        
    #base case - like mergesort
    if right - left  <= 1
    
    #divide
    median  = partition(L, left, right)
    
    quicksort(L, left, median )
    quicksort(L, median +1, right )

    

def partition(L, left, right):
    
       
    #init counter
    i = left # idx of first item
    j = right -2 #idx of 2nd last item 
    pivot = right -1 #idx of last item 
    
    while i < j:
        #find first big item on left
        while L[i] < L[pivot]: 
            i += 1
            
        #find first small item on right
        while i < j and L[j] >= L[pivot]:
            j -= 1
    
        if i < j: 
            L[j], L[i] = L[i], L[j]
    L[i], L[pivot] = L[pivot], L[i]
    pivot = i
    
    return pivot
        
        
    
    """Partitions L[left:right] around L[right-1]
            Input
            -----
                L: list[int]
                    list of integers
                left: int
                    index of leftmost item to be considered
                right: int
                    index of rightmost item to be considered + 1

            Output
            ------
                pivot: int
                    index of the pivot element after partitioning (where L[right-1] ends up)
    """

def mergesort(L, depth = 0):
    "sorts L using mergesort"
    # base case
    depth += 1 
    global max_depth
    if depth > max_depth:
        
    
    if len(L) <= 1: return L
    
    # divide
    median = len(L) // 2
    Lleft = mergesort(L[:median])
    Lright = mergesort(L[median:])

    # conquer
    merge(L, Lleft, Lright)

    return L

def merge(L, Lleft, Lright):
    "merges sorted sublists Lleft and Lright into L"
    i, j = 0, 0
    while i < len(Lleft) and j < len(Lright):
        if Lleft[i] < Lright[j]:
            L[i+j] = Lleft[i]
            i += 1
        else:
            L[i+j] = Lright[j]
            j+=1

    L[i+j:] = Lleft[i:] + Lright[j:]
    
    return L

if __name__ == '__main__':
    # test our algs work
    n = 1000

    L = [random.randint(0, n) for i in range(n)]
    Lmerge = L[:]
    Lquick = L[:]

    mergesort(Lmerge)
    assert is_sorted(Lmerge)
    
    quicksort(Lquick)
    assert is_sorted(Lquick)
  
    """
    ### Times mergesort
    t_merge = 1000*timeit.timeit("mergesort(L)", setup=f"L={Lmerge}", globals=globals(), number=1) 
    print(f"t_merge: {t_merge:.3f} ms")
    print(f"max_depth = {max_depth}") 
    print()

    ### Times quicksort
    t_quick = 1000*timeit.timeit("quicksort(L)", setup=f"L={Lquick}", globals=globals(), number=1)
    print(f"t_quick: {t_quick:.3f} ms")
    print()
    """