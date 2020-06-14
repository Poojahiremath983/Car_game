import pygame
import random
import load_resources as res
from game_actions import quit_game,paused
from end_game import crashed
from text_buttons import text_objects

escaped = 0

def score(count):
    text_objects("Arial Black","Score:"+str(count),30,res.yellow,70,30)
    

def road(y1,y2):   
    y1 += 5

    if y1 > 0:
        res.display_surface.blit(res.road_img,(0,y1))
        y2 += 5
        res.display_surface.blit(res.road_img,(0,y2))

    # check if road images goes out of the window
    if y1 > 600:
        y1 = 0
        y2 = -600

    return y1,y2


def opponent(x,y,speed,img):
    global escaped
    res.display_surface.blit(img, (x,y))
    y += speed

    # check if opponent car goes out of the window
    if y > 600:
        x = random.randrange(0,800)
        y = -100
        img = random.choice(res.opp_list)
        escaped += 1
    
    return x,y,img


     
        
def game_loop():
    running = True

    global escaped,paused

    escaped = 0

    # Initialize position of road
    road_y1 = 0
    road_y2 = -600

    # Initialize position of our car
    car_x = 400
    car_y = 450

    

    x_change = 0
    y_change = 0

    # Initialize position of 3 opponent cars
    opp_x1 = random.randrange(0, res.display_width)
    opp_y1 = -500
    opp_x2 = random.randrange(0, res.display_width)
    opp_y2 = -600
    opp_x3 = random.randrange(0, res.display_width)
    opp_y3 = -700

    
    #Randomly choose image for opponent car from the list
    img1 = random.choice(res.opp_list)
    img2 = random.choice(res.opp_list)
    img3 = random.choice(res.opp_list)

    pygame.mixer.music.play(-1)

   



    
    while running:
        #pygame.time.delay(50)
    
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                quit_game()

            # Check for Key press
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5


                elif event.key == pygame.K_RIGHT:
                    x_change = 5

                elif event.key == pygame.K_UP:
                    y_change = -5

                elif event.key == pygame.K_DOWN:
                    y_change = 5

                elif event.key == pygame.K_p:
                    pause = True
                    paused()

            # Check for key release
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = 0


        # Update the position to move the Road
        road_y1, road_y2 = road(road_y1,road_y2)
        
        # Update the position of our car
        car_x = car_x + x_change
        car_y = car_y + y_change

       
        res.display_surface.blit(res.car_img,(car_x,car_y))


        #Update the position of opponent cars
        if opp_x1 != opp_x2 or opp_x1 != opp_x3 or opp_x2 != opp_x3:
            opp_x1,opp_y1,img1 = opponent(opp_x1,opp_y1,10,img1)
            opp_x2,opp_y2,img2 = opponent(opp_x2,opp_y2,12,img2)
            opp_x3,opp_y3,img3 = opponent(opp_x3,opp_y3,15,img3)
            
        pygame.display.update()
    

        score(escaped)
        
        car_width = res.car_img.get_size()[0]
        car_height = res.car_img.get_size()[1]

        opp_width = res.opp_img1.get_size()[0]
        opp_height = res.opp_img1.get_size()[1]

        # Check for Crash
        if car_x > res.display_width or car_x < 0 or car_y<0 or car_y>res.display_height:
            crashed()

        if car_y < opp_y1 + opp_height:   
           if car_x + car_width > opp_x1 and car_x < opp_x1 + opp_width:
                crashed(escaped)
        if car_y < opp_y2 + opp_height:   
           if car_x + car_width > opp_x2 and car_x < opp_x2 + opp_width:
                crashed(escaped)
        if car_y < opp_y3 + opp_height:   
           if car_x + car_width > opp_x3 and car_x < opp_x3 + opp_width:
                crashed(escaped)
        
        pygame.display.update() 
        res.clock.tick(60)  
      