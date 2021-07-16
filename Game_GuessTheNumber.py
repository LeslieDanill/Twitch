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

