import pygame
from maze import Maze
from player import Player
from raycasting import Raycasting

# Constants
WIDTH, HEIGHT = 800, 600
TILE_SIZE = 40  # Size of each tile in pixels
MINIMAP_SCALE = 0.2  # Scale for minimap size

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
        self.raycasting.render(self.screen)  # Render the 3D view
        self.draw_minimap()

    def draw_minimap(self):
        """ Draw a scaled-down minimap in the top-left corner. """
        mini_tile = int(TILE_SIZE * MINIMAP_SCALE)
        maze_data = self.maze.get_maze()
        
        for row in range(len(maze_data)):
            for col in range(len(maze_data[0])):
                color = (255, 255, 255) if maze_data[row][col] == 1 else (0, 0, 0)
                pygame.draw.rect(self.screen, color,
                                 (col * mini_tile, row * mini_tile, mini_tile, mini_tile))
        
        # Draw player on minimap
        player_x = int(self.player.x * mini_tile)
        player_y = int(self.player.y * mini_tile)
        pygame.draw.circle(self.screen, (255, 0, 0), (player_x, player_y), 3)

if __name__ == "__main__":
    game = Game()
    game.run()
