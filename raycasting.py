import pygame
import math
from settings import *

class Raycasting:
    def __init__(self, game):
        self.game = game
        self.wall_texture = pygame.image.load("textures/wall.png.jfif").convert()
        self.floor_texture = pygame.image.load("textures/floor.png.jfif").convert()
        self.ceiling_texture = pygame.image.load("textures/ceiling.png.jpg").convert()

    def render(self, screen):
        # Draw floor and ceiling
        screen.blit(pygame.transform.scale(self.ceiling_texture, (WIDTH, HEIGHT // 2)), (0, 0))
        screen.blit(pygame.transform.scale(self.floor_texture, (WIDTH, HEIGHT // 2)), (0, HEIGHT // 2))
        
        for ray in range(NUM_RAYS):
            angle = self.game.player.angle - HALF_FOV + ray * DELTA_ANGLE
            sin_a = math.sin(angle)
            cos_a = math.cos(angle)

            depth = 0
            hit = False
            while depth < MAX_DEPTH and not hit:
                depth += 0.1  # Increase depth in smaller increments for precision
                target_x = self.game.player.x + depth * cos_a
                target_y = self.game.player.y + depth * sin_a
                col, row = int(target_x), int(target_y)
                
                if 0 <= row < len(self.game.maze.get_maze()) and 0 <= col < len(self.game.maze.get_maze()[0]):
                    if self.game.maze.get_maze()[row][col] == 1:
                        hit = True
                        
                        wall_height = int(HEIGHT / (depth * math.cos(self.game.player.angle - angle)))
                        texture_x = int((target_x % 1) * self.wall_texture.get_width())
                        texture_x = max(0, min(self.wall_texture.get_width() - 1, texture_x))  # Clamp value
                        
                        wall_slice = self.wall_texture.subsurface((texture_x, 0, 1, self.wall_texture.get_height()))
                        wall_slice = pygame.transform.scale(wall_slice, (WIDTH // NUM_RAYS, wall_height))
                        
                        # Draw the textured wall
                        screen.blit(wall_slice, (ray * (WIDTH // NUM_RAYS), HEIGHT // 2 - wall_height // 2))
                        break

