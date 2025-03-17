import pygame
from maze import Maze
from player import Player
from raycasting import Raycasting

# Constants
WIDTH, HEIGHT = 800, 600
TILE_SIZE = 40  # Size of each tile in pixels

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        # Create game objects
        self.maze = Maze(20, 15)
        self.player = Player()
        self.raycasting = Raycasting(self)  # Pass self so raycasting can access game attributes

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.player.move(self.maze.get_maze())  # Move player

    def render(self):
        self.screen.fill((0, 0, 0))
        self.draw_maze()
        self.raycasting.render(self.screen)  # Render the 3D view
        self.draw_player()
    
    def draw_maze(self):
        """ Draw the maze in 2D for debugging """
        maze_data = self.maze.get_maze()
        for row in range(len(maze_data)):
            for col in range(len(maze_data[0])):
                if maze_data[row][col] == 1:
                    pygame.draw.rect(self.screen, (255, 255, 255),
                                     (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
    
    def draw_player(self):
        """ Draw the player on the 2D map """
        pygame.draw.circle(self.screen, (255, 0, 0),
                           (int(self.player.x * TILE_SIZE), int(self.player.y * TILE_SIZE)), 5)

if __name__ == "__main__":
    game = Game()
    game.run()
