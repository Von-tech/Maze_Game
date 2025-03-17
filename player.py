import pygame
import math

# Constants
MOVE_SPEED = 0.05
ROT_SPEED = 0.03

class Player:
    def __init__(self, x=1.5, y=1.5, angle=0):
        self.x = x
        self.y = y
        self.angle = angle

    def move(self, maze):
        keys = pygame.key.get_pressed()
        new_x, new_y = self.x, self.y
        
        if keys[pygame.K_w]:  # Move forward
            new_x += math.cos(self.angle) * MOVE_SPEED
            new_y += math.sin(self.angle) * MOVE_SPEED
        if keys[pygame.K_s]:  # Move backward
            new_x -= math.cos(self.angle) * MOVE_SPEED
            new_y -= math.sin(self.angle) * MOVE_SPEED
        if keys[pygame.K_a]:  # Rotate left
            self.angle -= ROT_SPEED
        if keys[pygame.K_d]:  # Rotate right
            self.angle += ROT_SPEED
        
        # Collision detection
        if maze[int(new_y)][int(new_x)] == 0:
            self.x, self.y = new_x, new_y

