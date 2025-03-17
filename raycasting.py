import pygame
import math
from settings import *

class Raycasting:
    def __init__(self, game):
        self.game = game  # Store reference to the game instance

    def render(self, screen):
        for ray in range(NUM_RAYS):
            angle = self.game.player.angle - HALF_FOV + ray * DELTA_ANGLE
            depth = 0
            hit = False
            sin_a = math.sin(angle)
            cos_a = math.cos(angle)
            
            while not hit and depth < MAX_DEPTH:
                depth += 0.1
                target_x = self.game.player.x + depth * cos_a
                target_y = self.game.player.y + depth * sin_a
                
                if self.game.maze.get_maze()[int(target_y)][int(target_x)] == 1:
                    hit = True
                    depth *= math.cos(self.game.player.angle - angle)  # Fix fisheye effect

            wall_height = min(int(HEIGHT / (depth + 0.1)), HEIGHT)
            color_intensity = 255 - min(int(depth * 15), 255)
            color = (color_intensity, color_intensity, color_intensity)
            
            SCALE = WIDTH // NUM_RAYS  # Define SCALE correctly
            pygame.draw.rect(screen, color, (ray * SCALE, HEIGHT // 2 - wall_height // 2, SCALE, wall_height))

