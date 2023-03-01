import maze

class Game():
    '''Holds the game solving logic. Initialize with a fully initialized maze'''

    def __init__(self, maze):
        self._maze = maze

    # Creating simple methods (like the next two) to abstract core parts 
    #   of your algorithm helps increase the readability of your code.
    #   You will find these two useful in your solution.

    def _is_move_available(self, row, col, path):
        '''If (row, col) is already in the solved path then it is not available'''
        return (row, col) not in path

    def _is_puzzle_solved(self, row, col):
        '''Is the given row,col the finish square?'''
        return self._maze.get_finish() == (row, col)


    ########################################################
    # TODO - Main recursive method. Add your algorithm here.
    def find_route(self, currow, curcol, curscore, curpath):#The method needs to return the winning score and path when it reaches the finish square of the maze.
        optimalpath = []
        maxscore = -1
        
        
        #Check if the current row and column represent the finish square by calling _is_puzzle_solved. If so, return the current score and path.'''
        if self._is_puzzle_solved(currow,curcol):
            return (curscore, curpath)
        
        if self._maze.get_start() not in curpath:
            curpath.append(self._maze.get_start())
            
        #implement recursive algorithim - one method would be writng a for loop or a bunch of if statements
        
        neighbors = [[currow+1, curcol],[currow-1, curcol],[currow ,curcol+1],[currow ,curcol-1]]
        for neighbor in neighbors:
            copypath = curpath.copy() #copys the path 
            if self._is_move_available(neighbor[0], neighbor[1], copypath) and self._maze.is_move_in_maze(neighbor[0], neighbor[1]) and not self._maze.is_wall(neighbor[0],neighbor[1]):
                newscore = curscore + self._maze.make_move(neighbor[0], neighbor[1],copypath)
                nextscore, nextpath = self.find_route(neighbor[0],neighbor[1],newscore,copypath) #next step in recurison 
                
                if nextscore> maxscore:
                    maxscore = nextscore
                    optimalpath = nextpath
                
       #If no path found return -1 to indicate failure
        return maxscore, optimalpath        




# This block of code will be useful in debugging your algorithm. But you still need
#  to create unittests to thoroughly testing your code.
if __name__ == '__main__':
    # Here is how you create the maze. Pass the row,col size of the grid.
    grid = maze.Maze(3, 6)
    # You have TWO options for initializing the Value and Walls squares.
    # (1) init_random() and add_random_walls()
    #     * Useful when developing your algorithm without having to create 
    #         different grids
    #     * But not easy to use in testcases because you cannot preditably
    #         know what the winning score and path will be each run
    # (2) _set_maze()
    #     * You have to create the grid manually, but very useful in testing
    #       (Please see the test_game.py file for an example of _set_maze())
    grid.init_random(0,9) # Initialze to a random board
    grid.add_random_walls(0.2)   # Make a certian percentage of the maze contain walls

    # AFTER you have used one of the two above methods of initializing 
    #   the Values and Walls, you must set the Start Finish locations. 
    start = (0,2)
    finish = (1,1)
    grid.set_start_finish(start, finish)

    # Printing the starting grid for reference will help you in debugging.
    print(grid)           # Print the maze for visual starting reference

    # Now instatiate your Game algorithm class
    game = Game(grid)     # Pass in the fully initialize maze grid

    # Now initiate your recursize solution to solve the game!
    # Start from the start row, col... zero score and empty winning path
    score, path = game.find_route(start[0], start[1], 0, list())
    print(f"The winning score is {score} with a path of {path}")

