import pygame
pygame.init()

W, H = 600, 400
WHITE = (255, 255, 255)
RED = (255, 0, 0)

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("My first pygame project!")
pygame.display.set_icon(pygame.image.load("pacman.svg"))

clock = pygame.time.Clock()
FPS = 60

x = W / 10
y = H / 10
radius = 25
speed = 5
flLeft = flRight = flUp = flDown = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: 
                flLeft = True
            elif event.key == pygame.K_RIGHT:
                flRight = True
            elif event.key == pygame.K_UP:
                flUp = True
            elif event.key == pygame.K_DOWN:
                flDown = True
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                flLeft = flRight = flUp = flDown = False         
    
    if flLeft and x - speed >= 0:  
        x -= speed
    elif flRight and x + radius*2 + speed <= W:  
        x += speed
    elif flUp and y - speed >= 0: 
        y -= speed
    elif flDown and y + radius*2 + speed <= H:  
        y += speed
    
    sc.fill(WHITE)
    pygame.draw.circle(sc, RED, (x + radius, y + radius), radius)
    pygame.display.update()
            
    clock.tick(FPS)