# Improvement over first maze script
# * Encapsulated in a class; using dataclass
# * Improved comments
# * Improved method names

from dataclasses import dataclass

@dataclass
class Maze:
    maze: list
    N: int = 9

    def __post_init__(self) -> None:
        self.maze_solution = [[0 for x in range(self.N)] for y in range(self.N)]
    
    def __repr__(self) -> str:
        return ''.join([str(x)+'\n' for x in self.maze])

    def isSafe(self, x,y) -> bool:
        # Check if the path is safe to go in
        if x >= 0 and x < self.N and y >= 0 and y < self.N and self.maze[x][y] == 1:
            return True
        else:
            return False

    def checkForSolution(self) -> bool:
        # Check if the Maze has reached for a solution
        # This will recursively call itself, so we start at 0,0
        if self.mazeSolver(0, 0):
            # print solution
            for _ in self.maze_solution: print(_)
            return True
        else:
            print('No Solution')
            for _ in self.maze_solution: print(_)
            return False

    def mazeSolver(self, x, y) -> bool:
        # If we have reached the last row and there is an exit we have solved the maze
        if x == self.N - 1 and self.maze[x][y] == 1:
            self.maze_solution[x][y] = 1
            return True
        # If we can go in this path, mark it in the solution
        if self.isSafe(x, y):
            self.maze_solution[x][y] = 1
            # Check the space at the right (If we reach a solution, the func will be True)
            if self.mazeSolver(x+1, y):
                return True
            # Check the space below (If we reach a solution, the func will be True)
            if self.mazeSolver(x, y+1):
                return True
            # If the paths traveled do not go to a solution, then return false
            # And set this instance as a not viable path
            self.maze_solution[x][y] = 0
            return False
            
maze = Maze([[1, 0, 0, 0, 0, 0, 0, 0, 0], 
             [1, 1, 0, 1, 0, 1, 1, 1, 0], 
             [0, 1, 0, 0, 0, 1, 0, 1, 0], 
             [1, 1, 1, 1, 1, 1, 0, 1, 0],
             [1, 1, 1, 1, 0, 1, 0, 1, 1],
             [1, 1, 1, 1, 0, 1, 0, 1, 1],
             [1, 1, 1, 1, 0, 1, 1, 1, 1],
             [1, 1, 1, 1, 0, 0, 0, 1, 1],
             [0, 0, 0, 0, 0, 0, 0, 1, 1]])

maze.checkForSolution()