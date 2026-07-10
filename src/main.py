# Summer Game Project

import pygame
pygame.init()

def main():
    # Create Screen
    screen = pygame.display.set_mode((1530, 825))
    clock = pygame.time.Clock()
    running = True
    title_font = pygame.font.Font("src/files/BlackOpsOne-Regular.ttf",128)
    title = title_font.render("PC's Games", True, (0,50,255))

    right_arrow_coords = (1200,475)
    left_arrow_coords = (300,475)

    while running:
    
        screen.fill("black")
        
        #Title
        pygame.draw.rect(screen,"darkblue",(250,50,1000,150),width=8,border_radius=5)
        screen.blit(title, (340,50))
        
        #Game Placeholder Box
        pygame.draw.rect(screen,"gold", (450,350,600,300),width=8,border_radius=5)

        #Right Arrow
        x, y = right_arrow_coords
        pygame.draw.polygon(screen,"red",[right_arrow_coords,(x,y+25),(x+50,y+25),(x+50,y+40),(x+75,y+12.5),(x+50,y-15),(x+50,y)])

        #Left Arrow
        x,y = left_arrow_coords
        pygame.draw.polygon(screen,"red",[left_arrow_coords,(x,y+25),(x-50,y+25),(x-50,y+40),(x-75,y+12.5),(x-50,y-15),(x-50,y)])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                ex,ey = event.pos
                #Right Arrow Checking
                if ex >= 1100 and ex <= 1400:
                    if ey >= 450 and ey <= 525:
                        print("Right Arrow Clicked")
                
                #Left Arrow Checking
                if ex >= 175 and ex <= 325:
                    if ey >= 450 and ey <= 525:
                        print("Left Arrow Clicked")

        pygame.display.flip()

        clock.tick(60)
        


    pygame.quit()

    #Create Buttons



main()