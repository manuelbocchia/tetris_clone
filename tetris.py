import pygame
import time
import random
from my_tetris_class import change_shape, fall, m_left, m_right
import numpy as np
import itertools
from collections import defaultdict
import pprint


################################################################################################
#                       CONFIGURATIONS                                                         #             
################################################################################################

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

### FONT FOR DEBUGGING PIECE PLACES
debug_font = pygame.font.SysFont('arial', 8)

################################################################################################
#                       SET UP FUNCTIONS                                                       #             
################################################################################################


## Function to finish the game
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


#list comprehension
#[i for i in sublist if something]

### Generate the playing pieces
def new_piece():
    return {'shape': random.choice(['S','Z','L','J','I','O']), 
            #'place':(window_x/2), 
            'size' : 20, 
            'color' : random.choice(['white','blue','red']), 
            'loc':[[0,0],[0,0],[0,0],[0,0]], 
            'full_size':0, 
            'rotate':1}

#THIS IS DUMMY PIECE FOR DEBUGGING

my_piece = {'shape':'I', 
            #'place':(window_x/2), 
            'size' : 20, 
            'color' : random.choice(['white','blue','red']), 
            'loc':[[0,0],[0,0],[0,0],[0,0]], 
            "full_size":0, 
            "rotate":1}


change_shape(my_piece)


### GENERATES LIST OF COMPLETE LINES TO CHECK IF LINE IS COMPLETE IN GAME

def generate_list():
    nx_list = []
    ny_list = []
    vector_list1 = []
    x = 0
    y = 0
    while y < window_y - block_sz[0]:
        ny_list.append(y + block_sz[0])
        y += block_sz[0]
    while x < window_x - block_sz[0]:
        nx_list.append(x + block_sz[0])
        x += block_sz[0]
    #return nx_list
    for z in ny_list:
        vector_list1.append([[i,z] for i in nx_list])
    return vector_list1

## list of complete lines to check
complete_lines = generate_list()
       
## pieces that are no longer playing
pieces_list = []
## coordenates of each piece for better accessing
pieces_places = []

def instructions():
    small_text = pygame.font.SysFont("arial", 20)
    text_surface1 = small_text.render("← → ↓: Move", True, white)
    text_surface2 = small_text.render("↑: Rotate ", True, white)
    text_surface3 = small_text.render("P: Pause", True, white)
    text_rect1 = text_surface1.get_rect(center=(80, 10))
    text_rect2 = text_surface2.get_rect(center=(80, 30))
    text_rect3 = text_surface3.get_rect(center=(80, 50))
    game_window.blit(text_surface1, text_rect1)
    game_window.blit(text_surface2, text_rect2)
    game_window.blit(text_surface3, text_rect3)
    


game_state = 'RUNNING'

while True:

################################################################################################
#                       CONTROL SECTION                                                        #             
################################################################################################
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            ## special keys for debugging
            if event.key == pygame.K_1:
                pieces_list = []
                pieces_places = []
            if event.key == pygame.K_0:
                my_piece = new_piece()
                change_shape(my_piece, (window_x/2), 0)
            if event.key == pygame.K_2:
                my_piece = {'shape':'I', 
                            #'place':(window_x/2), 
                            'size' : 20, 
                            'color' : random.choice(['white','blue','red','green']), 
                            'loc':[[0,0],[0,0],[0,0],[0,0]], 
                            "full_size":0, 
                            "rotate":1}
                change_shape(my_piece, (window_x/2), 0)
            if event.key == pygame.K_3:
                my_piece = {'shape':'O', 
                            #'place':(window_x/2), 
                            'size' : 20, 
                            'color' : random.choice(['white','blue','red','green']), 
                            'loc':[[0,0],[0,0],[0,0],[0,0]], 
                            "full_size":0, 
                            "rotate":1}
                change_shape(my_piece, (window_x/2), 0)
            ## game keys
            #### ---- TO DO = FIX KEYS FOR LEFT AND RIGHT (adjust collission for all pieces)
            if event.key == pygame.K_UP:
                #change_to = 'UP'
                if my_piece['rotate'] == 1:
                    my_piece['rotate'] = 2
                    #my_piece['place'] = my_piece['loc'][0][0]
                    change_shape(my_piece, my_piece['loc'][0][0], my_piece['loc'][0][1])
                elif my_piece['rotate'] == 2 and my_piece['shape'] not in ['J','L']:
                    my_piece['rotate'] = 1
                    #my_piece['place'] = my_piece['loc'][0][0]
                    change_shape(my_piece, my_piece['loc'][0][0], my_piece['loc'][0][1])
                elif my_piece['rotate'] == 2 and my_piece['shape'] in ['J','L']:
                    my_piece['rotate'] = 3
                    #my_piece['place'] = my_piece['loc'][0][0]
                    change_shape(my_piece, my_piece['loc'][0][0], my_piece['loc'][0][1])
                elif my_piece['rotate'] == 3 and my_piece['shape'] in ['J','L']:
                    my_piece['rotate'] = 4
                    #my_piece['place'] = my_piece['loc'][0][0]
                    change_shape(my_piece, my_piece['loc'][0][0], my_piece['loc'][0][1])
                elif my_piece['rotate'] == 4 and my_piece['shape'] in ['J','L']:
                    my_piece['rotate'] = 1
                    change_shape(my_piece, my_piece['loc'][0][0], my_piece['loc'][0][1])
            if event.key == pygame.K_DOWN:
                #change_to = 'DOWN'
                game_speed = game_speed*4
            if event.key == pygame.K_LEFT:
                #change_to = 'LEFT'
                if my_piece["loc"][0][0] != 0 and my_piece['loc'][3][1] < window_y: #- my_piece['full_size']:
                    m_left(my_piece)
            if event.key == pygame.K_RIGHT:
                #change_to = 'RIGHT'
                if (my_piece["loc"][3][0] != window_x-my_piece['size']) and my_piece['loc'][3][1] < window_y - my_piece['full_size']:
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
                game_speed = game_speed/4

################################################################################################
#                       MAIN GAME LOOP                                                         #             
################################################################################################


    if game_state == 'RUNNING':


        game_window.fill(black)

        ## Booolean value to see if piece is not yet at the bottom of the screen
        not_bottom = (my_piece['loc'][3][1] < window_y - my_piece['size']) and (my_piece['loc'][2][1] < window_y - my_piece['size']) and (my_piece['loc'][1][1] < window_y - my_piece['size']) and (my_piece['loc'][0][1] < window_y - my_piece['size'])

        pieces_places = list(map(lambda x : x['loc'], pieces_list))


        #### TO DO - Investigate what is wrong with the bottom touching logic
        #### HINTS: seems to be something regarding the movement left to right?
        ## mapping function: returns true if pieces are touching eachother (bugged, some pieces won't stop, seems kind of random)
        not_touching_list = list(map(lambda x : list(map(check_touch, x)), pieces_places))

        def check_touch(array):
            x_axis1 = array[0]
            y_axis1 = array[1] - my_piece['size']
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
        
        ### First, check if line is complete.
        ## set up empty list to get all actually completed lines from the function below
        final_complete_lines = []

        def is_line_complete():
            ## Este diccionario ordena las piezas segun cada fila..
                   
            final_list = defaultdict(list)
            
            ## Primero achato la lista de bloques actuales.
            flat_list = list(itertools.chain.from_iterable(pieces_places))
            iter = 0
            ## Luego itero sobre la lista de lineas completas para comparar.
            ## 
            for y in complete_lines:    
            #    print(y)
                axis = y[0][1]
                final_list[iter] = [x for x in flat_list if x[1] == axis]
                iter += 1                
            ## Una vez que tengo la final list, puedo hacer el check:
            ## Este check consiste en validar si todos los elementos de una linea
            ## del complete_lines se encuentran presentes en alguno de los
            ## pares del dictionario final_list.
            whole_line = False
            for cl_list in complete_lines:
            # Check if all items in cl_list are contained in any list in final_list
            #    print(cl_list)
                for key in final_list:
            #        print(key)
                    if all(item in final_list[key] for item in cl_list):
                        whole_line = True
                        final_complete_lines.append(final_list[key])


            return whole_line

        ### If line is complete, take that line list and doble cross with list of pieces.
        ###
        ### Where there's a match, remove that block and modify the other ones.

        def clean_line():
        ## This function should clean all the lines and move the blocks from the other lines to the respective places.
        #so when a line is complete, you go to the list of complete lines and get each one.
            for line in final_complete_lines:
                piece_removed = False
                ## and then you go get all the pieces from the current piece_list
                for piece in pieces_list:
                    ## you check all the squares in those pieces, and if they match you remove them
                    for sq in piece['loc']:
                        if sq in line:
                            
                            piece['loc'].remove(sq)
                            piece_removed = True
                        
                            new_len = len(piece['loc'])
                          
                            if piece_removed and new_len >= 1:
                                for index in range(0,new_len-1):
                                    while piece['loc'][index][1] != window_y-piece['size'] and not any(pieces_places) == piece ['loc'][index][1] + piece['size']:
                                        piece['loc'][index][1] += piece['size']
                    if piece_removed and len(piece['loc']) == 4:
                    #new_len = len(piece['loc'])
                        while piece['loc'][3][1] != window_y and not any(pieces_places) == piece['loc'][3][1] +piece['size']:
                            print(f'argument 1 {[0,piece["size"]]}')
                            print(f'argument 2 {piece["loc"]}')
                            new_value = [0,piece['size']]
                            piece['loc'] = list(map(lambda x : np.add(piece['loc'],new_value),piece['loc']))

        is_line_complete()
        clean_line()

            ## FALLING MECHANIC: if nothing is touching, then piece will fall.
        if not_bottom and not touching:
            fall(my_piece)
        ## IF PIECE REACHES THE BOTTOM OR TOUCHES OTHER PIECE, IT STOPS
        if not not_bottom or touching:
            time.sleep(0.2)
            pieces_list.append(my_piece)
            my_piece = new_piece()
            change_shape(my_piece, (window_x/2), 0)

################################################################################################
#                       DRAWING SECTION                                                        #             
################################################################################################


        def draw_text(text, font, color, surface, x, y):
            textobj = font.render(text, True, color)
            textrect = textobj.get_rect()
            textrect.topleft = (x, y)
            surface.blit(textobj, textrect)

        ## DRAWS ALL PIECES IN THE LIST
        for piece in pieces_list:
            for sq_place in piece['loc']:
                pygame.draw.rect(game_window, piece['color'], pygame.Rect(sq_place[0], sq_place[1], piece['size'], piece['size']))
                #for debugging
                draw_text(f'{sq_place[0]}/{sq_place[1]}',debug_font,green,game_window,sq_place[0],sq_place[1])
        ## DRAWS CURRENT PIECE
        for sq_place in my_piece['loc']:
            pygame.draw.rect(game_window, my_piece['color'], pygame.Rect(sq_place[0], sq_place[1], my_piece['size'], my_piece['size']))
            #for debugging
            draw_text(f'{sq_place[0]}/{sq_place[1]}',debug_font,green,game_window,sq_place[0],sq_place[1])

        instructions()
        pygame.display.update()
        fps.tick(game_speed)

################################################################################################
#                       PAUSE SECTION                                                          #             
################################################################################################
    
    elif game_state == 'PAUSED':
           #screen = pygame.display.set_mode((200, 200))
            large_text = pygame.font.SysFont("comicsansms", 30)
            text_surface = large_text.render("Paused", True, white)
            text_rect = text_surface.get_rect(center=(100, 100))
            game_window.blit(text_surface, text_rect)
            instructions()
            pygame.display.update()
    