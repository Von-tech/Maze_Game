import pygame
from raycasting import Raycasting
from maze import Maze

# Constants
WIDTH, HEIGHT = 800, 600

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def main():
    running = True
    maze = Maze(20, 15)  # Generate a 20x15 maze
    raycasting = Raycasting(maze)
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update and render
        screen.fill((0, 0, 0))
        raycasting.render(screen)
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()
 
