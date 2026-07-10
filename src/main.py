# Summer Game Project

import pygame
pygame.init()

def main():
    #Create Screen
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        screen.fill("black")
        pygame.draw.rect(screen,"white",(100,100,100,100),border_radius=5)

        pygame.display.flip()

        clock.tick(60)
        


    pygame.quit()

    #Create Buttons



main()