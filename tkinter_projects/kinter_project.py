from tkinter import *

import random
import time

import os
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

root = Tk()
root.title("Treasure Hunt")
root.geometry("400x300")
root.iconbitmap(BASE_DIR + "/treasure2.ico")

class Treasure_game:
    count = 0
    search = 1
    
    x_coord = random.randint(3, 200)
    y_coord = random.randint(3, 200)
    
    tree_img = PhotoImage(file=BASE_DIR + "/favicon_2.gif")
    decor_1 = PhotoImage(file=BASE_DIR + "/favicon_5.gif")
    decor_2 = PhotoImage(file=BASE_DIR + "/favicon_6.gif")
    
    def __init__(self, main):
        self.main = main
        
        self.treasure_map = Canvas(self.main, bg="#f3c474", width=200, height=200)
        self.treasure_map.create_rectangle(2, 2, 201, 201)
        
        for i in range(8):
            self.treasure_map.create_image(random.randint(20, 180), random.randint(20, 180), image=self.decor_1)
        
        for i in range(7):
            self.treasure_map.create_image(random.randint(10, 190), random.randint(10, 190), image=self.decor_2)
        
        self.treasure_map.bind("<Button-1>", self.game)
        
        for i in range(15):
            self.treasure_map.create_image(random.randint(10, 190), random.randint(10, 190), image=self.tree_img)
        
        self.top_label = Label(self.main, text="Click on the map to find the treasure")
        
        self.coord_label = Label(self.main)
        
        self.parrot_button = Button(self.main, text="Search", state=DISABLED, command=self.parrot_search)
        
        self.reset = Button(self.main, text="New Game", command=self.new_game)
        
        self.reset.pack()
        self.top_label.pack()
        self.treasure_map.pack()
        self.coord_label.pack()
        self.parrot_button.pack()    
    
    def new_game(self):
        self.count = 0
        self.search = 1
        
        self.x_coord = random.randint(3, 200)
        self.y_coord = random.randint(3, 200)
        
        self.top_label.destroy()
        self.treasure_map.destroy()
        self.coord_label.destroy()
        self.parrot_button.destroy()
        
        self.treasure_map = Canvas(self.main, bg="#f3c474", width=200, height=200)
        self.treasure_map.create_rectangle(2, 2, 201, 201)
        
        self.treasure_map.bind("<Button-1>", self.game)
        
        for i in range(7):
            self.treasure_map.create_image(random.randint(20, 180), random.randint(20, 180), image=self.decor_1)
        
        for i in range(8):
            self.treasure_map.create_image(random.randint(10, 190), random.randint(10, 190), image=self.decor_2)
        
        for i in range(15):
            self.treasure_map.create_image(random.randint(10, 190), random.randint(10, 190), image=self.tree_img)
        
        self.top_label = Label(self.main, text="Click on the map to find the treasure")
        
        self.coord_label = Label(self.main)
        
        self.parrot_button = Button(self.main, text="Search", state=DISABLED, command=self.parrot_search)
        
        self.top_label.pack()
        self.treasure_map.pack()
        self.coord_label.pack()
        self.parrot_button.pack()
        
    def game(self, event):
        text = (f"You clicked at x: {event.x} y: {event.y}. You are {abs(event.x-self.x_coord)} away from x and {abs(event.y-self.y_coord)} from y.")
        self.coord_label.config(text=text)
        self.count += 1
               
        if abs(event.x-self.x_coord) < 5 and abs(event.y-self.y_coord) < 5:
            self.coord_label.config(text="You have found the treasure!")
            self.top_label.config(text="You have won!!")
            self.treasure_map.create_line(self.x_coord-5, self.y_coord-5, self.x_coord+5, self.y_coord+5, fill="red", width=2)
            self.treasure_map.create_line(self.x_coord-5, self.y_coord+5, self.x_coord+5, self.y_coord-5, fill="red", width=2)
            print(f"It took {self.count} tries to find the treasure")
                                     
        if self.count >= 10 and self.search == 1:
            self.parrot_button["state"] = NORMAL
    
    def parrot_search(self):
        if self.search == 1:
            self.treasure_map.create_oval(self.x_coord-random.randint(20, 40), self.y_coord-random.randint(20, 40), self.x_coord+random.randint(20, 40), self.y_coord+random.randint(20, 40))
            self.count += 1
            self.search -= 1
        


def main_game():     
    game = Treasure_game(root) 
 

if __name__ == '__main__':
    main_game()
    root.mainloop()