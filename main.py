import numpy as np
import sys
import pygame
import settings
import math


def create_board():
    #Creating a matrix of zeros that are returned
    board = np.zeros((settings.ROW_COUNT,settings.COLUMN_COUNT))
    return board
def drop_piece(board, row, col, piece):
    board[row][col] = piece#Here we drop the piece in the first empty spot in a given row and collumn
def is_valid_location(board, col):
    return board[settings.ROW_COUNT-1][col] == 0 #board[5][col] == 0 is a conditional statement that checks if the value at the specified column (col) in the 6th row (5) of a two-dimensional list or array board is equal to 0.
def get_next_open_row(board, col):
    for r in range(settings.ROW_COUNT):
        if board[r][col] == 0: #if any rows for each column in the 2D list == 0
            return r#Returns the first row instance empty
        
def print_board(board):
    print(np.flip(board, 0)) # reverses the order of array elements along the 0 axis

def winning_move(board, piece):
    #Check horizontal locations for the win 
    for c in range(settings.COLUMN_COUNT-3):#-3 because combinations doesnt work for values to far to the left
        for  r in range(settings.ROW_COUNT):
            #looping through every index in horizontal collumn that can have a winning move
            if board[r][c] == piece and  board[r][c+1] == piece and board[r][c+2] == piece and board[r][c] == piece:#checking the horizontal row
                return True
    #Check vertical locations for win
    for c in range(settings.COLUMN_COUNT):
        for  r in range(settings.ROW_COUNT -3):#-3 because combinations doesnt work for values to far on the top
            #looping through every index in horizontal collumn that can have a winning move
            if board[r][c] == piece and  board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:#checking the horizontal row
                return True
    #Check postiively sloped diagonals
    for c in range(settings.COLUMN_COUNT-3):
        for  r in range(settings.ROW_COUNT -3):#-3 because combinations doesnt work for values to far on the top
            #looping through every index in horizontal collumn that can have a winning move
            if board[r][c] == piece and  board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:#checking the horizontal row
                return True
    #Check negatively sloped diagonals
    for c in range(settings.COLUMN_COUNT-3):
        for  r in range(3, settings.ROW_COUNT):#-3 because combinations doesnt work for values to far on the top
            #looping through every index in horizontal collumn that can have a winning move
            if board[r][c] == piece and  board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:#checking the horizontal row
                return True

def draw_board(board):
    for c in range(settings.COLUMN_COUNT):
        for r in range(settings.ROW_COUNT):
            pygame.draw.rect(screen, settings.BLUE, (c*settings.SQUARE_SIZE, r*settings.SQUARE_SIZE+settings.SQUARE_SIZE, settings.SQUARE_SIZE, settings.SQUARE_SIZE))
            #Drawing the rectangle where the circles are and below drawing the actual circles. 
            pygame.draw.circle(screen, settings.BLACK,(int(c*settings.SQUARE_SIZE+settings.SQUARE_SIZE/2), int(r*settings.SQUARE_SIZE+settings.SQUARE_SIZE+settings.SQUARE_SIZE/2)) , settings.RADIUS)
    for c in range(settings.ROW_COUNT):
        for r in range(settings.ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, settings.RED,(int(c*settings.SQUARE_SIZE+settings.SQUARE_SIZE/2), settings.HEIGHT - int(r*settings.SQUARE_SIZE+settings.SQUARE_SIZE/2)) , settings.RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, settings.YELLOW ,(int(c*settings.SQUARE_SIZE+settings.SQUARE_SIZE/2), settings.HEIGHT - int(r*settings.SQUARE_SIZE+settings.SQUARE_SIZE/2)) , settings.RADIUS)
    pygame.display.update()#Rerenders the sceen on change
    
board = create_board()
print_board(board)
game_over = False
turn = 0

pygame.init()
myfont = pygame.font.SysFont("monospace", 75)
size = (settings.WIDTH, settings.HEIGHT) 
#Setting screen size and displaying them below
screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()#Updates in cases of changes

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #When pressed exit, the "system" exits
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, settings.BLACK, (0,0,settings.WIDTH, settings.SQUARE_SIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, settings.RED, (posx, int(settings.SQUARE_SIZE/2)), settings.RADIUS)
            else:
                pygame.draw.circle(screen, settings.YELLOW, (posx, int(settings.SQUARE_SIZE/2)), settings.RADIUS)
        pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN:
            #ask for player 1 input
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/settings.SQUARE_SIZE)) #Dividing by 100 so that we get a col ebtween 1-6

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)

                    if winning_move(board, 1):
                        label = myfont.render("Player 1 wins!!", 1, settings.RED)
                        screen.blit(label, (40, 10))
                        game_over = True

            #Aask for player 2 input
            else:
                posx = event.pos[0]
                col = int(math.floor(posx/settings.SQUARE_SIZE)) 
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)

                    if winning_move(board, 2):
                        label = myfont.render("Player 2 wins!!", 1, settings.YELLOW)
                        screen.blit(label, (40, 10))
                        game_over = True
            print_board(board)
            draw_board(board)
            turn += 1
            turn = turn % 2 # Rest after two so that we only get 0 or 1/ alternateves between player 1 and player 2

            if game_over:

                pygame.time.wait(50000)


    

