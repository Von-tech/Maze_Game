import pygame
import numpy as np
import math

# Constants
WIDTH, HEIGHT = 800, 600
FOV = math.pi / 3  # Field of view
NUM_RAYS = 120
MAX_DEPTH = 20
TILE_SIZE = 40

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Sample Maze (1 = Wall, 0 = Empty space)
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]
MAP_WIDTH = len(maze[0]) * TILE_SIZE
MAP_HEIGHT = len(maze) * TILE_SIZE

# Player settings
player_x = TILE_SIZE + TILE_SIZE // 2
player_y = TILE_SIZE + TILE_SIZE // 2
player_angle = 0


def cast_rays():
    """Raycasting function to draw walls"""
    for ray in range(NUM_RAYS):
        angle = player_angle - (FOV / 2) + (ray / NUM_RAYS) * FOV
        sin_a = math.sin(angle)
        cos_a = math.cos(angle)

        for depth in range(MAX_DEPTH):
            target_x = player_x + depth * cos_a * TILE_SIZE
            target_y = player_y + depth * sin_a * TILE_SIZE

            col, row = int(target_x / TILE_SIZE), int(target_y / TILE_SIZE)
            if 0 <= row < len(maze) and 0 <= col < len(maze[0]):
                if maze[row][col] == 1:
                    wall_height = int(HEIGHT / (depth + 0.1))
                    color = (255 - min(depth * 15, 255), 255 - min(depth * 15, 255), 255 - min(depth * 15, 255))
                    pygame.draw.rect(screen, color, (ray * (WIDTH // NUM_RAYS), HEIGHT // 2 - wall_height // 2, WIDTH // NUM_RAYS, wall_height))
                    break


def draw():
    screen.fill(BLACK)
    cast_rays()
    pygame.display.flip()


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    draw()
    clock.tick(60)

pygame.quit()

