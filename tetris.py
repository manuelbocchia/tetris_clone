import pygame
import time
import random
from my_tetris_class import change_shape, fall, m_left, m_right
#from game_loop import game_loop

game_speed = 15

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

#def paused_screen():


def new_piece():
    return {'shape':random.choice(['S','Z','L','J','I','O']), 
            'place':(window_x/2), 
            'size' : 20, 
            'color' : random.choice(['white','blue','red','green']), 
            'loc':[[0,0],[0,0],[0,0],[0,0]], 
            'full_size':0, 
            'rotate':1}

#my_piece = new_piece()

my_piece = {'shape':'J', 'place':(window_x/2), 
            'size' : 20, 
            'color' : random.choice(['white','blue','red','green']), 
            'loc':[[0,0],[0,0],[0,0],[0,0]], 
            "full_size":0, 
            "rotate":1}


change_shape(my_piece)
## pieces that are no longer playing
pieces_list = []
## coordenates of each piece for better accessing
pieces_places = []

game_state = 'RUNNING'

while True:


    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            ## special keys for debugging
            if event.key == pygame.K_1:
                pieces_list = []
                pieces_places = []
            if event.key == pygame.K_0:
                my_piece = new_piece()
                change_shape(my_piece)
            ## game keys
            if event.key == pygame.K_UP:
                #change_to = 'UP'
                if my_piece['rotate'] == 1:
                    my_piece['rotate'] = 2
                    change_shape(my_piece)
                elif my_piece['rotate'] == 2 and my_piece['shape'] not in ['J','L']:
                    my_piece['rotate'] = 1
                    change_shape(my_piece)
                elif my_piece['rotate'] == 2 and my_piece['shape'] in ['J','L']:
                    my_piece['rotate'] = 3
                    change_shape(my_piece)
                elif my_piece['rotate'] == 3 and my_piece['shape'] in ['J','L']:
                    my_piece['rotate'] = 4
                    change_shape(my_piece)
                elif my_piece['rotate'] == 4 and my_piece['shape'] in ['J','L']:
                    my_piece['rotate'] = 1
                    change_shape(my_piece)
            if event.key == pygame.K_DOWN:
                #change_to = 'DOWN'
                game_speed = game_speed*2
            if event.key == pygame.K_LEFT:
                #change_to = 'LEFT'
                if my_piece["loc"][0][0] != 0+my_piece['size'] and my_piece['loc'][3][1] < window_y - my_piece['full_size']:
                    m_left(my_piece)
            if event.key == pygame.K_RIGHT:
                #change_to = 'RIGHT'
                if my_piece["loc"][3][0] != window_x-my_piece['size'] and my_piece['loc'][3][1] < window_y - my_piece['full_size']:
                    m_right(my_piece)
            if event.key == pygame.K_ESCAPE:
                game_over()
            if event.key == pygame.K_p:
                    if game_state == 'RUNNING':
                        game_state = 'PAUSED'
                    elif game_state == 'PAUSED':
                        game_state = 'RUNNING'
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                #change_to = 'DOWN'
                game_speed = game_speed/2

    if game_state == 'RUNNING':
    #if paused:
    #    paused_screen()
    #    continue

        game_window.fill(black)

        ## Booolean value to see if piece is not yet at the bottom of the screen
        not_bottom = (my_piece['loc'][3][1] < window_y - my_piece['size']) and (my_piece['loc'][2][1] < window_y - my_piece['size']) and (my_piece['loc'][1][1] < window_y - my_piece['size']) and (my_piece['loc'][0][1] < window_y - my_piece['size'])

        #not_touching_list = list(map(lambda x : list(map(lambda y : y  ==  my_piece['loc'][0] or y ==  my_piece['loc'][1] or y ==  my_piece['loc'][2] or y ==  my_piece['loc'][3], x)), pieces_places))

        pieces_places = list(map(lambda x : x['loc'], pieces_list))
        ## mapping function: returns true if pieces are touching eachother (bugged, some pieces won't stop, seems kind of random)
        not_touching_list = list(map(lambda x : list(map(check_touch, x)), pieces_places))

        def check_touch(array):
            x_axis1 = array[0]
            #print(x_axis1)
            y_axis1 = array[1] - my_piece['size']
            #print(y_axis1)
            is_touching = False
            for x in my_piece['loc']:
                if [x_axis1,y_axis1] == x:
                    is_touching = True
            return is_touching

        touching = False

        for x in not_touching_list:
            if any(x) == True:
                touching = True
            else:
                touching = False

            ## FALLING MECHANIC: if nothing is touching, then piece will fall.
        if not_bottom and not touching:
            fall(my_piece)
        ## IF PIECE REACHES THE BOTTOM OR TOUCHES OTHER PIECE, IT STOPS
        if not not_bottom or touching:
            time.sleep(1)
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
    
    elif game_state == 'PAUSED':
           #screen = pygame.display.set_mode((200, 200))
            large_text = pygame.font.SysFont("comicsansms", 30)
            text_surface = large_text.render("Paused", True, white)
            text_rect = text_surface.get_rect(center=(100, 100))
            game_window.blit(text_surface, text_rect)
            pygame.display.update()
    