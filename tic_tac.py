'''
tic_tak
'''
from random import shuffle
#List of lits. Keeps track of player name and total score until end of all games.
PLAYER = [['Player One', 0], ['Player Two', 0]]
GAME = [['', '', ''] for i in range(3)] #The 3x3 game board. Resets with each new game.
TOKEN = ['X', 'O'] #Play pieces
PLAYS = [] #Record of the most recent game. Resets with each new game.
REMATCH = 'y'
DRAW = False

def init_game():
    '''
    Ask for player names
    '''
    PLAYER[0][0] = input("Enter Player One's name: ")
    PLAYER[1][0] = input("Enter Player Two's name: ")

def reset_board():
    '''
    Clear game board.  Each position has a placeholder positive number.
    '''
    global DRAW
    DRAW = False
    i = 1
    for ind_one in range(3):
        for ind_two in range(3):
            GAME[ind_one][ind_two] = i
            i += 1

def choose_player():
    '''
    Randomizes starting player and piece
    '''
    shuffle(PLAYER)
    shuffle(TOKEN)
    print(PLAYER[0][0]+' will begin with '+TOKEN[0]+'!')
    print('\n')

def print_game1():
    '''
    #Prints current game state
    '''
    print('{0:^1}|{1:^1}|{2:^1}'.format(GAME[0][0], GAME[0][1], GAME[0][2]))
    print('-'*10)
    print('{0:^1}|{1:^1}|{2:^1}'.format(GAME[1][0], GAME[1][1], GAME[1][2]))
    print('-'*10)
    print('{0:^1}|{1:^1}|{2:^1}\n'.format(GAME[2][0], GAME[2][1], GAME[2][2]))

def play1():
    '''
    Player1 makes move.
    Request position from Player1, searches for that position in Game array,
    replaces with Player1's piece

    Has error check for out-of-bounds integer
    Has error check for played position
    '''
    while True:
        try:
            play = int(input(PLAYER[0][0]+', on which number do you place your '+TOKEN[0]+'? '))
        except:
            print('Invalid input. Please try again.')
            continue
        else:
            break
    #Continue with integer input
    #Player enters invalid integer
    if play not in range(1, 10):
        print('Out of bounds! ' +PLAYER[0][0]+ ' loses a turn! \n')
    #Make the play, if valid
    for ind_one in range(3):
        for ind_two in range(3):
            if play == GAME[ind_one][ind_two]:
                GAME[ind_one][ind_two] = TOKEN[0]
                PLAYS.append((PLAYER[0][0], TOKEN[0], play))
                print('\n'*25)
                print_game1()
                return
    else:
    #Player moves on a taken field
        print('Position ' +str(play)+ ' is occupied! ' + PLAYER[0][0]+ ' loses a turn. \n')
def play2():
    '''
    #Same as play1() but now for Player2
    '''
    while True:
        try:
            play = int(input(PLAYER[1][0]+ ', on which number do you place your '+TOKEN[1]+'? '))
        except:
            print('Invalid input. Please try again.')
            continue
        else:
            break
    #Continue with integer input
    #Player enters invalid integer
    if play not in range(1, 10):
        print('Out of bounds! ' +PLAYER[1][0]+ ' loses a turn! \n')
    #Make the play, if valid
    for ind_one in range(3):
        for ind_two in range(3):
            if play == GAME[ind_one][ind_two]:
                GAME[ind_one][ind_two] = TOKEN[1]
                PLAYS.append((PLAYER[1][0], TOKEN[1], play))
                print('\n'*25)
                print_game1()
                return
    else:
    #Player moves on a taken field
        print('Position ' +str(play)+ ' occupied! ' + PLAYER[1][0]+ ' loses a turn. \n')

def play_game():
    '''
    Game play
    Prints current state of game
    Checks game over condition, asks for play

    '''
    print_game1()
    while True:
        if not game_over():
            play1()
        if not game_over():
            play2()
        elif not DRAW:
            if PLAYS[-1][0] == PLAYER[1][0]:
                PLAYER[1][1] += 1
                break
            elif PLAYS[-1][0] == PLAYER[0][0]:
                PLAYER[0][1] += 1
                break
        else:
            break

def game_over():
    '''
    Check to see if game play over.
    Checks for filled game board.  If board, full raises Draw flag
    '''
    #Draw
    global DRAW
    counter = 0
    for ind_one in range(3):
        for ind_two in range(3):
            if GAME[ind_one][ind_two] in ['X', 'O']:
                counter += 1
    if counter == 9:
        DRAW = True
    #Win
    #Check for winning condition and returns true if found
    if DRAW or ((GAME[0][0] == GAME[0][1] and GAME[0][1] == GAME[0][2])
                or (GAME[1][0] == GAME[1][1] and GAME[1][1] == GAME[1][2])
                or (GAME[2][0] == GAME[2][1] and GAME[2][1] == GAME[2][2])
                or (GAME[0][0] == GAME[1][0] and GAME[1][0] == GAME[2][0])
                or (GAME[0][1] == GAME[1][1] and GAME[1][1] == GAME[2][1])
                or (GAME[0][2] == GAME[1][2] and GAME[1][2] == GAME[2][2])
                or (GAME[0][0] == GAME[1][1] and GAME[1][1] == GAME[2][2])
                or (GAME[2][0] == GAME[1][1] and GAME[1][1] == GAME[0][2])):
        return True
    return False
def scores():
    '''
    Print running score at end of each match
    '''
    if DRAW:
        print('Draw!')
    else:
        #Winner is last person to play
        print(PLAYS[-1][0]+' wins!')
    #print scorecard for all games
    print('{p1} : {p1s} \n{p2} : {p2s}'.format(p1=PLAYER[0][0], 
                                               p2=PLAYER[1][0], p1s=PLAYER[0][1], p2s=PLAYER[1][1]))
#
#Game play logic
#
init_game()
choose_player()
reset_board()
play_game()
scores()
while input('Rematch? (y/n): ') == 'y':
    print('New game. \n')
    print('\n'*20)
    reset_board()
    play_game()
    scores()
#print('All done! Bye-bye!')
if PLAYER[0][1] > PLAYER[1][1]:
    print(PLAYER[0][0] + ' is the champion!')
elif PLAYER[0][1] < PLAYER[1][1]:
    print(PLAYER[1][0] + ' is the champion!')
else:
    print('Draw! Better luck next time!')
#print(PLAYS)
