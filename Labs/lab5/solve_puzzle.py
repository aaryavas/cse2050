def solve_puzzle(board,index = 0,vistied = 0): # Make sure to add input parameters here
    """Returns True(False) if a given board is (is not) solveable"""
    
    if vistied is None:
        vistied = set
    
    # 1) Base case: have you found a valid solution?
    #if value in board is one number return true or if the first index is equal to last index
    if index == len(board)-1: return True
    vistied.add(index)
    # 2) Find all valid next-steps
    next_move = set()
    moves = (index + board[index], index - board[index])
    
    for i in moves:
        i%= len(board)
        if i not in vistied:
            next_move.add()
        
    
    
    
    # 3) Recursively explore next-steps, returning True if any valid solution is found
    return any(solve_puzzle(board, i, vistied) for i in next_move)