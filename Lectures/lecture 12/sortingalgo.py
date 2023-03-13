'bubble sort'#adaptive
def is_sorted(L):
    return not any(L[i] > L[i+1] for i in range(len(L)-1))

def bubble(L):
    n = len(L)
    
    for i in range(n-1):
        for j in range(n-1-i):
            if L[j] > L[j+1]:
                keepgoing = True
                L[j+1], L[j] = L[j], L[j+1]
        
        if not keepgoing: break                    


'selection sort' #very very big random lists
'insertion sort'#adaptive
'cocktail sort'


if __name__ == '__main__':
    assert is_sorted([1,2,3])
    assert not is_sorted([3,2,1])
    
    
    n = 1000
    assert not is_sorted(L)
    L = [n for i in range(n)]
    L[n-1] = -1
    print('starting to sort...')
    bubble(L)
    print('sorted')
    