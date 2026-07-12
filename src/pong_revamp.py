#File for pong game

import pygame
pygame.init()


def pong_menu():

    screen = pygame.display.set_mode((1530,825))
    running = True
    clock = pygame.time.Clock()
    title_font = pygame.font.Font("src/files/BlackOpsOne-Regular.ttf",60)
    title = pygame

    while running:
        screen.fill("black")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

pong_menu()