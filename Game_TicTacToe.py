# --- Tic-Tac-Toe Game --- #

# --- Define Game Board --- #
board = {'A1': ' ', 'A2': ' ', 'A3': ' ', 'B1': ' ', 'B2': ' ', 'B3': ' ', 'C1': ' ', 'C2': ' ', 'C3': ' '}

# --- Define Functions --- #
# !!! Could loop through w function
'''
def getuserdifficulty():
    userdifficulty = input()
'''
''' This is where you lost your patience
def getusermove():
    usermove = input()
    #Validate
    if usermove.upper() == 'X' or 'O':
        ''
    else:
        print('Please choose either  X  or  O')
        continue
'''

def getbotmove():
    botmove = ''

def updatenewmove():
    newmove = ''

def printboard():
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

# --- GAMEPLAY --- #

#Bot message:  Welcome to TIC-TAC-TOE!  Choose your player:<br> X  or  O  ?
# getusermove
# validateusermove

# input playermove
# validate playermove, else input again; check if won or lost, and print and end game




'''
# --- Imports --- #
import random

# --- Define Functions --- #
# Input & validate userguess
def validateuserguess(): 
    print('Take a guess.')
    while True:
        try:
            userguess = int(input())
            return userguess
        except ValueError:
            print('I\'m not your pal, buddy.')
            print('Try a number this time?')
            continue
        except:
            print('Beep boop. You crashed the game.')
            exit(1) 

# --- Start Game --- #
print('Hello. What is your name?')
name = input()
key = random.randint(1,20)
print('Well, ' + name + ', I am thinking of a number between 1 and 20.')

#Allow user to guess up to 6 times
for x in range(6):
    userguess = validateuserguess()
    # If guess correct
    if userguess == key:
        print('Congrats, ' + name + ' ! You got it in only ' + str(x + 1) + ' ' + ("guesses" if (x + 1) > 1 else "guess") + '.')
        print("And remember the lesson you've learned here... you can use double quotes any time you like friend ;)")
        break
    # If guess not in range
    elif userguess < 1 or userguess > 20:
        print('That\'s not even between 1 and 20 ...')
    # If too low
    elif userguess < (key - 10):
        print('That\'s way too low!')
    elif userguess < (key - 2):
            print('Too low.')
    elif userguess < key:
        print('That\'s a little too low ...')
    # If too high
    elif userguess > (key + 10):
        print('That\'s way too high!')
    elif userguess > (key + 3):
            print('Too high.')
    elif userguess > key:
        print('That\'s a little too high ...')
    # If out of guesses
    if (x + 1) == 6:
        print('Uh oh, out of guesses. The number I was thinking of was ' + str(key) + '.')

print('Bye bye now!')
'''
