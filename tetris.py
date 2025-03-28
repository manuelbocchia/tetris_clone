import pygame
import time
import random
from my_tetris_class import change_shape, fall, m_left, m_right
#from game_loop import game_loop

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


move = ''

#sq_place = [window_x/2, 0]
def new_piece():
    return {'shape':random.choice(['S','Z','L','J','I','O']), 'place':(window_x/2), 'size' : 20, 'color' : random.choice(['white','blue','red','green']), 'loc':[[0,0],[0,0],[0,0],[0,0]], "full_size":0, "rotate":True}

#my_piece = new_piece()
my_piece = {'shape':'Z', 'place':(window_x/2), 'size' : 20, 'color' : random.choice(['white','blue','red','green']), 'loc':[[0,0],[0,0],[0,0],[0,0]], "full_size":0, "rotate":False}
change_shape(my_piece)

pieces_list = []



#game_loop(my_piece,game_window,window_x,window_y, game_speed)

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                my_piece = new_piece()
                change_shape(my_piece)
            if event.key == pygame.K_UP:
                #change_to = 'UP'
                if my_piece['rotate']:
                    my_piece['rotate'] = False
                    change_shape(my_piece)
                else:
                    my_piece['rotate'] = True
                    change_shape(my_piece)
            if event.key == pygame.K_DOWN:
                #change_to = 'DOWN'
                game_speed = game_speed*2
            if event.key == pygame.K_LEFT:
                #change_to = 'LEFT'
                if my_piece["loc"][0][0] != 0 and my_piece['loc'][3][1] < window_y - my_piece['full_size']:
                    m_left(my_piece)
            if event.key == pygame.K_RIGHT:
                #change_to = 'RIGHT'
                if my_piece["loc"][3][0] != window_x-my_piece['size'] and my_piece['loc'][3][1] < window_y - my_piece['full_size']:
                    m_right(my_piece)
            if event.key == pygame.K_ESCAPE:
                game_over()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                #change_to = 'DOWN'
                game_speed = game_speed/2

    game_window.fill(black)

    ## FALLING MECHANIC
    if my_piece['loc'][3][1] < window_y - my_piece['size']: #- my_piece['full_size']:
        fall(my_piece)
    ## IF PIECE REACHES THE BOTTOM
    if not my_piece['loc'][3][1] < window_y - my_piece['size']:
        pieces_list.append(my_piece)
        my_piece = new_piece()
        change_shape(my_piece)

    ## DRAWS ALL PIECES IN THE LIST
    for piece in pieces_list:
        for sq_place in piece['loc']:
            pygame.draw.rect(game_window, piece['color'], pygame.Rect(sq_place[0], sq_place[1], piece['size'], piece['size']))
    ## DRAWS CURRENT PIECE
    for sq_place in my_piece['loc']:
        pygame.draw.rect(game_window, my_piece['color'], pygame.Rect(sq_place[0], sq_place[1], my_piece['size'], my_piece['size']))

    pygame.display.update()
    fps.tick(game_speed)