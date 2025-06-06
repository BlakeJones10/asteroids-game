# Asteroids Game

A classic Asteroids arcade game built with Python and Pygame.

## Description

This is a recreation of the classic Asteroids arcade game where you control a spaceship and shoot asteroids while avoiding collisions. The game features asteroid splitting mechanics, player shooting with cooldown, and collision detection.

## Features

- **Player Controls**: Move and rotate your spaceship with WASD keys
- **Shooting System**: Fire bullets with the spacebar (with cooldown to prevent spam)
- **Asteroid Physics**: Asteroids move across the screen and wrap around edges
- **Splitting Mechanics**: Large asteroids split into smaller ones when shot
- **Collision Detection**: Game ends when player collides with an asteroid
- **Sprite Groups**: Efficient game object management using Pygame sprite groups

## Controls

- **W**: Move forward
- **S**: Move backward  
- **A**: Rotate left
- **D**: Rotate right
- **Spacebar**: Shoot

## Game Objects

### Player
- Triangle-shaped spaceship that can move and rotate
- Has a shooting cooldown of 0.3 seconds
- Collision with asteroids ends the game

### Asteroids
- Circular objects that move across the screen
- Split into two smaller, faster asteroids when shot
- Smallest asteroids are destroyed completely when shot

### Shots
- Small white circles fired by the player
- Move in straight lines at high speed
- Destroyed on impact with asteroids

## Technical Details

### File Structure
- `main.py` - Main game loop and initialization
- `player.py` - Player class with movement and shooting
- `asteroid.py` - Asteroid class with splitting mechanics
- `shot.py` - Bullet/shot class
- `asteroidfield.py` - Manages asteroid spawning
- `circleshape.py` - Base class for circular collision detection
- `constants.py` - Game constants (screen size, speeds, etc.)

### Dependencies
- Python 3.x
- Pygame 2.x

## Installation

1. Make sure you have Python 3 installed
2. Install Pygame:
   ```bash
   pip install pygame
   ```
3. Run the game:
   ```bash
   python3 main.py
   ```

## Game Constants

The game behavior can be customized by modifying values in `constants.py`:

- `SCREEN_WIDTH`, `SCREEN_HEIGHT` - Display dimensions
- `PLAYER_SPEED`, `PLAYER_TURN_SPEED` - Player movement speeds
- `PLAYER_SHOOT_SPEED`, `PLAYER_SHOOT_COOLDOWN` - Shooting mechanics
- `ASTEROID_MIN_RADIUS`, `ASTEROID_MAX_RADIUS` - Asteroid sizes
- `ASTEROID_SPAWN_RATE` - How often new asteroids appear

## How to Play

1. Use WASD to move your triangular spaceship
2. Press spacebar to shoot at asteroids
3. Avoid colliding with asteroids (game over if you do)
4. Shoot large asteroids to split them into smaller ones
5. Destroy all asteroids to clear the area

## Future Enhancements

Potential improvements could include:
- Score system
- Multiple lives
- Power-ups
- Sound effects
- Levels with increasing difficulty
- High score persistence

## License

This project is for educational purposes.
