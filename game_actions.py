import pygame
import load_resources as res
from text_buttons import text_objects,button
import play_game as pg


def quit_game():
    pygame.quit()
    quit()

def paused():
    pygame.mixer.music.pause()

    while pg.pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        text_objects("Paused",120,res.yellow,res.display_width/2,res.display_height/2)
        button("Resume",res.blue,250,400,100,50,unpause)
        button("Quit",res.red,450,400,100,50,quit_game)

        pygame.display.update()

def unpause():

    pygame.mixer.music.unpause()
    pg.pause=False

