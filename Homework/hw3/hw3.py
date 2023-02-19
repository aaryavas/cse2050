import time 

'''iterates over two nested loops to check for pairs that match the target'''
def find_pairs_naive(lst, target):

    mySet = set() #1
    #loop
    for i in lst: #n
        for x in lst: #n
            if i + x == target and (i,x) not in mySet and (i,x) and x!=i:
                mySet.add((i,x))  
                lst.remove(i)


    return mySet #1 
                #--------
                #overall has 0(n^2) complexity (1+ (n^2) *5 +1)

'''Function uses hash map for shorter time complexity'''
def find_pairs_optimized(lst, target):

    pairs = set()#1
    diff = set()#1
    #hash map for shorter time complexity
    for x in lst: #n
        if x in diff: #1
            pairs.add((target-x, x)) #2
        else: #1
            diff.add(target-x) #1


    return pairs #1 
                #-------
                #has complexity 0(n) (2 +n *8 + 1)

'''finds the minimum time over 10 average runs'''
def measure_min_time(fn, args):
    TotalTimeList= []

    for i in range(10):
        start = time.time()
        fn(*args)
        end = time.time()
        total = end - start
        TotalTimeList.append(total)


    sort = sorted(TotalTimeList)
    return sort[0] 

'''Measuring running times over given intervals'''
if __name__ == "__main__":
    list, n_value, a = [0,1,2,3,4,5,6,7,8,9], [10,50,100,150,200, 300, 500], ' '

    print('''n               naive             optimized
**************************************************''')


    for i in range (len(n_value)):
        if n_value[i] > 99:
            a =''

        print(str(n_value[i]) + a +'             ' + str(f'{measure_min_time(find_pairs_naive,(list*(int(n_value[i]/10)), 6)):.4f}')+'             '+f'{measure_min_time(find_pairs_optimized,(list*int((n_value[i]/10)), 6)):.4f}')
    print("--------------------------------------------------")



