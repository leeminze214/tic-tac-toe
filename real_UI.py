import pygame
import time
import backend
import user
import bot
import os

pygame.init()
# Set up the drawing window
screen = pygame.display.set_mode([600, 600])

# for some reasons it cant access the images even tho its in the same folder
mydir = os.path.dirname('__file__')
pygame.image.load(os.path.join(mydir, 'tictac_O.png'))
pygame.image.load(os.path.join(mydir, 'tictac_X.png'))
X = pygame.transform.scale(screen, (150, 130))
O = pygame.transform.scale(screen, (150, 130))


def mouse_x_y():
    font = pygame.font.SysFont("comicsansms", 10)
    x, y = pygame.mouse.get_pos()
    text = font.render(f"{x},{y}", True, (0, 128, 0))
    screen.blit(text, (10, 10))


def quitt():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


# TODO def scoreboard():

class Rect:
    def __init__(self, name, x, y, width, height, row, col):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.row = row
        self.col = col
        self.the_box = pygame.draw.rect(screen, (255, 0, 255), [self.x, self.y, self.width, self.height], 5)

    def update_board(self):

        if user.Bob.turn:
            if self.the_box.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0]:
                    if backend.Board.taken_or_not(self.row, self.col) == "empty":
                        backend.Board.fill(self.row, self.col, user.Bob.symbol)
                        backend.Board.update_status_sym(self.name)
                        backend.Board.turns += 1

        else:  # TODO if its bots turn
            print("BOts turn now")
            # TODO RUN BOT ALGORITHm\
            # needs to turn on and off symbol update, plus one on turn, sleep.

    def draw_symbol(self):
        if backend.Board.symbols[self.name]:
            if user.Bob.symbol == "X":
                screen.blit(X, (self.x, self.y))
            else:
                screen.blit(O, (self.x, self.y))


'''         
            else:
                if bot.robot.symbol == "X":
                    screen.blit(X, (self.x, self.y))
                else:
                    screen.blit(O, (self.x, self.y))
'''

# picks randomly, who goes first
backend.Board.random_first()
running = True
while running:
    screen.fill((255, 255, 255))
    mouse_x_y()
    quitt()
    ev = pygame.event.get()
    print(backend.Board.turns)
    # the grid
    one = Rect("one", 70, 150, 150, 130, 0, 0)
    two = Rect("two", 220, 150, 150, 130, 0, 1)
    three = Rect("three", 370, 150, 150, 130, 0, 2)
    four = Rect("four", 70, 300, 150, 130, 1, 0)
    five = Rect("five", 220, 300, 150, 130, 1, 1)
    six = Rect("six", 370, 300, 150, 130, 1, 2)
    seven = Rect("seven", 70, 450, 150, 130, 2, 0)
    eight = Rect("eight", 220, 450, 150, 130, 2, 1)
    nine = Rect("nine", 370, 450, 150, 130, 2, 2)
    grid_list = [one, two, three, four, five, six, seven, eight, nine]
    [x.update_board() for x in grid_list]
    [x.draw_symbol() for x in grid_list]
    backend.Board.Turns()

    pygame.display.update()
pygame.quit()
