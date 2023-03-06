# import libraries
from tkinter import *
import tkinter as tk
from tkinter import font
from itertools import cycle
#import numpy as np

# define size of game board and other dimensions
size_of_window = 800 # in px
player_totem_size = (size_of_window/4- size_of_window/8)/2
totem_thickness = 40
totem_X_color = '#EE4035'
totem_Y_color = '#0492CF'

#initialize canvas
play_window = Tk()
play_window.title('Tic-Tac-Toe')
canvas = Canvas(play_window,bg="blue",width=size_of_window-100,height=size_of_window-100)
canvas.pack()

# Create display label
display = tk.Label(text="Ready?",
                font= font.Font(size=28, weight="bold"))
display.pack()

# create 3X3 grid
cells={}
for row in range(3):
    #set the size of cell on the grid
    display.rowconfigure(row, weight=1, minsize=50)
    display.columnconfigure(row, weight=1, minsize=75)
    for col in range(3):
        #create a button object for each cell
        button = tk.Button(
            master=canvas,
            text="",
            font=font.Font(size=36, weight="bold"),
            fg="black",
            width=3,
            height=2,
            highlightbackground="lightblue",
        )
        cells[button]=(row,col)
        # add cells to main window
        button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

