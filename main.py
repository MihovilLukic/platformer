import pygame
from pygame.locals import *

pygame.init()

#set up the game window
screen_width = 800
screen_height = 600

WIN = pygame.display.set_mode((screen_width, screen_height))
WHITE = (255, 255, 255)

pygame.display.set_caption("IGRA!")

clock = pygame.time.Clock()

def draw_window():
    WIN.fill(WHITE)
    
    #draw game elements here
    pygame.display.update()


def draw_main_menu():
    WIN.fill(WHITE):

    #Draw menu elements

    pygame.display.update()


def handle_gameplay_input():
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                # Handle left movement
                player.move_left()
            elif event.key == K_RIGHT:
                # Handle right movement
                player.move_right()
            elif event.key == K_SPACE:
                # Handle jumping
                player.jump()


def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        #Handle user input for the main menu
        handle_gameplay_input()
        if in_main_menu:
            for evenet in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        #Start the game or to the lecel selection screen
                        in_main_menu = False
                    elif event.key == K_ESCAPE:
                        running = False

        elif in_level_selection:
            for evenet in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        in_level_selection = False
                    elif event.key == K_ESCAPE:
                        in_level_selection = False
                        in_main_menu = True
                    
            
                
        #update game logic

        if in_main_menu:
            draw_main_menu()
        elif in_level_selection:
            draw_level_selection()
        else:
            draw_gameplay()
                
        
        draw_window()
        clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    main()
