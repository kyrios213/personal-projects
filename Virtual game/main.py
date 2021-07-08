import sqlite3
import csv
import time

conn = sqlite3.connect("database.sqlite")
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Players (
    name TEXT ,
    save_file VARCHAR(50)  ) ''')


class Pet():
    ALIVE = True

    def __init__(self, name, race, hunger=100,stamina=100,happiness=100,age=0.0):
        self.name = name
        self.race = race
        self.hunger = hunger
        self.stamina = stamina
        self.happiness = happiness
        self.age = age

    def pet_state(self):
        pet_state = ">u<"
        if self.hunger < 50 or self.stamina < 50 or self.happiness < 50:
            pet_state = ">~<"
        if self.hunger < 30 or self.stamina < 30 or self.happiness < 30:
            pet_state = "T~T"
        if self.hunger <= 0 or self.stamina <= 0 or self.happiness <= 0:
            pet_state = "X~X"
        print(pet_state)

    def feed_pet(self):
        self.hunger += 60
        if self.hunger > 100:
            self.hunger = 100
        print(">0<")
        time.sleep(1)
        print(">M<")
        time.sleep(1)
        self.pet_state()

    def sleep_pet(self):
        if self.stamina > 70:
            self.happiness -= 20
        self.stamina += 50
        self.hunger -= 20
        if self.stamina > 100:
            self.stamina = 100
        print("-_- zzzzz")
        time.sleep(1)
        print("-0- ....")
        time.sleep(1)
        self.pet_state()

    def play_with_pet(self):
        self.happiness += 40
        self.hunger -= 20
        self.stamina -= 20
        if self.happiness > 100:
            self.happiness = 100
        print("OuO !!!!")
        time.sleep(1)
        self.pet_state()

    def wait(self):
        self.hunger -= 10
        self.happiness -= 10
        self.stamina += 10
        if self.stamina > 100:
            self.stamina = 100
        print("OuO .")
        time.sleep(0.5)
        print("OuO ..")
        time.sleep(0.5)
        print("OuO ...")
        time.sleep(0.5)
        print("OuO ....")


def save_game(profile, name, race, data1, data2, data3, data4, data5):
    save_data = (name, race, data1, data2, data3, data4, data5)
    filename = 'data.csv'
    with open(filename, 'w+') as save:
        writer = csv.writer(save)
        writer.writerow(save_data)
    try:
        cur.execute('''SELECT name FROM Players WHERE name = ?''', (profile,))
        select = cur.fetchone()[0]
        if len(select) < 0:
            cur.execute('''
                    UPDATE Players SET save_file = ? WHERE name = ?''', (filename, profile))
    except:
        cur.execute('''
        INSERT INTO Players (name, save_file) VALUES (?, ?)''', (profile, filename))
    conn.commit()


def load_game(name):
    cur.execute('''SELECT save_file FROM Players WHERE name = ?''', (name,))
    save_file = cur.fetchone()[0]
    if save_file is None:
        return None
    with open(save_file, 'r') as saves:
        reader = csv.reader(saves)
        for row in reader:
            if len(row) == 0:
                continue
            return row


def print_profile():
    cur.execute('''SELECT name FROM Players''')
    x = cur.fetchall()
    for y in x:
        for z in y:
            if z is None:
                continue
            print(z)


def new_game():
    profile_name = input("Enter your name: ")
    pet_name = input("Enter your pet's name: ")
    print("Good")
    pet_race = input("Enter your pet's race ")
    print("Nice")
    virtual_pet = Pet(pet_name, pet_race)
    while virtual_pet.ALIVE:
        print(f"Name: {virtual_pet.name}")
        print(f"Race: {virtual_pet.race}")
        print(f"Hunger: {virtual_pet.hunger}")
        print(f"Happiness: {virtual_pet.happiness}")
        print(f"Stamina: {virtual_pet.stamina}")
        print(f"Age: {virtual_pet.age}")
        virtual_pet.pet_state()
        command = input("Enter a command: \nFeed Pet: [f]\nPlay with pet: [p]\nSleep: [s]\nWait: [w]\n"
                        "Save&Quit: [q]\n>>>")
        if command == 'f':
            virtual_pet.feed_pet()
            print("Burp")
        elif command == 's':
            virtual_pet.sleep_pet()
        elif command == 'p':
            virtual_pet.play_with_pet()
        elif command == 'w':
            virtual_pet.wait()
        elif command == 'q':
            save_game(profile_name, pet_name, pet_race, virtual_pet.hunger, virtual_pet.stamina, virtual_pet.happiness,
                      virtual_pet.age, virtual_pet.ALIVE)
            break
        else:
            virtual_pet.wait()
        if virtual_pet.hunger <= 0 or virtual_pet.stamina <= 0 or virtual_pet.happiness <= 0:
            print(f"Name: {virtual_pet.name}")
            print(f"Race: {virtual_pet.race}")
            print(f"Hunger: {virtual_pet.hunger}")
            print(f"Happiness: {virtual_pet.happiness}")
            print(f"Stamina: {virtual_pet.stamina}")
            print(f"Age: {virtual_pet.age}")
            virtual_pet.pet_state()
            virtual_pet.ALIVE = False
        virtual_pet.age += 0.2
        print("===============================================")
        time.sleep(1)
    print("Game over")


def loaded_game(profile, data):
    virtual_pet = Pet(data[0], data[1], int(data[2]), int(data[3]), int(data[4]), float(data[5]))
    virtual_pet.ALIVE = bool(data[6])
    while virtual_pet.ALIVE:
        print(f"Name: {virtual_pet.name}")
        print(f"Race: {virtual_pet.race}")
        print(f"Hunger: {virtual_pet.hunger}")
        print(f"Happiness: {virtual_pet.happiness}")
        print(f"Stamina: {virtual_pet.stamina}")
        print(f"Age: {virtual_pet.age}")
        virtual_pet.pet_state()
        command = input("Enter a command: \nFeed Pet: [f]\nPlay with pet: [p]\nSleep: [s]\nWait: [w]\n"
                        "Save&Quit: [q]\n>>>")
        if command == 'f':
            virtual_pet.feed_pet()
            print("Burp")
        elif command == 's':
            virtual_pet.sleep_pet()
        elif command == 'p':
            virtual_pet.play_with_pet()
        elif command == 'w':
            virtual_pet.wait()
        elif command == 'q':
            save_game(profile, virtual_pet.name, virtual_pet.race, virtual_pet.hunger, virtual_pet.stamina,
                      virtual_pet.happiness,
                      virtual_pet.age, virtual_pet.ALIVE)
            break
        else:
            virtual_pet.wait()
        if virtual_pet.hunger <= 0 or virtual_pet.stamina <= 0 or virtual_pet.happiness <= 0:
            print(f"Name: {virtual_pet.name}")
            print(f"Race: {virtual_pet.race}")
            print(f"Hunger: {virtual_pet.hunger}")
            print(f"Happiness: {virtual_pet.happiness}")
            print(f"Stamina: {virtual_pet.stamina}")
            print(f"Age: {virtual_pet.age}")
            virtual_pet.pet_state()
            virtual_pet.ALIVE = False
        virtual_pet.age += 0.2
        print("===============================================")
        time.sleep(1)
    print("Game over")


def virtual_pet_game():
    print('Welcome')
    game = input("new game: [n]\nload game: [l]\n>>>")
    if game == 'n':
        new_game()
    elif game == 'l':
        print_profile()
        profile = input('Select Profile: ')
        load_data = load_game(profile)
        if load_data is None:
            print("No save file")
            new_game()
        loaded_game(profile, load_data)
    else:
        print("Invalid Option")
    again = input("Wanna play again: y or n\n")
    if again == 'y':
        virtual_pet_game()


virtual_pet_game()