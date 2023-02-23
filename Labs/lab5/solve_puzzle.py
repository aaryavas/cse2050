def solve_puzzle(board = None,index = 0,vistied = 0): # Make sure to add input parameters here
    """Returns True(False) if a given board is (is not) solveable"""
    
    index = len(board)
    
    # 1) Base case: have you found a valid solution?
    #if value in board is one number return true or if the first index is equal to last index
    if board[i] == board[-1]: return True
    visted.add(index)
    # 2) Find all valid next-steps
    next_move = set()
    moves = (index + board[index], index - board[index])
    
    for i in moves:
        
        if move not in vistied:
            next_move.add()
        
    
    
    
    # 3) Recursively explore next-steps, returning True if any valid solution is found