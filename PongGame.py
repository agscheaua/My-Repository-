from email.mime import image
import random
from cgitb import reset, text
from cProfile import label
from ctypes import windll
from fileinput import close
from tabnanny import check
from time import time
from tkinter import *
from turtle import resetscreen, width, window_height, window_width
from pyparsing import anyCloseTag
from setuptools import Command
from traitlets import Int
import sys
import time

GAME_WIDTH = 1250
GAME_HEIGHT = 850

xVelocity = 10
yVelocity = 10

 
def NewGame():
    pass
    

def ExitGame():
    window.destroy()


def move_up_player1(event):
    player1label.place(x=player1label.winfo_x(),y=player1label.winfo_y()-20)
    

def move_down_player1(event):
    player1label.place(x=player1label.winfo_x(),y=player1label.winfo_y()+20)
    

def move_up_player2(event):
    player2label.place(x=player2label.winfo_x(),y=player2label.winfo_y()-20)


def move_down_player2(event):
    player2label.place(x=player2label.winfo_x(),y=player2label.winfo_y()+20)



#----------------------------------------------------------------------------- Window 

window = Tk()
window.title("Pong Game")
window.resizable(0,0)
window.geometry(f"1250x850+335+70")
window.config(bg="black")

#------------------------------------------------------------------------------ Menu

menubar = Menu(window)
window.config(menu=menubar)

menubar.add_command(label="New Game", command=NewGame)
menubar.add_command(label="Exit", command=ExitGame)

#------------------------------------------------------------------------------ Player Label

player1label = Label(window, width=4, height=8, bg="yellow", fg="black")
player1label.place(x=10,y=350)

player2label = Label(window, width=4, height=8, bg="yellow", fg="black")
player2label.place(x=1205,y=350)

#----------------------------------------------------------------------------- CapyBall Label

ballimage = PhotoImage(file = "D:\Capybara2.png")
canvas = Canvas(window,width=GAME_WIDTH,height=GAME_HEIGHT)
canvas.pack()
Capyballlabel = canvas.create_image(0,0,image=ballimage)
#Capyballlabel = Label(window, image=ballimage, bg="black")
#Capyballlabel.pack()

#----------------------------------------------------------------------------- Window Binding

window.bind("<w>",move_up_player1)
window.bind("<s>",move_down_player1)
window.bind("<Up>",move_up_player2)
window.bind("<Down>",move_down_player2)


#-----------------------------------------------------------------------------

capyballlabel_width = ballimage.width()
capyballlabel_height = ballimage.height()

while True:
    coordinates = canvas.coords(Capyballlabel)
    if(coordinates[0]>=(GAME_WIDTH-capyballlabel_width) or coordinates[0]<0):
        xVelocity = -xVelocity
    if(coordinates[1]>=(GAME_HEIGHT-capyballlabel_height) or coordinates[1]<0):
        yVelocity = -yVelocity

    canvas.move(Capyballlabel,xVelocity,yVelocity)
    window.update()
    time.sleep(0.01)


window.mainloop()
