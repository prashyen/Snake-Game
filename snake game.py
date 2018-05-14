import pygame
import sys
import random
# COLOURS
black = 0, 0, 0
white = 255, 255, 255
red = (255, 0, 0)
greendark = (0, 128, 0)

# display
screen = pygame.display.set_mode((900, 600))
clock = pygame.time.Clock()


class Snake(pygame.sprite.Sprite):

    '''A class representing the snake'''

    def __init__(self, screen):
        super(Snake, self).__init__()
        # initial length of snake
        self.length = 3
        # x, and y coordinates of each block of the snake
        self.x = [450, 450, 450]
        self.y = [300, 310, 320]
        self.screen = screen

    def drawsnake(self):
        # draw each block by loop through the x and y coordinates in the list
        for index in range(0, self.length):
            pygame.draw.rect(self.screen, black, (
                self.x[index], self.y[index], 10, 10), 1)

    def update_up(self):
        '''(Snake) -> Nonetype
        Alters the last y coordinate in the list by 10 pixels above the y
        coordinate of the first element in the y coordinate list, and
        removes the last x coordinate and places it at the front of the list
        '''
        # set last y coordinate to be  10 less than first y coordinate
        self.y[-1] = self.y[0] - 10
        # set last x coordinate to be equal to first
        self.x[-1] = self.x[0]
        # place the last coordinates at begining of list
        self.x.insert(0, self.x.pop())
        self.y.insert(0, self.y.pop())

    def update_right(self):
        '''(Snake) -> Nonetype
        Alters the last x coordinate in the list by 10 pixels right of the x
        coordinate of the first element in the x coordinate list, and removes
        the last y coordinate and places it at the front of the list
        '''
        # set last y coordinate to be equal to first
        self.y[-1] = self.y[0]
        # set last x coordinate to be  10 more than first x coordinate
        self.x[-1] = self.x[0] + 10
        # place the last coordinates at begining of list
        self.x.insert(0, self.x.pop())
        self.y.insert(0, self.y.pop())

    def update_down(self):
        '''(Snake) -> Nonetype
        Alters the last y coordinate in the list by 10 pixels below the y
        coordinate of the first element in the y coordinate list, and removes
        the last x coordinate and places it at the front of the list
        '''
        # set last y coordinate to be  10 more than first y coordinate
        self.y[-1] = self.y[0] + 10
        # set last x coordinate to be equal to first
        self.x[-1] = self.x[0]
        # place the last coordinates at begining of list
        self.x.insert(0, self.x.pop())
        self.y.insert(0, self.y.pop())

    def update_left(self):
        '''(Snake) -> Nonetype
        Alters the last x coordinate in the list by 10 pixels left of the
        x coordinate of the first element in the x coordinate list, and
        removes the last y coordinate and places it at the front of the list
        '''
        # set last y coordinate to be equal to first
        self.y[-1] = self.y[0]
        # set last x coordinate to be 10 less than first x coordinate
        self.x[-1] = self.x[0] - 10
        # place the last coordinates at begining of list
        self.x.insert(0, self.x.pop())
        self.y.insert(0, self.y.pop())


class Food(pygame.sprite.Sprite):

    def __init__(self, screen):
        super(Food, self).__init__()
        # place food at random coordinates
        # choose x,y coordinate to be random int that are multiples of 10 and
        # appear within white rectangel on the screen
        self.x = random.randrange(30, 840, 10)
        self.y = random.randrange(30, 540, 10)
        self.screen = screen

    def draw_food(self):
        # draw the food 10x10 pixel block based on the x,y coordinate
        pygame.draw.rect(self.screen, black, (self.x, self.y, 10, 10), 0)


def main():
    snake = Snake(screen)
    food = Food(screen)
    # no keys are  initially pressed
    pressed_left = False
    pressed_up = False
    pressed_right = False
    pressed_down = False
    # to access font methods
    pygame.font.init()
    # sset creen background to black
    screen.fill(black)
    # initially intro is open and true, and it is the start of the game
    start = True
    intro = True
    while intro:
        # determine all the keys pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and
                                             event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            # if enter is pressed, game is started
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    intro = False
        # game title
        myfont = pygame.font.SysFont('Times New Roman', 115)
        textsurf = myfont.render("Snakes", False, white)
        screen.blit(textsurf, (300, 200))
        # start button
        pygame.draw.rect(screen, greendark, (200, 450, 100, 50))
        font = pygame.font.SysFont("Times New Roman", 50)
        screen.blit(font.render("Start", -1, (1, 1, 1)), (200, 440))
        # quit button
        pygame.draw.rect(screen, red, (600, 450, 100, 50))
        font1 = pygame.font.SysFont("Times New Roman", 50)
        screen.blit(font1.render("Quit", -1, (1, 1, 1)), (600, 440))
        # main menu use mouse to select start or quit
        mouse = pygame.mouse.get_pos()
        # if start button is pressed using mouse, start game
        if (200 + 100 > mouse[0] > 150 and 450 + 50 > mouse[1] > 450 and
                pygame.mouse.get_pressed()[0]):
            intro = False
        # if quit button is pressed using mouse, exit game
        elif (600 + 100 > mouse[0] > 150 and 450 + 50 > mouse[1] > 450 and
              pygame.mouse.get_pressed()[0]):
            pygame.quit()
            sys.exit()
        # update display
        pygame.display.update()
        clock.tick(15)

    play = True
    # enter playing mode
    while play:
        # determine key pressed, execute the specific if statement
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # when new key is pressed, previous movements are stopped
                pressed_left = False
                pressed_up = False
                pressed_right = False
                pressed_down = False
                # when the key the pressed it is no longer the
                # start of the game
                start = False
                # set the key that was pressed to be true, so snake continues
                # to move in that direction until next key pressed
                if event.key == pygame.K_LEFT:
                    pressed_left = True

                elif event.key == pygame.K_RIGHT:
                    pressed_right = True

                elif event.key == pygame.K_UP:
                    pressed_up = True

                elif event.key == pygame.K_DOWN:
                    pressed_down = True
        # execute the snake method based on the key that was pressed
        if pressed_left:
            snake.update_left()
        elif pressed_right:
            snake.update_right()
        elif pressed_down:
            snake.update_down()
        elif pressed_up:
            snake.update_up()
        # when snake eats food
        if food.x == snake.x[0] and food.y == snake.y[0]:
            # remove/cover up the old food block
            pygame.draw.rect(food.screen, white, (food.x, food.y, 10, 10), 0)
            # choose coordinates for the new food block at random
            food.x = random.randrange(30, 840, 10)
            food.y = random.randrange(30, 540, 10)
            # based on the direction of the current state add a the x, y
            # coordinates to their respective list to make snake bigger
            # by 1 block
            if pressed_left:
                snake.x.append(snake.x[-1] - 10)
                snake.y.append(snake.y[-1])
                snake.length += 1
            elif pressed_right:
                snake.x.append(snake.x[-1] + 10)
                snake.y.append(snake.y[-1])
                snake.length += 1

            elif pressed_down:
                snake.x.append(snake.x[-1])
                snake.y.append(snake.y[-1] - 10)
                snake.length += 1

            elif pressed_up:
                snake.x.append(snake.x[-1])
                snake.y.append(snake.y[-1] + 10)
                snake.length += 1
        # if snake goes out of white square
        if(870 < snake.x[0] or snake.x[0] < 30 or snake.y[0] < 30 or
           snake.y[0] > 540):
            play = False
        # draw a white rectangle to present the  playing stadium
        pygame.draw.rect(screen, white, (30, 30, 840, 540), 0)
        # draw snake and food
        snake.drawsnake()
        food.draw_food()
        # if start of game and no arrow keys pressed
        if(start):
            # inform user to strike up arrow key to start game
            myfont = pygame.font.SysFont('Times New Roman', 50)
            textsurf = myfont.render(
                "Press  up arrow key to start", False, black)
            screen.blit(textsurf, (160, 145))
        pygame.display.update()
        clock.tick(15)
    # end of game menu
    end = True
    while end:
        # if exited
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and
                                              event.key == pygame.K_ESCAPE)):
                pygame.quit()
                sys.exit()
        # game over message
        myfont = pygame.font.SysFont('Times New Roman', 115)
        textsurf = myfont.render("Game Over", False, black)
        screen.blit(textsurf, (165, 160))
        # restart button
        pygame.draw.rect(screen, greendark, (200, 450, 100, 50))
        font = pygame.font.SysFont("Times New Roman", 35)
        screen.blit(font.render("Restart", -1, (1, 1, 1)), (200, 456))
        # quit button
        pygame.draw.rect(screen, red, (600, 450, 100, 50))
        font1 = pygame.font.SysFont("Times New Roman", 35)
        screen.blit(font1.render("Quit", -1, (1, 1, 1)), (610, 455))

        # use mouse to strike restart or quit button
        mouse = pygame.mouse.get_pos()

        if (200 + 100 > mouse[0] > 150 and 450 + 50 > mouse[1] > 450 and
                pygame.mouse.get_pressed()[0]):
            main()
        elif (600 + 100 > mouse[0] > 150 and 450 + 50 > mouse[1] > 450 and
              pygame.mouse.get_pressed()[0]):
            pygame.quit()
            sys.exit()

        pygame.display.update()
        clock.tick(15)
if __name__ == '__main__':
    main()
