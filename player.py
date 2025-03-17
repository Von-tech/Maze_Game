import pygame
import math
from maze import maze

# Constants
WIDTH, HEIGHT = 800, 600
FOV = math.pi / 3
NUM_RAYS = 120
MAX_DEPTH = 10
MOVE_SPEED = 0.05
ROT_SPEED = 0.03

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize player
player_x, player_y = 1.5, 1.5  # Start position
player_angle = 0

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Movement function
def move_player():
    global player_x, player_y, player_angle
    keys = pygame.key.get_pressed()
    new_x, new_y = player_x, player_y
    
    if keys[pygame.K_w]:
        new_x += math.cos(player_angle) * MOVE_SPEED
        new_y += math.sin(player_angle) * MOVE_SPEED
    if keys[pygame.K_s]:
        new_x -= math.cos(player_angle) * MOVE_SPEED
        new_y -= math.sin(player_angle) * MOVE_SPEED
    if keys[pygame.K_a]:
        player_angle -= ROT_SPEED
    if keys[pygame.K_d]:
        player_angle += ROT_SPEED
    
    # Collision detection
    if maze[int(new_y)][int(new_x)] == 0:
        player_x, player_y = new_x, new_y

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    move_player()
    
    screen.fill(BLACK)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

