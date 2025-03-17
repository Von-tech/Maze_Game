# Maze Game

## Overview

Maze Game is a 3D raycasting-based maze exploration game built using SDL2 and Python (via Pygame). The game dynamically generates a solvable maze with a randomly placed exit and allows the player to navigate using smooth movement and wall rendering techniques.

## Features

- **Procedurally Generated Maze**: A new maze is generated each time with an entrance and a randomly placed exit.
- **Raycasting Rendering**: Walls are rendered in a 3D perspective using raycasting.
- **Smooth Player Movement**: Allows for forward, backward, strafing, and rotation.
- **Minimap**: Displays an overhead view of the maze with the player's position.
- **Textured Walls, Floor, and Ceiling**: Uses image textures to create a more immersive environment.

## Installation

### Requirements

- Python 3.12
- Pygame 2.6.1

### Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/Maze_Game.git
   cd Maze_Game
   ```
2. Install dependencies:
   ```sh
   pip install pygame
   ```
3. Run the game:
   ```sh
   python main.py
   ```

## Controls

- **W**: Move forward
- **S**: Move backward
- **A**: Strafe left
- **D**: Strafe right
- **Q**: Rotate left
- **E**: Rotate right

## Code Structure

```
Maze_Game/
├── main.py           # Entry point of the game
├── game.py           # Main game loop and event handling
├── maze.py           # Generates a random solvable maze
├── player.py         # Player movement and controls
├── raycasting.py     # Handles 3D rendering using raycasting
├── renderer.py       # Draws walls using raycasting calculations
├── settings.py       # Game settings and constants
└── textures/         # Folder for wall, floor, and ceiling textures
```

## How It Works

- **Maze Generation**: Uses depth-first search to create a path through the grid, ensuring that the maze is always solvable.
- **Raycasting**: Casts rays from the player's position to detect walls and determine their distance, which is then used to render a 3D perspective.
- **Player Movement**: Allows movement in all directions with collision detection against maze walls.
- **Minimap**: Displays a small-scale representation of the maze and updates as the player moves.

## Future Improvements

- Additional visual effects like lighting and shadows.
- More advanced textures and UI enhancements.
- Sound effects for movement and interactions.

## License

This project is open-source under the MIT License.

## Credits

Developed by [Vonzell S Carson]. Contributions and feedback are welcome!

 
