import csv
from game import janken_game
from game2 import Game

def save_profile(name, data):
  filename = name + ".csv"
  save = [data]
  with open(filename, 'w+') as save_data:
    writer = csv.writer(save_data)
    writer.writerow(save)

def load_profile(name):
  filename = name + ".csv"
  try:
    with open(filename, 'r+') as save_data:
      reader = csv.reader(save_data)
      for saves in reader:
        data = saves[0]
      return data
  except:
    return None

def main_game():
  profile = input("Enter profile name: ")
  data = 0
  if load_profile(profile) != None:
    print("Profile aldready exists")
    load = input("Load Game? [y] or [n]\n\t")
    if load == 'y':
      data = int(load_profile(profile))
    else:
      data = 0
  while True:
    data += 1
    save_profile(profile, data)
    move = input("Enter any key: ")
    if len(move) != 0:
      print(f"data = {data}")
    else:
      break
  print("End")

if __name__ == "__main__":
    game = Game("Janken", "Text-Based")
    game.announce_game()
    janken_game()