class Game():
  def __init__(self, name, genre):
    self.name = name
    self.genre = genre
  def announce_game(self):
    print(f"Game name is: {self.name}")
    print(f"Game genre is: {self.genre}")
