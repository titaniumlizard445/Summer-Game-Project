import pygame
pygame.init()
screen = pygame.display.set_mode((1530, 825))
clock = pygame.time.Clock()
running = True
curr = "main menu"
font = pygame.font.Font("src/files/BlackOpsOne-Regular.ttf",128)

def main():
    title = font.render("BRIDGE", True, (0,50,255))

    while running:
        for event in pygame.event.get():
            if event == pygame.QUIT():
                running = False

        match curr:
            case "main menu":
                main_menu()
            # case settings:

            case _:
                print("Invalid value given for match case (" + curr + "). Changed back to main menu.")
                curr = "main menu"







        pygame.display.flip()
        clock.tick(60) # limit fps to 60
    
    # quit if not running            
    pygame.QUIT()




def main_menu():
    screen.fill("black")
    

    
    











main()


