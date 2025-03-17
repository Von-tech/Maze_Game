import pygame
import math
from settings import *

class Raycasting:
    def __init__(self, game):
        self.game = game  # Reference to Game class

    def render(self, screen):
        for ray in range(NUM_RAYS):
            angle = self.game.player.angle - HALF_FOV + ray * DELTA_ANGLE
            sin_a = math.sin(angle)
            cos_a = math.cos(angle)

            # Ray marching
            for depth in range(1, MAX_DEPTH):
                target_x = self.game.player.x + depth * cos_a
                target_y = self.game.player.y + depth * sin_a

                col, row = int(target_x), int(target_y)
                if 0 <= row < len(self.game.maze.maze) and 0 <= col < len(self.game.maze.maze[0]):
                    if self.game.maze.maze[row][col] == 1:
                        wall_height = int(HEIGHT / (depth + 0.1))
                        color = (255 - min(depth * 15, 255), 255 - min(depth * 15, 255), 255 - min(depth * 15, 255))
                        pygame.draw.rect(screen, color, (ray * (WIDTH // NUM_RAYS), HEIGHT // 2 - wall_height // 2, WIDTH // NUM_RAYS, wall_height))
                        break

