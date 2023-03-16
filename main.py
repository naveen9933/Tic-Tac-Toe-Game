#creating TIc-Tac_Toe game

#creating game board
board=["-","-","-",
       "-","-","-",
       "-","-","-"]

#diaplaying of the board
def display_board():
  print(board[0] + " |" + board[1] + " |" + board[2])
  print(board[3] + " |" + board[4] + " |" + board[5])
  print(board[6] + " |" + board[7] + " |" + board[8])

#creating global variables
game_still_going = True

current_player='X'

winner= None

def play_game():

  #dispalying initial board
  display_board()
  
  while game_still_going:

    #handleing the turn of the current player
    handle_turn(current_player)

    #checking if the game has ended
    check_if_game_ended() 

    #chaning the player
    flip_player() 

  #checking if there is a winner
  if(winner == 'X' or winner == 'O'):
    print(winner + " won the game")

  #if there is no winner then there printing that it is tie
  else:
    print("Tie")

#handleing the turn of the current player
def handle_turn(current_player):
  
  #printing whose turn it is
  print(current_player + "'s turn")
  
  #taking input for placing
  position = input("Enter any number from 1-9:")
  valid = False
  
  #checking whether the given input is correct
  while not valid:
    
    #checking whether the given input is correct
    while position not in ['1','2','3','4','5','6','7','8','9']:
      position=input("choose a position from 1-9:")
      
    position=int(position)-1

    #checking whether the position is used before
    if board[position] == '-':
      valid = True 
    else:
      print("You can't go there, go again")
  
  #according to the turn filling the position entered
  board[position]=current_player
  
  #displaying board after changes
  display_board()
  
  return

#checking if the game has ended
def check_if_game_ended():
  check_for_winner()
  check_for_tie()
  return 

#checking for winner
def check_for_winner():
  global winner
  #row winner
  row_winner= check_rows()
  #column winner 
  column_winner= check_columns()
  #diagonal winner
  diagonal_winner= check_diagonals()

  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None
  return 
  
#checking for a row winner
def check_rows():
  global game_still_going
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  if row_1 or row_2 or row_3:
    game_still_going = False
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  return

#checking for column winner
def check_columns():
  global game_still_going
  col_1 = board[0] == board[3] == board[6] != "-"
  col_2 = board[1] == board[4] == board[7] != "-"
  col_3 = board[2] == board[5] == board[8] != "-"
  if col_1 or col_2 or col_3:
    game_still_going = False
  if col_1:
    return board[0]
  elif col_2:
    return board[1]
  elif col_3:
    return board[2]
  return

#checking for diagonal winner
def check_diagonals():
  global game_still_going
  dia_1 = board[0] == board[4] == board[8] != "-"
  dia_2 = board[2] == board[4] == board[6] != "-"
  if dia_1 or dia_2:
    game_still_going = False
  if dia_1:
    return board[0]
  elif dia_2:
    return board[2]
  return

#checking for tie
def check_for_tie():
  global game_still_going
  if "-" not in board:
    game_still_going = False
  return

#changing current player to next player
def flip_player():
  global current_player
  if current_player=='X':
    current_player='O'
  elif current_player=='O':
    current_player='X'  
  return

play="y"
#creating a loop so that we can continuously play game until we what to stop 
while(play == 'y'):
  play_game()
  play=input("Do you want to play again y or n:")
  if(play == 'n'):
    break