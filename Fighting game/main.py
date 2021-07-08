import random
import time


class Fighter:
  HEALTH = 100
  ATTACK = 10
  STAMINA = 100
  stun_state = False
  def __init__(self, name):
    self.name = name
  def display_stats(self):
    print(f"{self.name}'s health: {self.HEALTH}")
    print(f"{self.name}'s stamina: {self.STAMINA}")
    print(f"{self.name}'s attack: {self.ATTACK}")
  def normal_attack(self, obj):
    if self.STAMINA < 20:
      print('Not Enough Stamina')
      self.display_stats()
    else:
      obj.HEALTH -= self.ATTACK
      self.STAMINA -= 20
      print(f"{obj.name} - {obj.HEALTH} Health\n")
      self.display_stats()
  def sword_bash(self, obj):
    if self.STAMINA < 60:
      print('Not Enough Stamina')
      self.display_stats()
    else:
      obj.HEALTH -= self.ATTACK
      obj.stun_state = True
      self.STAMINA -= 60
      print(f"{obj.name} - {obj.HEALTH} Health\n")
      self.display_stats()
  def rest(self):
    print(f'{self.name} have rested for a turn')
    self.STAMINA += 50
    self.display_stats()
  def attack_up(self):
    print(f"{self.name} attack + 5")
    self.ATTACK += 5
    self.display_stats()
  def move_set(self, obj):
    print('Normal Attack: w\n', 'Sword Bash: a\n', 'Rest: s\n', 'Attack up: d')
    move = input('>>> ')
    if move == 'w':
      self.normal_attack(obj)
    if move == 'a':
      self.sword_bash(obj)
    if move == 's':
      self.rest()
    if move == 'd':
      self.attack_up()

class Computer(Fighter):
  def __init__(self, name):
    super().__init__(name)
    self.name = name
  def moves(self, obj):
    move_set = ["Attack", "Sword Bash", "Train"]
    if self.ATTACK == 50:
        move_set.remove("Train")
    action = random.choice(move_set)
    if self.STAMINA <= 0:
        action = 'Rest'
    if self.STAMINA < 20 and move_set == "Attack":
        action = 'Rest'
    if self.STAMINA < 60 and move_set == "Sword Bash":
        no_stamina = ["Attack", "Train"]
        action = random.choice(no_stamina)
    print(f"Computer has chosen {action}")
    if action == "Attack":
      self.normal_attack(obj)
    elif action == "Sword Bash":
      self.sword_bash(obj)
    elif action == "Train":
      self.attack_up()
    elif action == 'Rest':
      self.rest()


def game():
  name1 = input("Enter name player 1: ")
  fighter1 = Fighter(name1)
  name2 = input("Enter name player 2: ")
  fighter2 = Fighter(name2)
  while True:
    print(f"\n{fighter1.name}'s Turn")
    if fighter1.stun_state:
      fighter1.rest()
      fighter1.stun_state = False
    else:
      fighter1.move_set(fighter2)
    if fighter2.HEALTH <= 0:
      print(f"winner is {fighter1.name}")
      break
    print(f"\n{fighter2.name}'s Turn")
    if fighter2.stun_state:
      fighter2.rest()
      fighter2.stun_state = False
    else:
      fighter2.move_set(fighter1)
    if fighter1.HEALTH <= 0:
      print(f"winner is {fighter2.name}")
      break
  print("game over")
  again = input("Wanna play again?")
  if again == 'yes':
    game()


def vs_ai():
  name1 = input("Enter name player 1: ")
  fighter1 = Fighter(name1)
  name2 = input("Enter name for computer: ")
  fighter2 = Computer(name2)
  while True:
    print(f"\n{fighter1.name}'s Turn")
    if fighter1.stun_state:
      fighter1.rest()
      fighter1.stun_state = False
    else:
      fighter1.move_set(fighter2)
    if fighter2.HEALTH <= 0:
      print(f"winner is {fighter1.name}")
      break
    print(f"\n{fighter2.name}'s Turn")
    time.sleep(1)
    if fighter2.stun_state:
      fighter2.rest()
      fighter2.stun_state = False
    else:
      fighter2.moves(fighter1)
    if fighter1.HEALTH <= 0:
      print(f"winner is {fighter2.name}")
      break
  print("game over")
  again = input("Wanna play again?")
  if again == 'yes':
    vs_ai()


print("\tPlayer vs Player: 1\n\tPlayer vs Ai: 2")
game_type = input()
if game_type == '1':
  game()
elif game_type == '2':
  vs_ai()