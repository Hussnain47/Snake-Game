# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 19:09:18 2020

@author: Killer Instinct
"""
import pygame
import random
import math

pygame.init()
pygame.font.init()
dis_width = 810
dis_height = 610
dis = pygame.display.set_mode((dis_width, dis_height))

pygame.display.set_caption("Snake Game")

Clock = pygame.time.Clock()

Bg = pygame.image.load("image\Background.png")
Sl = pygame.image.load("image\SnakeLogo.png")
Head = pygame.image.load("image\Head.png")
Mid = pygame.image.load("image\Mid.png")
Food = pygame.image.load("image\Food.png")

class Player(object):

    def __init__(self,x,y,height,width):    
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.x_change = 10
        self.y_change = 0
        self.left = False
        self.right = True
        self.up = False
        self.down = False
        self.Start = False
        self.ang = 90
        self.vel = 10

    def draw_snake(self, dis, snake_Part, snake_Body):
        """
        This Method is used to display the snake on the screen 
        
        """
        for x in snake_Body:
            if self.left:
                direction = pygame.transform.rotate(x[2], x[3])             
                dis.blit(direction, (x[0], x[1]))
            elif self.right:
                direction = pygame.transform.rotate(x[2], x[3])               
                dis.blit(direction, (x[0], x[1]))
            elif self.up:
                direction = pygame.transform.rotate(x[2], x[3])           
                dis.blit(direction, (x[0], x[1]))
            elif self.down:
                direction = pygame.transform.rotate(x[2], x[3]) 
                dis.blit(direction, (x[0], x[1]))
        if self.left:
            x1 = self.x + self.x_change - 10
            y1 = self.y + self.y_change - 10
            hdir = pygame.transform.rotate(Head, -90)
            dis.blit(hdir, (x1,y1))
        elif self.right:
            x1 = self.x + self.x_change - 10
            y1 = self.y + self.y_change - 10
            hdir = pygame.transform.rotate(Head, 90)
            dis.blit(hdir, (x1,y1))
        elif self.up:
            x1 = self.x + self.x_change - 10
            y1 = self.y + self.y_change - 10
            hdir = pygame.transform.rotate(Head, 180)
            dis.blit(hdir, (x1,y1))
        elif self.down:
            x1 = self.x + self.x_change - 10
            y1 = self.y + self.y_change - 10
            hdir = pygame.transform.rotate(Head, 0)
            dis.blit(hdir, (x1,y1))    

        pygame.display.update            

def fooddraw(foodx, foody):
    """
    This Function Displays the Food
    """
    dis.blit(Food, (foodx, foody))
    pygame.display.update()

def message(msg ,font_size, color , pos):
    """
    This Function Shows a message on the screen
    """
    font_style = pygame.font.SysFont( "Times New Roman" , font_size)
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, pos)
    pygame.display.update()
    
def Movement():    
    """
    This Function is used to control the Movement of the Snake
    
    """
    keys = pygame.key.get_pressed()
                
    if keys[pygame.K_LEFT] and not snake.ang==90:
        snake.x_change = -snake.vel
        snake.y_change = 0
        snake.left = True
        snake.right = False
        snake.up = False
        snake.down = False
        snake.ang = -90
    elif keys[pygame.K_RIGHT] and not snake.ang==-90:
        snake.x_change = snake.vel
        snake.y_change = 0
        snake.left = False
        snake.right = True
        snake.up = False
        snake.down = False
        snake.ang = 90
    elif keys[pygame.K_UP] and not snake.ang==0:
        snake.x_change = 0
        snake.y_change = -snake.vel
        snake.left = False
        snake.right = False
        snake.up = True
        snake.down = False
        snake.ang = 180
    elif keys[pygame.K_DOWN] and not snake.ang==180:
        snake.x_change = 0
        snake.y_change = snake.vel
        snake.left = False
        snake.right = False
        snake.up = False
        snake.down = True
        snake.ang = 0
    

def scoredraw(score):
    """
    This Function Shows the current Score of the Player

    """
    msg = "SCORE : " + str(score - 4)
    font_style = pygame.font.SysFont( "Microsoft Sans Serif" , 30)    
    mesg = font_style.render(msg, True, (255,255,255))
    dis.blit(mesg, (10,10))
    pygame.display.update()
    
def redraw(dis):
    """
    This Function draws The Background of the Game

    """
    dis.blit(Bg,(0,0))
    
def Distance(foodx,foody):
    """
    This Function Calculates distance between Food and Snake
    
    """   
    di = ((snake.x - foodx)**2) + ((snake.y - foody)**2)
    d = int(math.sqrt(di)) 
    return d
    
def StartScreen():
    """
    This Function Shows the Start screen at the Start of the Game

    """
    dis.blit(Sl, (dis_width/2 - 200, 0))
    message("Snake" , 90, (23, 252, 3), (dis_width/2 - 100, 400))
    message("Press Enter To Start", 50, (143,250,3), (dis_width/2 - 190, 500))    
    pygame.display.update() 

def EndScreen(score):
    """
    This function Show an End Screen If Player Losses the Game 
    
    """
    message("Game Over", 100, (255, 16, 16), (dis_width/2 - 210 , dis_height/2 -100) )
    message(" Press Enter to Try Again and Esc to Exit", 30 , (50,255,100), (dis_width/2 - 250, dis_height/2 + 50))
    last_score = "Your Score is : " +str(score - 4)
    message(last_score, 50, (255,255,255), (dis_width/2 - 170, dis_height/2))  

def Quit():    
    """
    If the user presses the close button in the Title Bar This Function Closes the Game

    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True       
        
        
        
snake = Player(dis_height/2, dis_width/2, 20, 20)

def main_game():
    """
    Main_Game function which includes all the functions and commands to run the game

    Returns
    -------
    None.

    """
    #All the initial perimeters required to Run the Game
    Game_quit = False
    Loss = False
    foodx = round(random.randrange(50, dis_width - 50))
    foody = round(random.randrange(50, dis_height - 50))
    snake_Body = []
    score = 4
    redraw(dis)

    while not Game_quit:
        
        keys = pygame.key.get_pressed()
        
        Game_quit = Quit()
        
        if not snake.Start: 
            StartScreen()
            if keys[pygame.K_RETURN]:
                snake.Start = True             

        if Loss:
            
           EndScreen(score)
           
           if keys[pygame.K_RETURN]:
              main_game()
           
           elif keys[pygame.K_ESCAPE]:
              Game_quit = True

        snake.x = dis_width/2
        snake.y = dis_height/2
        #Playing Game......
        while snake.Start and not Loss and not Game_quit :

            Clock.tick(20)
            Game_quit = Quit()  
        

            Movement()
                
            snake.x += snake.x_change
            snake.y += snake.y_change
            
            if snake.x < 0 or snake.x > dis_width - snake.width or snake.y < 0 or snake.y > dis_height - snake.height:
                Loss = True
                
            #For Drawing Snake Body having different x and y with each part of snake  
            
            snake_Part = []
            snake_Part.append(snake.x)
            snake_Part.append(snake.y)
            snake_Part.append(Mid)
            snake_Part.append(snake.ang)
            snake_Body.append(snake_Part) 

            if len(snake_Body) > score:
                
                del snake_Body[0]
                
            #For Drawing the Head of the snake
            
            snake_x = snake.x
            snake_y = snake.y
            snake_x += snake.x_change    
            snake_y += snake.y_change
            headposx = snake_x
            headposy = snake_y 
            
            #Collision Detection between head and body
            
            for track in snake_Body[:-1]:
            
                if track[0] == headposx and track[1] == headposy:
                    Loss = True
            
            snake.draw_snake(dis, snake_Part, snake_Body)    
            fooddraw(foodx, foody) 
            
            d = Distance(foodx,foody)
            #Collision Detection between Snake and the Food
            if d < 40:
                foodx = round(random.randrange(50, dis_width - 50))
                foody = round(random.randrange(50, dis_height - 50))
                score += 1
                        
            scoredraw(score)
            redraw(dis)

             
main_game()    
pygame.quit()    