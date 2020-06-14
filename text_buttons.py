import pygame
from load_resources import display_surface,white

pygame.init()

def text_objects(font,text,size,color,x,y):

    # Create font object
    my_font  = pygame.font.SysFont(font,size)
    # Create a text surface
    my_text = my_font.render(text, True, color)
    # Get rectangle from the text surface
    text_rect = my_text.get_rect(center = (x,y))

    display_surface.blit(my_text, text_rect)


def button(text,color,x,y,width,height,action=None):
    # rect(surface,color,(x,y,width,height))
    button_rect = pygame.draw.rect(display_surface,color,(x,y,width,height))
    text_objects("Arial Black",text,20,white,x+(width/2), y+(height/2))

    # Get the position of mouse or cursor
    mouse_pos = pygame.mouse.get_pos()   # It returns (x,y)
    
    mouse_click = pygame.mouse.get_pressed()
    
    # Check if the point is within the rectangle (Button)
    if button_rect.collidepoint(mouse_pos[0],mouse_pos[1]):
        if mouse_click[0] == 1 and action != None:
            action()