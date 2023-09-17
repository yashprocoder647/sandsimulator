
import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)
SAND_COLOR = (194, 178, 128)
SAND_SIZE = 5

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sand Simulator")

# Sand grid
sand = [[0] * WIDTH for _ in range(HEIGHT)]

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Create sand particles at the top of the screen
    for x in range(WIDTH):
        if random.random() < 0.2:
            sand[0][x] = 1

    # Simulate sand falling
    for y in range(HEIGHT - 2, -1, -1):
        for x in range(1, WIDTH - 1):
            if sand[y][x] == 1:
                if sand[y + 1][x] == 0:
                    sand[y][x] = 0
                    sand[y + 1][x] = 1
                elif sand[y + 1][x - 1] == 0 or sand[y + 1][x + 1] == 0:
                    direction = random.choice([-1, 1])
                    sand[y][x] = 0
                    sand[y + 1][x + direction] = 1

    # Draw sand particles
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if sand[y][x] == 1:
                pygame.draw.circle(screen, SAND_COLOR, (x, y), SAND_SIZE)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    pygame.time.delay(10)

# Quit Pygame
pygame.quit()
