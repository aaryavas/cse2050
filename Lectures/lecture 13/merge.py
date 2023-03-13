def merge(L1, L2):
    'returns L3, which is a sortedversion of L1+ L2'
    #do not use list.sort()
    #assume L1 and L2 are sorted

    
    L3 = (None for i in range(len(L1) +len(L2)))
    i1, i2 =0,0
    
    while i1 < len(L1)  and i2 < len(L2):
        #find smaller of two items and write into L3
        if L1[i1] < L2[i2]:
            L3[i1+i2] = L1[i1]    