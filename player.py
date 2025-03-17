import pygame
import math

# Constants
MOVE_SPEED = 0.05
ROT_SPEED = 0.03

# Player starting position
PLAYER_START_X = 1.5
PLAYER_START_Y = 1.5
PLAYER_START_ANGLE = 0

class Player:
    def __init__(self, x=PLAYER_START_X, y=PLAYER_START_Y, angle=PLAYER_START_ANGLE):
        self.x = x
        self.y = y
        self.angle = angle

    def move(self, maze):
        keys = pygame.key.get_pressed()
        new_x, new_y = self.x, self.y
        
        # Forward / Backward Movement
        if keys[pygame.K_w]:  # Move forward
            new_x += math.cos(self.angle) * MOVE_SPEED
            new_y += math.sin(self.angle) * MOVE_SPEED
        if keys[pygame.K_s]:  # Move backward
            new_x -= math.cos(self.angle) * MOVE_SPEED
            new_y -= math.sin(self.angle) * MOVE_SPEED

        # Strafing (side movement)
        if keys[pygame.K_a]:  # Move left (strafe)
            new_x += math.sin(self.angle) * MOVE_SPEED
            new_y -= math.cos(self.angle) * MOVE_SPEED
        if keys[pygame.K_d]:  # Move right (strafe)
            new_x -= math.sin(self.angle) * MOVE_SPEED
            new_y += math.cos(self.angle) * MOVE_SPEED

        # Rotation (use Q/E for rotation instead of A/D)
        if keys[pygame.K_q]:  # Rotate left
            self.angle -= ROT_SPEED
        if keys[pygame.K_e]:  # Rotate right
            self.angle += ROT_SPEED
        
        # Collision detection
        if maze[int(new_y)][int(new_x)] == 0:
            self.x, self.y = new_x, new_y

