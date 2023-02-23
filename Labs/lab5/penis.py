
board = [3, 4, 1, 2, 0]
index = len(board)    
visted = set()


# 1) Base case: have you found a valid solution?
#if value in board is one number return true or if the first index is equal to last index
if board[0] == board[-1]: 
    print('True')
visted.add(index)
print(visted)
# 2) Find all valid next-steps
next_move = set()
moves = (index + board[index], index - board[index])
    
for i in moves:
    
    if i not in visted:
        next_move.add(i)
        
        
    