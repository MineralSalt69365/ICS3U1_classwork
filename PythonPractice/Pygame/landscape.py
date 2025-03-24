import pygame
import random

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

#color
white = (255,255, 255)
yellow = (255,255,0)
light_yellow = (255,255,204)
green = (50,205,50)
dark_green = (34,139,34)
darker_green = (0, 51, 0)
red = (255,0,0)
light_blue = (130, 205, 223)
black = (0,0,0)
grey = (119,136,153)
brown = (102, 51, 0)
another_green = (0, 153, 51)

#variables
cloud_radius = 40
sun_radius = 60
cloud_x1 = 330
cloud_y1 = 100
cloud_x2 = 100
cloud_y2 = 70
cloud_x3 = 190
cloud_y3 = 90


sun_x = 0
sun_y = 120
sun_y_speed = 0


#ants!!!!!!!!!!
def draw_ant(x, y):
    pygame.draw.ellipse(screen, black, (x, y + 20, 10, 10))  
    pygame.draw.ellipse(screen, black, (x + 9, y + 22, 8, 8))  
    pygame.draw.ellipse(screen, black, (x + 16, y + 23, 12, 10)) 
    pygame.draw.line(screen, black, (x, y + 34), (x + 4, y + 30), 2) 
    pygame.draw.line(screen, black, (x + 15, y + 34), (x + 10, y + 28), 2)
    pygame.draw.line(screen, black, (x + 25, y + 36), (x + 20, y + 30), 2) 

ant_positions = [400 + a * 50 for a in range(5)]

#rain!!!
raindrops_num = 200
raindrops = []
#rain drop list
for i in range(raindrops_num):
    rain_x = random.randrange(0, WIDTH)
    rain_y = random.randrange(0, HEIGHT)
    rain_speed = random.randrange(1, 3)
    raindrops.append([rain_x,rain_y,rain_speed])

#boolean
running = True
sun_see = True
# ---------------------------

while running:
    screen.fill(light_blue)  # always the first drawing command
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # GAME STATE UPDATES
    #update raindrops


    if sun_x >= WIDTH // 2:
        sun_see = False
        screen.fill(grey)
    # if cloud_x1 == WIDTH or cloud_x2 == WIDTH：

    
    # All game math and comparisons happen here
    
    #animations
    if cloud_x1 <= 450:
        cloud_x1 += 0.9
    if cloud_x2 <= 210:
     cloud_x2 += 0.6
    if cloud_x3 <= 350:
        cloud_x3 += 0.7

    sun_x += 1
    sun_y -= 0.2
    
    # DRAWING
    
    #sun
    if sun_see == True:
        pygame.draw.circle(screen, (255,255,0), (sun_x, sun_y), sun_radius)
    #cloud1
    pygame.draw.circle(screen, white, (cloud_x1, cloud_y1), cloud_radius)
    pygame.draw.circle(screen, white, (cloud_x1-33, cloud_y1+22), cloud_radius)
    pygame.draw.circle(screen, white, (cloud_x1+24, cloud_y1+26), cloud_radius)
    #cloud2
    pygame.draw.circle(screen, white, (cloud_x2, cloud_y2), cloud_radius)
    pygame.draw.circle(screen, white, (cloud_x2-33, cloud_y2+22), cloud_radius)
    pygame.draw.circle(screen, white, (cloud_x2+24, cloud_y2+26), cloud_radius)
    #cloud2
    pygame.draw.circle(screen, white, (cloud_x3, cloud_y3), cloud_radius)
    pygame.draw.circle(screen, white, (cloud_x3-33, cloud_y3+22), cloud_radius)
    pygame.draw.circle(screen, white, (cloud_x3+24, cloud_y3+26), cloud_radius)
    #bush
    pygame.draw.ellipse(screen, dark_green, (-50, 180, 300, 400))
    pygame.draw.ellipse(screen, dark_green, (230, 180, 300, 400))
    pygame.draw.ellipse(screen, dark_green, (520, 180, 300, 400))
    
    #grass
    pygame.draw.rect(screen, green, (0, 350 ,WIDTH, 350))
    #mushroom1
    pygame.draw.rect(screen, white, (450, 300, 40, 60))
    pygame.draw.ellipse(screen, red, (430, 250, 80, 60))  
    pygame.draw.circle(screen, white, (450, 270), 10) 
    pygame.draw.circle(screen, white, (480, 260), 10)
    pygame.draw.circle(screen, white, (460, 290), 8)
    pygame.draw.circle(screen, white, (490, 285), 6)
    
    #ant
    for a in range(5):
        draw_ant(ant_positions[a], 350)  # Draw ant at current position
        ant_positions[a] -=0.5
        # draw_ant(400+x*50, 350)
    #tree
    pygame.draw.ellipse(screen, darker_green, (-80, -40, 280, 290))
    pygame.draw.rect(screen, brown, (30, 170, 60,250) )
    pygame.draw.circle(screen, red,(20, 50), 20 )
    pygame.draw.circle(screen, red,(130, 70), 20 )
    pygame.draw.circle(screen, red,(60, 120), 20 )
    pygame.draw.ellipse(screen, another_green, (-50, 320, 220, 190))
   
    #rains
    if sun_x >= WIDTH // 2:
        for drop in raindrops:
         #rain animations
            drop[1] += drop[2]

            if drop[1] > HEIGHT:
                drop[0] = random.randint(0, WIDTH)  
                drop[1] = random.randint(-20, -5)  
                drop[2] = random.randint(5, 10)  
        
            pygame.draw.line (screen, white, (drop[0], drop[1]), (drop[0], drop[1] + 10) )

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)       
    #---------------------------


pygame.quit()