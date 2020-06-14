import pygame
import load_resources as res
from text_buttons import text_objects,button
from play_game import game_loop
from game_actions import quit_game
from end_game import crashed

pygame.init()

def game_intro():
    start = True

    while start:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
                quit_game()

        # Render image on the surface
        res.display_surface.blit(res.start_img, (0,0))

        text_objects("Eras Demi ITC","LETS RACE",100,res.red,400,200)
        text_objects("Eras Demi ITC","Ready Steady Go",50,res.red,400,300)

        button("GO",res.blue,250,400,100,50,game_loop)
        button("QUIT",res.red,450,400,100,50,quit_game)
        
        #Updates a portion of the display
        pygame.display.update()


if __name__ == '__main__':
    game_intro()
    quit()