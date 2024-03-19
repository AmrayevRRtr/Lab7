import pygame

pygame.init()

W, H = 600, 600
white = (255, 255, 255)
sc = pygame.display.set_mode((W, H), pygame.RESIZABLE) 

playlist = ['mb.mp3', 'Levelup2.mp3', 'First_time.mp3', 'vnezony.mp3', 'DDG.mp3']
current_song = -1
end_of_the_song = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(end_of_the_song)

font = pygame.font.SysFont('comicsansms', 28)
text = font.render("Firstly, press 'n' to start first song.", True, (0,0,0))
text2 = font.render("'b' - previous song,", True, (0,0,0))
text3 = font.render("'n' - next and 'space' - pause/unpause song" , True, (0,0,0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            # press space to pause the song
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            # press 'n' to start song firstly and then play next song
            elif event.key == pygame.K_n:
                current_song = (current_song + 1) % len(playlist)
                pygame.mixer.music.load(playlist[current_song])
                pygame.mixer.music.play()
            # press 'b' to play previous song
            elif event.key == pygame.K_b:
                current_song = (current_song - 1) % len(playlist)
                pygame.mixer.music.load(playlist[current_song])
                pygame.mixer.music.play()
        # to play next song after end of the previous
        elif event.type == pygame.USEREVENT + 1:
            current_song = (current_song + 1) % len(playlist)
            pygame.mixer.music.load(playlist[current_song])
            pygame.mixer.music.play()


                
    sc.fill(white)
    sc.blit(text,(30,50))
    sc.blit(text2, (30,90))
    sc.blit(text3, (30,130))
    pygame.display.update()



