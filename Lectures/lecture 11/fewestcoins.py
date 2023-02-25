'''
solved in dictionary 
should look like 
solved= {1:1, 2:2, 3:3,4:4,5:1,6:2}

'''
def recr_fewest_coins(amt, coins, solved=None):
    # initialize solved in the first pass
    
    #solved = {} - my way
    if solved is None: solved = (coin:1  for coin in coins)
    
    #if amt in coins: return 1
    if amt in solved: return solved[amt]
    # initialize guess at "optimum" solution
    min_coins = amt # use pennies

    # find all possible solutions
    valid_coins = [coin for coin in coins if coin <= amt]

    # go through every valid path
    for coin in valid_coins:
        # TODO: check if you've already solved this problem
        #if coin in solved:- my way 
        #    solved.update({amt,coins})
        path_optimum = 1 + recr_fewest_coins(amt-coin, coins)

        if path_optimum < min_coins:
            min_coins = path_optimum

    # update solved problems

    return min_coins





#to test
print("Fewest coins to make $0.63 using only:")
print("\tpennies: ", end = '')
print(recr_fewest_coins(63, [1]))

print("\tpennies and nickles: ", end = '')
print(recr_fewest_coins(63, [1, 5]))

print("\tpennies, nickles, and dimes: ", end = '')
print(recr_fewest_coins(63, [1, 5, 10]))

print("\tpennies, nickles, dimes, and quarters: ", end = '')
print(recr_fewest_coins(63, [1, 5, 10, 25]))


print("\tpennies, $0.21 pieces, and quarters: ", end = '')
print(recr_fewest_coins(63, [1, 5, 10, 21, 25]))
