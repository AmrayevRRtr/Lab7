import pygame, math, datetime

pygame.init()

W, H = 800, 800
white = (255, 255, 255)
sc = pygame.display.set_mode((W,H), pygame.RESIZABLE)

clock = pygame.image.load('clock.png')
clock_rect = clock.get_rect()
minute_hand = pygame.image.load('minute.png')
second_hand = pygame.image.load('second.png')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # import datetime library and get exact minutes and seconds
    x = datetime.datetime.now()

    seconds = x.strftime('%S')
    minutes = x.strftime('%M')
    
    s = int(seconds)
    m = int(minutes)


    # calculate angles
    sec_angle = -math.radians(s * 6) + math.pi / 2 + 12
    min_angle = -math.radians(m * 6) + math.pi / 2 + 12

    # rotate the minute and second hands
    minute = pygame.transform.rotate(minute_hand, math.degrees(min_angle))
    second = pygame.transform.rotate(second_hand, math.degrees(sec_angle))


    minute_rect = minute.get_rect(center=clock_rect.center)
    second_rect = second.get_rect(center=clock_rect.center)

    sc.fill(white)
    sc.blit(clock, clock_rect)
    sc.blit(minute, minute_rect)
    sc.blit(second, second_rect)

    pygame.display.flip()