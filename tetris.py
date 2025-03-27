import pygame
import time
import random
from my_tetris_class import change_shape, fall, m_left, m_right

game_speed = 5

#window size
window_x = 200
window_y = 600


# defining colors
black = pygame.Color(0,0,0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# initialising pygame
pygame.init()

# initialise game window
pygame.display.set_caption('Vamos a Jugar al Tetris')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS controller
fps = pygame.time.Clock()

# block size

block_sz = 20, 20




def game_over():
    my_font = pygame.font.SysFont('times new roman', 10)

    game_over_surface = my_font.render('Thanks for playing!', 0, white)

    game_over_rect = game_over_surface.get_rect()

    game_over_rect.midtop = (window_x/2, window_y/4)

    game_window.blit(game_over_surface, game_over_rect)
    
    pygame.display.flip()

    time.sleep(1)

    pygame.quit()

    quit()


#lass pieces:
#   def __init__(self, shape = str, color = str, size = int) -> None:
#       self.shape = shape
#       self.place = 0
#       self.loc = [[self.place,size],[self.place,size],[self.place,size],[self.place,size]]
#       self.color = color
#       self.turn = False
#       self.size = size
#       self.full_size = size
#
#   def change_shape(self):
#       self.loc = [[self.place,self.size],[self.place,self.size],[self.place,self.size],[self.place,self.size]]
#       if self.shape == 'L':
#           self.loc[0] = self.loc[0]
#           self.loc[1][1] += self.size
#           self.loc[2][1] += self.size*2
#           self.loc[3][0] += self.size
#           self.loc[3][1] += self.size*2
#       if self.shape == 'O':
#           self.loc[0] = self.loc[0]
#           self.loc[1][0] += self.size
#           self.loc[2][1] += self.size
#           self.loc[3][0] += self.size
#           self.loc[3][1] += self.size
#       if self.shape == 'S':
#           self.loc[0] = self.loc[0]
#           self.loc[1][1] += self.size
#           self.loc[2][0] += self.size
#           self.loc[2][1] += self.size
#           self.loc[3][0] += self.size
#           self.loc[3][1] += self.size*2
#       if self.shape == 'SR':
#           self.loc[0][0] += self.size
#           self.loc[1][0] += self.size
#           self.loc[1][1] += self.size
#           self.loc[2][0] += self.size*2
#           self.loc[3][0] += self.size
#           self.loc[3][1] += self.size*2
#       if self.shape == 'LR':
#           self.loc[0][0] += self.size
#           self.loc[1][0] += self.size
#           self.loc[1][1] += self.size
#           self.loc[2][1] += self.size*2
#           self.loc[3][0] += self.size
#           self.loc[3][1] += self.size*2
#       if self.shape == "I":
#           self.loc[0] = self.loc[0]
#           self.loc[1][1] += self.size
#           self.loc[2][1] += self.size*2
#           self.loc[3][1] += self.size*3
#       
#       self.full_size = self.loc[3][1]
#   
#   def fall(self):
#       self.loc[0][1] += self.size
#       self.loc[1][1] += self.size
#       self.loc[2][1] += self.size
#       self.loc[3][1] += self.size
#
#   def draw(self):
#       self.fall()
#       for square in self.loc:
#           pygame.draw.rect(game_window, shape_1.color, pygame.Rect(square[0], square[1], self.size, self.size))
#       
#   
#   def m_right(self):
#       self.loc[0][0] += self.size
#       self.loc[1][0] += self.size
#       self.loc[2][0] += self.size
#       self.loc[3][0] += self.size
#
#   def m_left(self):
#       self.loc[0][0] -= self.size
#       self.loc[1][0] -= self.size
#       self.loc[2][0] -= self.size
#       self.loc[3][0] -= self.size




change_to = ''

sq_place = [window_x/2, 0]

my_piece = {'shape':'SR', 'place':0, 'size' : 20, 'color' : 'white', 'loc':[[0,0],[0,0],[0,0],[0,0]], "full_size":0}
change_shape(my_piece)
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
                m_left(my_piece)
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
                m_right(my_piece)
            if event.key == pygame.K_ESCAPE:
                game_over()

    game_window.fill(black)

    if my_piece['loc'][3][1] < window_y + my_piece['size']:
        fall(my_piece)

    for sq_place in my_piece['loc']:
        pygame.draw.rect(game_window, my_piece['color'], pygame.Rect(sq_place[0], sq_place[1], my_piece['size'], my_piece['size']))

    #shape_1 = pieces("O", blue, 20)
    #shape_1.change_shape()
    #
    #while shape_1.loc[3][1] < window_y:
    #    shape_1.draw()

    #shape_1.fall()
    #for square in shape_1.loc:
    #    pygame.draw.rect(game_window, shape_1.color, pygame.Rect(square[0], square[1], shape_1.size, shape_1.size))
    # piece movement
    # left with border collision
    if change_to == 'LEFT' and sq_place[0] > 0 and sq_place[1] != window_y - 20:
        sq_place[0] -= 20
        change_to = ''
    # right with border collision
    if change_to == 'RIGHT' and sq_place[0] < window_x - 20 and sq_place[1] != window_y - 20:
        sq_place[0] += 20
        change_to = ''
    # constantly falling
    if sq_place[1] < window_y - 20:
        sq_place[1] += 20
    pygame.display.flip()
    fps.tick(game_speed)