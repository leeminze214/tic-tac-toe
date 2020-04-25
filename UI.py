import pygame
import time
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])


running = True
while running:

\
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    if pygame.mouse.get_pressed()[0]:
        if pygame.mouse.get_pos()[0] >= 80 and pygame.mouse.get_pos()[1]>= 200:
            print("Inicio jogo")
            time.sleep(1)
    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    pygame.draw.rect(screen, (0,0,222),[1,100,2,200] )
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
