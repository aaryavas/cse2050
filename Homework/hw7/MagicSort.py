from math import log2


def linear_scan(L): 
    #checks if list is already sorted 
    #   if list is already sorted return immediately
    if L == sorted(L):
        return L
    
    #if 5 or more items are out of place use insertion sort
    
    
    #check if list is reverse sorted and if so reference reverse list
    if reverse_list(L) == sorted(L):#this might be wrong looks like horrible code
        return reverse_list(L)

    #if no special cases found default to quick sort
def reverse_list(L): 
    #write algo to see if list is reverst sorted and will flip the list
    
    newL = []
    for i in L:
        newL = [i] + newL
    return newL
        

def insertionsort(L, left, right):
     
    #when divide and conquer falls below 16 items use insertion sort 

    
    #base algo not sure if this will work 
    if (right >= 1): # run the rest if there list has one element
        for x in range(left + 1, right): # iterates through elements
            key = L[x]
            y = x - 1 
            
            while y >= 0 and key < L[y]: # while key is smaller and y is a valid index
                L[y+1] = L[y] 
                y -= 1 
            L[y+1] = key 
    return L

def quicksort(L, left, right ):pass
    #use last item in the sublist as pivot point
    
    #keep track of recursive depth
    #   best case maximum depth is 
    #   If the recursive depth reaches twice the best-case maximum-depth, use mergesort 
    #   use log to determine this

def mergesort():pass
    # use if quick sort exceed maximum depth 
    
   
def magic_sort(): pass
    #should sort l in place