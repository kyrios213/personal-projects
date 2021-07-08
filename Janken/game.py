import random
import time

print("Welcome to Rock, Paper, Scissors!")

def janken_game():
  moves = ["rock", "paper", "scissors"]
  player = input("rock, paper, scissors: ")
  try:
    enemy = random.choice(moves)
    print("Enemy: " + enemy + "!")
    time.sleep(1)
    if player == enemy:
      print("Tie!")
      janken_game()
    elif player == 'rock' and enemy == 'paper':
      print("Paper covers rock!")
      print("You lose!")
    elif player == 'rock' and enemy == 'scissors':
      print("Rock beats scissors!")
      print("You win!")
    elif player == 'paper' and enemy == 'scissors':
      print("Scissors cut paper!")
      print("You lose!")
    elif player == 'paper' and enemy == 'rock':
      print("Paper covers rock!")
      print("You win!")
    elif player == 'scissors' and enemy == 'rock':
      print("Rock beats scissors!")
      print("You lose!")
    elif player == 'scissors' and enemy == 'paper':
      print("Scissors cut paper!")
      print("You lose!")
  except:
    print("Wrong move!")
    print("Try again")
    janken_game()
  again = input("Play again [y] or [n]: ")
  if again == 'y':
    janken_game()

janken_game()