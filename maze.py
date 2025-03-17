import random

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = [[1] * width for _ in range(height)]
        self.generate_maze()

    def generate_maze(self):
        """
        Generates a solvable maze using depth-first search,
        with a randomly placed exit.
        """
        stack = [(1, 1)]
        self.maze[1][1] = 0

        directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]

        while stack:
            x, y = stack[-1]
            random.shuffle(directions)
            carved = False

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (1 <= nx < self.height - 1 and
                        1 <= ny < self.width - 1 and
                        self.maze[nx][ny] == 1):
                    self.maze[nx][ny] = 0
                    self.maze[x + dx // 2][y + dy // 2] = 0
                    stack.append((nx, ny))
                    carved = True
                    break

            if not carved:
                stack.pop()

        # Set entrance
        self.maze[1][0] = 0
        
        # Set random exit along the last row or last column
        exit_options = []
        for row in range(1, self.height - 1):
            if self.maze[row][self.width - 2] == 0:
                exit_options.append((row, self.width - 1))
        for col in range(1, self.width - 1):
            if self.maze[self.height - 2][col] == 0:
                exit_options.append((self.height - 1, col))

        if exit_options:
            exit_x, exit_y = random.choice(exit_options)
            self.maze[exit_x][exit_y] = 0

    def get_maze(self):
        return self.maze

