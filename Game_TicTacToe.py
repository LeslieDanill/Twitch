# --- Tic-Tac-Toe Game --- #

# --- Setup Game --- #
# Define game board
board = {'A1': ' ', 'A2': ' ', 'A3': ' ', 'B1': ' ', 'B2': ' ', 'B3': ' ', 'C1': ' ', 'C2': ' ', 'C3': ' '}

# Define Victory
# !!! Can specify horizontal, vertical, diagonal
victory = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3'], ['C1', 'C2', 'C3'], ['A1', 'B1', 'C1'], ['A2' , 'B2' , 'C2'], ['A3' , 'B3' , 'C3'], ['A1' , 'B2' , 'C3'], ['C1' , 'B2' , 'A3']]

# --- Define Functions --- #
# !!! Could loop through w function

def printboard(board):
    while True:
        x = 'X'
        print('   | A | B | C |')
        print('   -------------')
        print(' 1 | ' + board['A1'] + ' | ' + board['A2'] + ' | ' + board['A3'] + ' |')
        print('----------------')
        print(' 2 | ' + board['B1'] + ' | ' + board['B2'] + ' | ' + board['B3'] + ' |')
        print('----------------')
        print(' 3 | ' + board['C1'] + ' | ' + board['C2'] + ' | ' + board['C3'] + ' |')
        print('   -------------')
        break

def gameplay():
    print('Welcome to TIC-TAC-TOE!  Choose your player: \nX  or  O  ?')
    usermove = input()
    # input playermove
    # validate playermove, else input again; check if won or lost, and print and end game
    while True:
        usermove = input()
        #Validate
        if usermove.upper() == 'X' or 'O':
            ''
        else:
            print('Please choose either  X  or  O')
            continue

'''


# --- GAMEPLAY --- #
gameplay()


# --- Later, when you want to overcomplicate things, you can scale this game to Bingo... and more! --- #
boarddimensions = {'x'='3', 'y'='3', 'z'='0'}
board = 
    int(boarddimensions['x'])


'''
