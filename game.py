import pygame
from maze import Maze
from player import Player
from raycasting import Raycasting

# Constants
WIDTH, HEIGHT = 800, 600

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

if __name__ == "__main__":
    game = Game()
    game.run()

