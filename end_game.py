import pygame
import load_resources as res
from text_buttons import text_objects,button
import play_game as pg
from game_actions import quit_game


def crashed(count):
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(res.csound)
    res.display_surface.blit(res.start_img,(0,0))
    text_objects("Eras Demi ITC","You Crashed",100,res.red,400,200)

    text_objects("Eras Demi ITC","Final Score:"+str(count),40,res.red,400,300)

    while True:
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:
                quit_game()
                

        button("Play Again",res.blue,200,400,150,50,pg.game_loop)
        button("Quit",res.red,450,400,100,50,quit_game)

        pygame.display.update()