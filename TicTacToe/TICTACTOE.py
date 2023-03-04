import pygame
import math
from SaveLoadManager import SaveLoadSystem

#Initializing Save/Load System
saveloadmanager=SaveLoadSystem(".save","save_data")

#Initializing pygame
pygame.init()

#Setting the Font
font = pygame.font.Font("Fonts/neuropol.otf",20)

#Setting display resolution and window title
height=700
width=1200
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("TIC-TAC-TOE")

# Loading all images and Texts
bg = pygame.image.load('Icons/background.png')
grid = pygame.image.load('Icons/grid.png')
X_1 = pygame.image.load('Icons/X_1.png')
X_2 = pygame.image.load('Icons/X_2.png')
X_3 = pygame.image.load('Icons/X_3.png')
X_4 = pygame.image.load('Icons/X_4.png')
X_5 = pygame.image.load('Icons/X_5.png')
X_6 = pygame.image.load('Icons/X_6.png')
X_7 = pygame.image.load('Icons/X_7.png')
X = pygame.image.load('Icons/X.png')

x_array = [X_1,X_2,X_3,X_4,X_5,X_6,X_7,X]

O_1 = pygame.image.load('Icons/O_1.png')
O_2 = pygame.image.load('Icons/O_2.png')
O_3 = pygame.image.load('Icons/O_3.png')
O_4 = pygame.image.load('Icons/O_4.png')
O_5 = pygame.image.load('Icons/O_5.png')
O_6 = pygame.image.load('Icons/O_6.png')
O_7 = pygame.image.load('Icons/O_7.png')
O_8 = pygame.image.load('Icons/O_8.png')
O_9 = pygame.image.load('Icons/O_9.png')
O_10 = pygame.image.load('Icons/O_10.png')
O = pygame.image.load('Icons/O.png')

y_array = [O_1,O_2,O_3,O_4,O_5,O_6,O_7,O_8,O_9,O_10,O]

horizontal = pygame.image.load('Icons/horizontal.png')
vertical = pygame.image.load('Icons/vertical.png')
diagonal_1 = pygame.image.load('Icons/diagonal_1.png')
diagonal_2 = pygame.image.load('Icons/diagonal_2.png')

grid_info = [['a','a','a'],['a','a','a'],['a','a','a']]
grid_pos = [[[75,75],[275,75],[475,75]],[[75,275],[275,275],[475,275]],[[75,475],[275,475],[475,475]]]
current = 'x'
score=saveloadmanager.Load_game_data(["score"],[[0,0]])
score_x = score[0]
score_o = score[1]

text_1 = font.render('Game Over: Draw', True, (0, 0, 0))
text_2 = font.render('Game Over: Player wins', True, (0, 0, 0))
text_3 = font.render('Press Space for next round', True, (0, 0, 0))
text_4 = font.render('Press R to reset score', True, (0, 0, 0))
sc_x = font.render(f"Player 1 score : {score_x} ", True , (0,0,0))
sc_o = font.render(f"Player 2 score : {score_o} ", True , (0,0,0))


def insert(grid_info,current,x_array):
    
    mouse_positon = pygame.mouse.get_pos()
    x_pos = mouse_positon[0]
    y_pos = mouse_positon[1]
    y_index = math.floor((0.005)*x_pos - 0.25)
    x_index = math.floor((0.005)*y_pos - 0.25)

    if x_index > 2 or x_index < 0 or y_index > 2 or y_index < 0 :
        x_index = -1
        y_index = -1
        return (grid_info,current,x_array)

    if current == 'x' and grid_info[x_index][y_index] == 'a':
        grid_info[x_index][y_index] = 'x'
        pos = grid_pos[x_index][y_index]
        for h in range(7):
            screen.blit(x_array[h], (pos[0], pos[1]))
            pygame.display.update()
            pygame.time.delay(10)

    elif current == 'o' and grid_info[x_index][y_index] == 'a':
        grid_info[x_index][y_index] = 'o'
        pos = grid_pos[x_index][y_index]
        for h in range(11):
            screen.blit(y_array[h], (pos[0], pos[1]))
            pygame.display.update()
            pygame.time.delay(10)

    else:
        return (grid_info,current,x_array)

    if current == 'x':
        current = 'o'
    else:
        current = 'x'
        
    return (grid_info,current,x_array)

def display(grid_pos,grid_info):

    for i in range(3):
        for j in range(3):

            if grid_info[i][j] == 'x' :
                pos = grid_pos[i][j]
                screen.blit(X,(pos[0],pos[1]))

            elif grid_info[i][j] == 'o' :
                pos = grid_pos[i][j]
                screen.blit(O,(pos[0],pos[1]))

def check(grid_info):
    for i in range(3):
        first = grid_info[i][0]
        value = 0
        for j in range(3):
            if grid_info[i][j] != first or grid_info[i][j] == 'a':
                value = 1
                break
        if value == 0:
            #print( "1_Game Over" )
            return False,i,1,first

    for i in range(3):
        first = grid_info[0][i]
        value = 0
        for j in range(3):
            if grid_info[j][i] != first or grid_info[j][i] == 'a':
                value = 1
                break
        if value == 0:
            #print( "2_Game Over" )
            return False,i,2,first

    if grid_info[0][0] == grid_info[1][1] and grid_info[1][1] == grid_info[2][2]:
        if grid_info[0][0] == 'a':
            return True,-1,3,'a'
        #print("3_Game Over")
        return False,-2,3,grid_info[0][0]

    if grid_info[2][0] == grid_info[1][1] and grid_info[1][1] == grid_info[0][2]:
        if grid_info[2][0] == 'a':
            return True,-1,3,'a'
        #print("4_Game Over")
        return False,-3,4,grid_info[2][0]

    return True,-1,3,'a'

def check_NA(grid_info):
    for i in range(3):
        if 'a' in grid_info[i]:
            return True
    #print("5_Game Over")
    return False

def reset(grid_info,grid_pos,current,counter):
    
    grid_info = [['a', 'a', 'a'], ['a', 'a', 'a'], ['a', 'a', 'a']]
    grid_pos = [[[75, 75], [275, 75], [475, 75]], [[75, 275], [275, 275], [475, 275]],
                [[75, 475], [275, 475], [475, 475]]]
    current = 'x'
    counter = 0
    
    return (grid_info,grid_pos,current,counter)
counter = 0
first = 1

active = True
while active:
    
    screen.fill((0,0,0))
    screen.blit(bg,(0,0))
    screen.blit(grid, (50, 50))
    screen.blit(sc_x, (780, 250))
    screen.blit(sc_o, (780, 300))
    if first == 1:
        screen.blit(text_4, (780, 150))

    display(grid_pos,grid_info)

    status = check(grid_info)
    status_NA = check_NA(grid_info)
    # All current info is stored in these status arrays
    val = 0

    if status[0] == False:
        first = first + 1
        val = 1
        screen.blit(text_2,(780,50))
        screen.blit(text_3,(780,100))
        screen.blit(text_4,(780,150))

        if status[2] == 1:
            screen.blit(horizontal, (50, (200 * status[1]) + 145))
        elif status[2] == 2:
            screen.blit(vertical, ((200*status[1])+145,50))
        elif status[2] == 3:
            screen.blit(diagonal_2, (50,50))
        elif status[2] == 4:
            screen.blit(diagonal_1, (50,50))

        if status[3] == 'x'  and counter == 0:
            #print( status[3] )
            #print( score_x )
            score_x = score_x + 1
            text_2=font.render("Game Over: Player 1 wins",True,(0,0,0))
            sc_x = font.render(f"Player 1 score : {score_x} ", True, (0, 0, 0))
            sc_o = font.render(f"Player 2 score : {score_o} ", True, (0, 0, 0))
            screen.blit(sc_x, (780, 250))
            screen.blit(sc_o, (780, 300))
            counter = counter + 1

        elif status[3] == 'o' and counter == 0:
            #print(status[3])
            #print( score_o )
            score_o = score_o + 1
            text_2=font.render("Game Over: Player 2 wins",True,(0,0,0))
            sc_x = font.render(f"Player 1 score : {score_x} ", True, (0, 0, 0))
            sc_o = font.render(f"Player 2 score : {score_o} ", True, (0, 0, 0))
            screen.blit(sc_x, (780, 250))
            screen.blit(sc_o, (780, 300))
            counter = counter + 1

    elif status_NA == False and status[0] == True:
        val = 1
        screen.blit(text_1,(780,50))
        screen.blit(text_3,(780,100))
        screen.blit(text_4, (780, 150))
        first = first + 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            score=[score_x,score_o]
            saveloadmanager.Save_game_data([score],["score"])
            active = False
            

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE and val == 1:
                (grid_info,grid_pos,current,counter)=reset(grid_info,grid_pos,current,counter)
            if event.key == pygame.K_r and ( first == 1 or val == 1 ) :
                score_x , score_o= 0 , 0
                sc_x = font.render(f"Player 1 score : {score_x} ", True, (0, 0, 0))
                sc_o = font.render(f"Player 2 score : {score_o} ", True, (0, 0, 0))
                (grid_info,grid_pos,current,counter)=reset(grid_info,grid_pos,current,counter)

        if event.type == pygame.MOUSEBUTTONDOWN and val == 0:
            (grid_info,current,x_array)=insert(grid_info,current,x_array)

    pygame.display.update()
    
pygame.quit();