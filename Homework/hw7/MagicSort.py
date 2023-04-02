from math import log2
from random import randint
def linear_scan(L):
    
    #initialize counters for sorted and reverse sorted
    sorted_count = 0
    reverse_sorted_count = 0


    #if list empty return sorted
    if not L:
        return 'sorted'

    #iterate through list
    for i in range(len(L) - 1):
        
        #if item is less than next item increases count in sorted
        if L[i] <= L[i + 1]:
            sorted_count += 1
        if L[i] >= L[i + 1]:
            reverse_sorted_count += 1


    # Check edge cases:
    
    #if list already sorted return sorted
    if sorted_count == len(L) - 1:
        return 'sorted'
    
    #if more than 5 items out of place return insertion
    elif reverse_sorted_count <= 5:
        return 'insertion'
    
    # If the list is reverse sorted, return 'reverse_sorted' to use the reverse_list function
    elif reverse_sorted_count == len(L) - 1:
        return 'reverse_sorted'
    
    # If none of the edge cases apply, return 'none'
    else:
        return 'none'

def reverse_list(L):
    #reverses list
    L.reverse()

def insertionsort(L, left, right):
    
    # Iterate over the range of indices in L
    for i in range(left + 1, right + 1):
    
        # Set j to the index immediately to the left of i
        key_item = L[i]
        # Set j to the index immediately to the left of i
        j = i - 1
        # While j is greater than or equal to left AND the value at L[j] is greater than key_item
        while j >= left and L[j] > key_item:
            # Shift the value at L[j] one position to the right
            L[j + 1] = L[j]
            # Decrement j by 1
            j -= 1
        # Insert key_item into its proper location
        L[j + 1] = key_item

def quicksort(L, left, right):
    #base case: if the sublist has less than and equal 1 elements it is already sort
    if right - left <= 1:
        return None

    #random pivot index
    pivot_idx = randint(left, right - 1)

    # Partition
    pivot_val = L[pivot_idx]
    i, j = left, right - 1
    while i <= j:
        while L[i] < pivot_val:
            i += 1
        while L[j] > pivot_val:
            j -= 1
        if i <= j:
            L[i], L[j] = L[j], L[i]
            i += 1
            j -= 1

    # Recursive
    quicksort(L, left, j + 1)
    quicksort(L, i, right)

    # Return sorted list
    return L

def mergesort(L):
    # Base case: if the list has 0 or 1 elements, it is already sorted
    if len(L) <= 1:
        return L

    # Divide the list into two halves
    mid = len(L) // 2
    left_half = L[:mid]
    right_half = L[mid:]

    # Recursive
    sorted_left = mergesort(left_half)
    sorted_right = mergesort(right_half)

    # Merge
    merged = []
    i, j = 0, 0
    while i < len(sorted_left) and j < len(sorted_right):
        if sorted_left[i] < sorted_right[j]:
            merged.append(sorted_left[i])
            i += 1
        else:
            merged.append(sorted_right[j])
            j += 1
    merged += sorted_left[i:]
    merged += sorted_right[j:]

    # Return
    return merged

def magic_sort(L):
    #create set
    algorithms_used = set()
    
    
    # Step 1: Linear scan
    scan_result = linear_scan(L)
    if scan_result == 'sorted':
        algorithms_used.add('sorted')
        return algorithms_used
    elif scan_result == 'insertion':
        algorithms_used.add('insertionsort')
        insertionsort(L, 0, len(L) - 1)
        return algorithms_used
    elif scan_result == 'reverse_sorted':
        algorithms_used.add('reverse_list')
        reverse_list(L)


    # Step 2: Quicksort
    algorithms_used.add('quicksort')
    quicksort(L, 0, len(L) - 1)


    # Step 3: Check if the depth got too high
    depth = 2 * (log2(len(L)) + 1)
    if depth > log2(len(L)):
        mergesort(L)
        algorithms_used.add('mergesort')


    # Step 4: Check if sublists are small enough for insertion sort
    if len(L) <= 16:
        algorithms_used.add('insertionsort')
        insertionsort(L, 0, len(L) - 1)

    return algorithms_used