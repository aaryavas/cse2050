def greedy_fewest_coins(amt_in_cents, coin_value_list = [1,5,10,25]):
    # Sort and reverse coin list
    coin_value_list.sort(reverse=True)

    # Iterate through coin list, biggest value first
        # Use as many largest coins as possible
        # deduct that value from the amount remaining

    # Return number of coins
    num_coins = 0

    for coin in coin_value_list:
        if coin <= amt_in_cents:
            num_coins += amt_in_cents // coin   #  63 // 25 = 2
            amt_in_cents %= coin                # 63 % 25  = 13

    return num_coins

def recr_fewest_coins(amt, coins = {1,5,10,25}):
    #sort and reverse coin list
    # iterate through coin list, biggest value first
        #use as many largest coins as possible 
        #deduct that value form the amount remaining
    
    
    
    if amt in coins: return 1
    
    #initialzie guess at optimum solution
    min_coins = amt
    
    #go through every valud path
    for coin in coins:
        #TODO: check if you've already solved this problem 
        if 
        
        if coin <= amt:
            
        
            path_optimum = 1+ recr_fewest_coins(amt-coin, coins)
            #              1 + fc(62) #1
            #              1 + fc(58) #5
            #              1+ fc(53)  #10 
            #              1+  fc(42) #21
            
            if path_optimum < min_coins:
                min_coins = path_optimum
   
   
    return min_coins

        


print("Fewest coins to make $0.63 using only:")
print("\tpennies: ", end = '')
print(greedy_fewest_coins(63, [1]))

print("\tpennies and nickles: ", end = '')
print(greedy_fewest_coins(63, [1, 5]))

print("\tpennies, nickles, and dimes: ", end = '')
print(greedy_fewest_coins(63, [1, 5, 10]))

print("\tpennies, nickles, dimes, and quarters: ", end = '')
print(greedy_fewest_coins(63, [1, 5, 10, 25]))


################################### Quiz ###################################
# Will this give the correct answer (fewest coins) for any amount and      #
# any list of coins?                                                       #
#    1) yes                                                                #
#    2) no                                                                 #
############################################################################



# print("\tpennies, $0.21 pieces, and quarters: ", end = '')
# print(greedy_fewest_coins(63, [1, 5, 10, 21, 25]))