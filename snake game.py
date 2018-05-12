import pygame
import os
import sys
import random
# COLOURS
black = 0,0,0
white = 255,255,255
red = (255, 0, 0)
greendark = (0, 128, 0)

# display
screen = pygame.display.set_mode((900, 600))
clock = pygame.time.Clock()

class Snake(pygame.sprite.Sprite):

    def __init__(self, screen):
        super(Snake, self).__init__()
        # initial length of snake
        self.length = 8
        self.speed = 1
        # x, and y coordinates of each block
        self.x = [450, 450, 450, 450, 450, 450, 450, 450]
        self.y = [300, 310, 320, 330, 340, 350, 360, 370]
        self.screen = screen
        
    def drawsnake(self):
        # draw each block
        for index in range (0, self.length):
            pygame.draw.rect(self.screen, black, (self.x[index], self.y[index],10,10), 1)
    def update_up(self):
        # set x and y coordinate upon move
        self.y[-1] = self.y[0]-10 
        self.x[-1] = self.x[0] 
        # place the coordinates at begining of list
        self.x.insert(0,self.x.pop())
        self.y.insert(0,self.y.pop())
    def update_right(self):
        self.y[-1] = self.y[0] 
        self.x[-1] = self.x[0]+10 
        self.x.insert(0,self.x.pop())
        self.y.insert(0,self.y.pop())
    def update_down(self):
        self.y[-1] = self.y[0]+10 
        self.x[-1] = self.x[0] 
        self.x.insert(0,self.x.pop())
        self.y.insert(0,self.y.pop())
    def update_left(self):
        self.y[-1] = self.y[0] 
        self.x[-1] = self.x[0]-10 
        self.x.insert(0,self.x.pop())
        self.y.insert(0,self.y.pop())        
        
class Food(pygame.sprite.Sprite):

    def __init__(self, screen):
        super(Food, self).__init__()
        # place food at random coordinates
        self.x = random.randrange(30, 840, 10)
        self.y = random.randrange(30, 540, 10)
        self.screen = screen
    def draw_food(self):       
        pygame.draw.rect(self.screen, black, (self.x, self.y,10,10), 0)
    
        
def main():
    snake = Snake(screen)
    food =Food(screen)
    play = True
    pressed_left =False
    pressed_up =False
    pressed_right =False
    pressed_down = False
    pygame.font.init() 
    screen.fill(black)
    intro = True
    start = True
    
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_RETURN      :  
                    intro = False           
        
        myfont = pygame.font.SysFont('Times New Roman',115)
        textsurf= myfont.render("Snakes", False, white)
        screen.blit(textsurf, (300, 200))
        pygame.draw.rect(screen, greendark,(200,450,100,50))
        pygame.draw.rect(screen, red,(600,450,100,50))        
        font = pygame.font.SysFont("Times New Roman", 50)
        screen.blit(font.render("Start", -1, (1, 1, 1)), (200, 440))
        font1 = pygame.font.SysFont("Times New Roman", 50)
        screen.blit(font1.render("Quit", -1, (1, 1, 1)), (600, 440)) 
        # outside of gameplay Use mouse to toggle
        mouse = pygame.mouse.get_pos()
        if 200+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450 and pygame.mouse.get_pressed()[0]:
            intro = False
        elif 600+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450 and pygame.mouse.get_pressed()[0]:
            pygame.quit()
            sys.exit()            
        
        pygame.display.update()
        clock.tick(15)        
    while play:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN: 
                pressed_left = False    
                pressed_up =False
                pressed_right =False
                pressed_down = False   
                start = False
                if event.key == pygame.K_LEFT:  
                    pressed_left = True    
                                        
                elif event.key == pygame.K_RIGHT:
                    pressed_right = True  
                                        
                elif event.key == pygame.K_UP:
                    pressed_up = True 
                                        
                elif event.key == pygame.K_DOWN:
                    pressed_down = True  
        
                   
                
        if pressed_left:
            snake.update_left()
        elif pressed_right:
            snake.update_right()            
        elif pressed_down:
            snake.update_down()
        elif pressed_up:
            snake.update_up()
        
        if food.x == snake.x[0] and food.y == snake.y[0]:
            pygame.draw.rect(food.screen, white, (food.x, food.y,10,10), 0)
            food.x = random.randrange(30, 840, 10)
            food.y = random.randrange(30, 540, 10)            
            if pressed_left:
                snake.x.append(snake.x[-1]-10)
                snake.y.append(snake.y[-1])
                snake.length+=1
            elif pressed_right:
                snake.x.append(snake.x[-1]+10)
                snake.y.append(snake.y[-1])
                snake.length+=1
                
            elif pressed_down:
                snake.x.append(snake.x[-1])
                snake.y.append(snake.y[-1]-10)
                snake.length+=1
                
            elif pressed_up:
                snake.x.append(snake.x[-1])
                snake.y.append(snake.y[-1]+10)
                snake.length+=1
        
        if(870<snake.x[0] or snake.x[0]<30 or snake.y[0]<30 or snake.y[0]>540):
            play = False
        pygame.draw.rect(screen, white, (30,30,840,540), 0)    
        snake.drawsnake()  
        food.draw_food()
        if(start):
            myfont = pygame.font.SysFont('Times New Roman',50)
            textsurf = myfont.render("Press  up arrow key to start", False, black)
            screen.blit(textsurf, (160, 145))         
        pygame.display.update()
        clock.tick(15) 
    end = True
    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()   
                                   
                                
            
        
        myfont = pygame.font.SysFont('Times New Roman',115)
        textsurf= myfont.render("Game Over", False, black)
        screen.blit(textsurf, (165, 160))
        pygame.draw.rect(screen, greendark,(200,450,100,50))
        pygame.draw.rect(screen, red,(600,450,100,50))        
        font = pygame.font.SysFont("Times New Roman", 35)
        screen.blit(font.render("Restart", -1, (1, 1, 1)), (200, 456))
        font1 = pygame.font.SysFont("Times New Roman", 35)
        screen.blit(font1.render("Quit", -1, (1, 1, 1)), (610, 455))        
        mouse = pygame.mouse.get_pos()     
        
        if 200+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450 and pygame.mouse.get_pressed()[0]:
            main()
        elif 600+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450 and pygame.mouse.get_pressed()[0]:
            pygame.quit()
            sys.exit()            
        
        pygame.display.update()
        clock.tick(15)                
if __name__ == '__main__':
    main()
        