import pygame
import math

# Constants
FOV = math.pi / 3  
NUM_RAYS = 120  
MAX_DEPTH = 20  
TILE_SIZE = 40  

# Colors
BLACK = (0, 0, 0)

class Renderer:
    def __init__(self, maze, player):
        self.maze = maze.get_maze()  # Get the maze layout
        self.player = player

    def cast_rays(self, screen):
        """Raycasting function to draw walls."""
        for ray in range(NUM_RAYS):
            angle = self.player.angle - (FOV / 2) + (ray / NUM_RAYS) * FOV
            sin_a = math.sin(angle)
            cos_a = math.cos(angle)

            for depth in range(MAX_DEPTH):
                target_x = self.player.x + depth * cos_a * TILE_SIZE
                target_y = self.player.y + depth * sin_a * TILE_SIZE

                col, row = int(target_x / TILE_SIZE), int(target_y / TILE_SIZE)
                if 0 <= row < len(self.maze) and 0 <= col < len(self.maze[0]):
                    if self.maze[row][col] == 1:
                        wall_height = int(600 / (depth + 0.1))  # Adjusted height
                        color = (255 - min(depth * 15, 255),) * 3
                        pygame.draw.rect(
                            screen, color, (ray * (800 // NUM_RAYS), 300 - wall_height // 2, 800 // NUM_RAYS, wall_height)
                        )
                        break

    def render(self, screen):
        """Render the scene."""
        screen.fill(BLACK)
        self.cast_rays(screen)

