class Mazesolver(object):
    def __init__(self, maze, N):
        self.maze = maze
        self.N = N

    def is_safe(self, x, y):
        '''
        Check whether x and y are valid indexes of a maze.
        '''
        return (x >= 0 and x < self.N and y >= 0 and y < self.N and 
                self.maze[x][y] == 1)

    def solve(self, start, end):
        solution = [[0]*self.N for i in range(self.N)]
        # List to store all possible paths.
        result = []
        # Find out al possible paths one by one and block the path in a maze
        # once it is identified so that new path can be found out.
        while True:
            res = self.solve_maze_util(start, end, solution)
            if isinstance(res, bool) and not res:
                break
            else:
                result.append(res[1])
                # Block the recently obtained path in a maze.
                for i in range(self.N):
                    for j in range(self.N):
                        if solution[i][j] == 1:
                            self.maze[i][j] = 0
        print "All possible paths"
        print result

    def solve_maze_util(self, x, y, solution, result=[]):
        if x == (self.N - 1) and y == (self.N - 1):
            solution[x][y] = 1
            return True
        # Check if maze is valid
        if self.is_safe(x, y):
            # Mark x, y part of solution path.
            result.append((x,y, ))
            solution[x][y] = 1
            # Move forward in x direction
            if self.solve_maze_util(x+1, y, solution):
                return True, result
            # If moving in x direction does not give solution then move down
            # in y direiction
            if self.solve_maze_util(x, y+1, solution):
                return True, result

            # If none of the above movements work then backtrack and unmark
            # 
            # x,y position
            solution[x][y] = 0
            return False
        return False



if __name__ == "__main__":
    maze = [[1, 0 ,0 ,0], [1, 1, 0, 1], [0, 1, 0, 0], [1, 1, 1, 1]]
    ms = Mazesolver(maze, 4)
    ms.solve(start=0, end=0)
