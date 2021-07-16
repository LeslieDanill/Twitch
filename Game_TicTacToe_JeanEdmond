from random import randint
import os

def get_user_team():
  while True:
    team = input("Choose your team: (X or O)").upper()
    if team == "X" or team == "O":
      return team
    else:
      print("Incorrect input.")


def get_user_move(board):
  while True:
    move = input("Input your move: ").upper()

    # A move is only valid if it is one of the key of the dict
    # and if the associated value is empty, meaning that the move
    # hasn't been played before by either player
    if move in board.keys() and board[move] == " ":
      return move
    else:
      print("Incorrect input.")

def keep_playing():
  while True:
    user_input = input("wanna play again? (y/n)")
    if user_input.lower() == 'y':
      return True
    elif user_input.lower() == 'n':
      return False
    else:
      print("Incorrect input.")

def is_board_full(board):
  return all(e != " " for e in board.values())

def has_won(team, board):
  #copy paste ftw
  assert(team == "X" or team == "O")

  if board["A1"] == team and board["A2"] == team and board["A3"] == team:
    return True
  if board["B1"] == team and board["B2"] == team and board["B3"] == team:
    return True
  if board["C1"] == team and board["C2"] == team and board["C3"] == team:
    return True

  if board["A1"] == team and board["B1"] == team and board["C1"] == team:
    return True
  if board["A2"] == team and board["B2"] == team and board["C2"] == team:
    return True
  if board["A3"] == team and board["B3"] == team and board["C3"] == team:
    return True

  if board["A1"] == team and board["B2"] == team and board["C3"] == team:
    return True
  if board["A3"] == team and board["B2"] == team and board["C1"] == team:
    return True

  return False


def get_available_moves(board):
  moves = []
  for key, value in board.items():
    if value == " ":
      moves.append(key)
  return moves

def generate_random_move(board):
  moves = get_available_moves(board)
  assert(len(moves) > 0)
  return moves[randint(0, len(moves) - 1)]

def game_not_over(board):
  return not (has_won("X", board) or has_won("O", board) or is_board_full(board))

def get_winner(board):
  if has_won("X", board):
    return "X"
  if has_won("O", board):
    return "O"
  return None

def print_board(board):
  clear_screen()
  print(f"{board['A1']} | {board['A2']} | {board['A3']}")
  print("-" * 9)
  print(f"{board['B1']} | {board['B2']} | {board['B3']}")
  print("-" * 9)
  print(f"{board['C1']} | {board['C2']} | {board['C3']}\n")

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

def whose_turn(board):
  # If the number of empty cells in the board 
  # is even then it's O's turn otherwise it's X's turn
  if sum(value == " " for value in board.values()) % 2 == 0:
    return "O"
  else:
    return "X"

def start_new_game():

  board = {
    "A1": " ",
    "A2": " ",
    "A3": " ",
    "B1": " ",
    "B2": " ",
    "B3": " ",
    "C1": " ",
    "C2": " ",
    "C3": " ",
  }

  user_team = get_user_team()

  if user_team == "X":
    computer_team = "O"
  else:
    computer_team = "X"

  while game_not_over(board):
    print_board(board)
    if whose_turn(board) == user_team:
      move = get_user_move(board)
      board[move] = user_team
    else:
      move = generate_random_move(board)
      board[move] = computer_team
  
  print_board(board) 
  winner = get_winner(board)
  
  if winner is None:
    print("drawn game residentSleeper")
  elif winner == user_team:
    print("You won")
  else:
    print("You suck")

def main():
  start_new_game()

  while keep_playing():
    clear_screen()
    start_new_game()
    
main()