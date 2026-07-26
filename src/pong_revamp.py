#File for pong game

import pygame
pygame.init()

def pong_score_reader():
    with open("files/pong_single_scores.csv","r") as file:
        print()

def pong_menu():

    screen = pygame.display.set_mode((1530,825))
    running = True
    clock = pygame.time.Clock()
    title_font = pygame.font.Font("src/files/BlackOpsOne-Regular.ttf",60)
    title = title_font.render("Pong Revamped",True,"yellow")
    exit_text = title_font.render("Exit",True,"red")
    secondary_font = pygame.font.Font("src/files/BlackOpsOne-Regular.ttf",40)
    scoreboard_title_text = secondary_font.render("Single Player",True,"blue")
    scoreboard = secondary_font.render("Scoreboard",True,"blue")
    play_button_text1 = title_font.render("Play Regular 2P",True,"green")
    play_button_text2 = title_font.render("Play Singleplayer",True,"green")
    explanation_message = "This Version of \n Pong includes \n Powerups and \n abilities to \n spice up \n the timeless \n classic, Pong! \n There is also a \n Single Player \n Version which \n Only Uses \n P1 Controls"


    while running:

        screen.fill("black")
        
        #Title
        pygame.draw.rect(screen,"gold",(470,35,580,100),width=8,border_radius=5)
        screen.blit(title,(500,50))

        #Exit Button
        pygame.draw.rect(screen,(200,0,0),(50,35,200,100),width=8,border_radius=5)
        screen.blit(exit_text,(80,50))

        #Scoreboard
        pygame.draw.rect(screen,"darkblue",(1100,35,350,100),width=8,border_radius=5)
        screen.blit(scoreboard_title_text,(1125,40))
        screen.blit(scoreboard,(1130,75))
        pygame.draw.rect(screen,"darkblue",(1100,150,350,500),width=8,border_radius=5)

        #Play Buttons
        pygame.draw.rect(screen,"darkgreen",(470,200,580,150),width=8,border_radius=5)
        screen.blit(play_button_text1,(500,230))

        pygame.draw.rect(screen,"darkgreen",(470,400,580,150),width=8,border_radius=5)
        screen.blit(play_button_text2,(475,430))

        #Explanation Box
        pygame.draw.rect(screen,"darkblue",(50,150,350,500),width=8,border_radius=5)
        for line,x in enumerate(explanation_message.split(" \n ")):
            screen.blit(secondary_font.render(x,True,"blue"),(60,170+(line*35)))



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

pong_menu()