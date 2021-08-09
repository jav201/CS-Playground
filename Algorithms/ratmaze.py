maze = [[1, 0, 0, 0, 0, 0, 0, 0, 0], 
        [1, 1, 0, 1, 0, 1, 1, 1, 0], 
        [0, 1, 0, 0, 0, 1, 0, 1, 0], 
        [1, 1, 1, 1, 1, 1, 0, 1, 0],
        [1, 1, 1, 1, 0, 1, 0, 1, 1],
        [1, 1, 1, 1, 0, 1, 0, 1, 1],
        [1, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 1, 1]] 
def print_maze(solution):
    for i in solution:
        print(i)

N = len(maze)
# Create an empty maze
solution = [[0 for x in range(N)] for y in range(N)]
# Check if the given coordinates are valid and 
# the path is valid
def isSafe(maze, x,y):
    if x >= 0 and x<N and y >=0 and y<N and maze[x][y] == 1:
        return True
    else:
        return False

def solveMaze(maze, solution):
    # Call solveMaze which will call itself upon resolution
    if solveMazeBT(maze, 0, 0, solution) == False:
        print('No solution')
        return False
    print_maze(solution)
    return True

def solveMazeBT(maze, x,y, solution):
    # Check if we have reached the exit and if so return TRUE
    if x == N-1 and y == N-1 and maze[x][y] == 1:
        solution[x][y] = 1
        return True
    # Check for teh current path validity
    if isSafe(maze,x,y) == True:
        # Mark as part of the solution
        solution[x][y] = 1
        # Move on one space in X
        if solveMazeBT(maze, x+1, y, solution) == True:
            return True
        # Move on one space in Y
        if solveMazeBT(maze, x, y+1, solution) == True:
            return True
        # If there are no valid options to move in x nor in y
        # delete the current x,y marking and return False
        # to backtrack into the last valid space
        solution[x][y] = 0
        return False
        
solveMaze(maze, solution)