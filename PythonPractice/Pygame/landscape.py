import pygame


pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

white = (255,255, 255)
yellow = (255,255,0)
light_yellow = (255,255,204)
green = (50,205,50)
dark_green = (34,139,34)
red = (255,0,0)
light_blue = (130, 205, 223)
black = (0,0,0)

sun_radius = 60
cloud_x = 210
cloud_y = 56
sun_x = 0
sun_y = 120
sun_y_speed = 0

# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # GAME STATE UPDATES
    # All game math and comparisons happen here
    radius = 40
    sun_radius -= 0.01

    cloud_x += 0.3
    sun_x += 1
    sun_y -= 0.2

    if sun_x >= WIDTH -20:
        running = False
    
    # DRAWING
    screen.fill((135, 206, 215))  # always the first drawing command

    # pygame.draw.rect(screen, (255, 0, 0), (0, 0, radius, radius))
    #sun
    pygame.draw.circle(screen, (255,255,0), (sun_x, sun_y), sun_radius)
    #cloud
    pygame.draw.circle(screen, white, (cloud_x, cloud_y), radius)
    pygame.draw.circle(screen, white, (cloud_x-33, cloud_y+22), radius)
    pygame.draw.circle(screen, white, (cloud_x+24, cloud_y+26), radius)
    #bush
    pygame.draw.ellipse(screen, dark_green, (-50, 180, 330, 300))
    pygame.draw.ellipse(screen, dark_green, (250, 200, 310, 400))
    pygame.draw.ellipse(screen, dark_green, (520, 180, 310, 400))
    #grass
    pygame.draw.rect(screen, green, (0, 350 ,WIDTH, 350))
    #rain
    # pygame.draw.line(screen, white, (50, 100), (80,130))
    pygame.draw.ellipse(screen, black, (200, 340, 10, 10))
    pygame.draw.ellipse(screen, black, (209, 342, 8, 8))
    pygame.draw.ellipse(screen, black, (216, 343, 12, 10))

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)       
    #---------------------------


pygame.quit()
