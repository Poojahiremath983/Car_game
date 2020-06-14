import pygame
pygame.init()



clock = pygame.time.Clock()

display_height = 600
display_width = 800

# Create pygame window
display_surface = pygame.display.set_mode((display_width,display_height)) 
pygame.display.set_caption('This is a Car Game')   

# Load images
road_img = pygame.image.load('resources/images/road1.jpg').convert_alpha()
start_img = pygame.image.load('resources/images/car.png').convert_alpha()
car_img = pygame.image.load('resources/images/1.png').convert_alpha()
opp_img1 = pygame.image.load('resources/images/2.png').convert_alpha()
opp_img2 = pygame.image.load('resources/images/3.png').convert_alpha()
opp_img3 = pygame.image.load('resources/images/4.png').convert_alpha()



opp_list = [opp_img1,opp_img2,opp_img3]

# Load music
pygame.mixer.music.load("resources/sounds/bg_music.mp3")
csound=pygame.mixer.Sound("resources/sounds/crash.wav")


# Colors in RGB
green = (230,255,205)   
black = (0,0,0)
yellow = (200,200,0)
blue = (81, 135, 168)
red = (212, 95, 95)
white= (255, 255, 255)