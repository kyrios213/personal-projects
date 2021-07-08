def compare(set1, set2):
  x = set(set1)
  y = set(set2)
  if x.intersection(y) == y:
    return True
def win_con(moves):
  win1 = [1, 2, 3]
  win2 = [4, 5, 6]
  win3 = [7, 8, 9]
  win4 = [1, 4, 7]
  win5 = [2, 5, 8]
  win6 = [3, 6, 9]
  win7 = [1, 5, 9]
  win8 = [3, 5, 7]
  if compare(moves, win1):
    return True
  elif compare(moves, win2):
    return True
  elif compare(moves, win3):
    return True
  elif compare(moves, win4):
    return True
  elif compare(moves, win5):
    return True
  elif compare(moves, win6):
    return True
  elif compare(moves, win7):
    return True
  elif compare(moves, win8):
    return True
  else:
    return False
def tic_tac_toe():
  tic_board = "1|2|3\n_|_|_\n4|5|6\n_|_|_\n7|8|9"
  player1_moves = []
  player2_moves = []
  turn = 0
  while True:
    print(tic_board)
    p1 = input("Player 1's Turn: ")
    try:
      tic_board = tic_board.replace(p1, 'X')
      print(tic_board)
    except:
      print("Invalid move")
    player1_moves.append(int(p1))
    turn += 1
    if win_con(player1_moves):
      print("Player 1 wins")
      break
      turn += 1
    if turn == 9:
      print("Out of moves")
      break
    p2 = input("Player 2's Turn: ")
    try:
      tic_board = tic_board.replace(p2, 'O')
    except:
      print("Invalid move")
    player2_moves.append(int(p2))
    turn += 1
    if turn == 9:
      print("Out of moves")
      break
    if win_con(player2_moves):
      print(tic_board)
      print("Player 2 wins")
      break
  again = input("Wanna play again?: y or n\n")
  if again == 'y':
    tic_tac_toe()

tic_tac_toe()