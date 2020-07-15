# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 19:09:18 2020

@author: Killer Instinct
"""
import pygame
import random
import math

pygame.init()

dis_width = 810
dis_height = 610
dis = pygame.display.set_mode((dis_width, dis_height))

pygame.display.set_caption("Snake Game")

Clock = pygame.time.Clock()

Bg = pygame.image.load("Background.png")
Sl = pygame.image.load("SnakeLogo.png")
Head = pygame.image.load("Head.png")
Tail = pygame.image.load("Tail.png")
Mid = pygame.image.load("Mid.png")
Food = pygame.image.load("Food.png")

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

    def draw(self, dis, snake_Part, snake_Body):

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
    dis.blit(Food, (foodx, foody))
    pygame.display.update()

def message(msg ,font_size, color , pos):
    font_style = pygame.font.SysFont( None , font_size)
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, pos)
    pygame.display.update()

def scoredraw(score):
    msg = "SCORE : " + str(score - 3)
    font_style = pygame.font.SysFont( "Ariel" , 30)    
    mesg = font_style.render(msg, True, (255,255,255))
    dis.blit(mesg, (0,0))
    pygame.display.update()
def redraw(dis):
    dis.blit(Bg,(0,0))
    
def StartScreen():
    dis.blit(Sl, (dis_width/2 - 200, 0))
    message("Snake" , 70, (23, 252, 3), (dis_width/2 - 70, 420))
    message("Press Enter To Start", 50, (143,250,3), (dis_width/2 - 160, 500))    
    pygame.display.update() 

def EndScreen(score):
     message("Game Over", 100, (161, 161, 161), (dis_width/2 - 210 , dis_height/2 -100) )
     message(" Press Enter to Try Again and Esc to Exit", 50 , (50,255,100), (dis_width/2 - 340, dis_height/2 + 50))
     last_score = "Your Score is : " +str(score - 3)
     message(last_score, 50, (255,255,255), (dis_width/2 - 170, dis_height/2))  

def Quit():     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True            
snake = Player(dis_height/2, dis_width/2, 20, 20)

def main_game():
    Game_quit = False
    Loss = False
    Start = False
    foodx = round(random.randrange(50, dis_width - 50))
    foody = round(random.randrange(50, dis_height - 50))
    snake_Body = []
    score = 3
    ang = 90
    redraw(dis)

    while not Game_quit:
        keys = pygame.key.get_pressed()
        
        Game_quit = Quit()
        
        if not Start:
            StartScreen()
            if keys[pygame.K_RETURN]:
                Start = True             

        if Loss:
           EndScreen(score)
           if keys[pygame.K_RETURN]:
              main_game()
           elif keys[pygame.K_ESCAPE]:
              Game_quit = True



        snake.x = dis_width/2
        snake.y = dis_height/2
        
        while Start and not Loss and not Game_quit :

            Clock.tick(20)
            Game_quit = Quit()  
            keys = pygame.key.get_pressed()        

            if keys[pygame.K_LEFT] and snake.x > 0:
                snake.x_change = -10
                snake.y_change = 0
                snake.left = True
                snake.right = False
                snake.up = False
                snake.down = False
                ang = -90
            elif keys[pygame.K_RIGHT] :
                snake.x_change = 10
                snake.y_change = 0
                snake.left = False
                snake.right = True
                snake.up = False
                snake.down = False
                ang = 90
            elif keys[pygame.K_UP] :
                snake.x_change = 0
                snake.y_change = -10
                snake.left = False
                snake.right = False
                snake.up = True
                snake.down = False
                ang = 180
            elif keys[pygame.K_DOWN] :
                snake.x_change = 0
                snake.y_change = 10
                snake.left = False
                snake.right = False
                snake.up = False
                snake.down = True
                ang = 0
                
            snake.x += snake.x_change
            snake.y += snake.y_change
            
            if snake.x < 0 or snake.x > dis_width - snake.width or snake.y < 0 or snake.y > dis_height - snake.height:
                Loss = True
            snake_Part = []
            snake_Part.append(snake.x)
            snake_Part.append(snake.y)
            snake_Part.append(Mid)
            snake_Part.append(ang)
            snake_Body.append(snake_Part) 

            if len(snake_Body) > score:
                del snake_Body[0]
            snake_x = snake.x
            snake_y = snake.y
            snake_x += snake.y_change    
            snake_y += snake.y_change
            headposx = snake_x
            headposy = snake_y 
            for track in snake_Body[:-1]:
                if track[0] == headposx and track[1] == headposy:
                    Loss = True
            snake.draw(dis, snake_Part, snake_Body,)        
            di = ((snake.x - foodx)**2) + ((snake.y - foody)**2)
            d = int(math.sqrt(di))
            fooddraw(foodx, foody) 

            if d < 40:
                foodx = round(random.randrange(50, dis_width - 50))
                foody = round(random.randrange(50, dis_height - 50))
                score += 1
                
            
            scoredraw(score)
            redraw(dis)

             
main_game()    
pygame.quit()    