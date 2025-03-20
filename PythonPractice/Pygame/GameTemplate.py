# pygame template

import pygame


pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

circle_x = 200
circle_y = 200
circle_x_speed = 5
circle_y_speed = 0
circle_radius = 70
# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # GAME STATE UPDATES
    # All game math and comparisons happen here
    circle_y_speed += 0.4
    circle_x += circle_x_speed
    circle_y += circle_y_speed

    if circle_y >= HEIGHT - circle_radius:
        circle_y_speed *= -1

    if circle_x >= WIDTH + circle_radius:
        circle_x = -circle_radius

    # DRAWING
    screen.fill((135, 206, 215))  # always the first drawing command

    pygame.draw.circle(screen, (255, 255, 255), (circle_x, circle_y), circle_radius)

    radius = 200
    pygame.draw.rect(screen, (255, 0, 0), (0, 0, radius, radius))
    pygame.draw.circle(screen, (0, 0, 0), (0, 0), radius)


    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()