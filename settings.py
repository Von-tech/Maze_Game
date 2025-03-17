import math

# Screen settings
WIDTH, HEIGHT = 800, 600

# Raycasting settings
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 120
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20
TILE_SIZE = 40
SCALE = WIDTH // NUM_RAYS  # Defines the width of each vertical slice

