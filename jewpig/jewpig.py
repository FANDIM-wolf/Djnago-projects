from tkinter import *
from tkinter import messagebox
from PIL import Image , ImageTk
import os 
import pyglet
from threading import Thread
from time import sleep

def on_closing():
    if messagebox.askokcancel("EXIT", "EXIT?"):
        tk.destroy()
#sounds of jew pig
def pig_talks():
    sound_of_pig=pyglet.resource.media("01011.mp3")
    sound_of_pig.play()
    pyglet.app.run()
def main():
    #main window 
    tk = Tk()
    tk.protocol("WM_DELETE_WINDOW", on_closing)
    tk.title("Jew pig")
    tk.resizable(0, 0)
    tk.wm_attributes("-topmost", 1)
    canvas = Canvas(tk, width=860, height=500, bd=0, highlightthickness=0)
    canvas.pack()

    #create obiject of image
    our_image = PhotoImage(file="jjj.png")
    #our_image = our_image.subsample(2,2) #decrease in 2 times
    our_label = Label(tk)
    our_label.image = our_image
    our_label['image'] = our_label.image
    our_label.place(x=50,y=50)
    
    #end
    tk.mainloop()

#it creates threads 

th1_pig_sound = Thread(target=pig_talks)
th2_window    = Thread(target=main)

#start threads

th1_pig_sound.start()
th2_window.start()

th1_pig_sound.join()
th2_window.join()

