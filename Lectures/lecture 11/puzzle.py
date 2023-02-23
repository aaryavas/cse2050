def solve_puzzle(board, idx = 0, visted = None):
    if visted is None: visted = set()
    visted.add(idx)
    
    
    #base case
    if idx == len(board)-1: return True
    
    #find all valid moves
    idx_cw = idx + board[idx]
    idx_ccw = idx - board[idx]
    valid_moves = [idx_cw,idx_ccw]
    #valid moves in fewest coins
    #valid_coins = [coins for coin in coins if coin <= amt]
    
    #explore everything
    for move in valid_moves:
        if move in visted: continue #skip this iter of for loop and move onto next iter
        
        
        
        path_optimum = solve_puzzle(board, move)      
        if path_optimum: return True # short circuts if we find a solution
        
    return False
    
    #   while idx_cw >= len(board):
    #       idx_cw = len(board)    
    # explore all valid moves
 

    # return optimal solution 