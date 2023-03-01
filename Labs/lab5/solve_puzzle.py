def solve_puzzle(puzzle, seen = None, index = 0): # Make sure to add input parameters here
    if seen == None:    seen = []
    if index == (len(puzzle) - 1):  return True
    if index in seen:   return False
    seen += [index]
    return solve_puzzle(puzzle, seen, (index + puzzle[index])%len(puzzle)) or solve_puzzle(puzzle, seen, (index - puzzle[index])%len(puzzle))