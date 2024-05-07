import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((600, 400))

# Define snake properties
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_speed = 10

# Game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the snake
    snake_pos[0] += snake_speed
    snake_body.insert(0, list(snake_pos))

    # Check if the snake has eaten something
    # If not, remove the last segment
    if len(snake_body) > 0:
        snake_body.pop()

    # Draw everything
    screen.fill((0, 0, 0))
    for pos in snake_body:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(pos[0], pos[1], 10, 10))

    # Refresh the screen
    pygame.display.flip()
    pygame.time.Clock().tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
