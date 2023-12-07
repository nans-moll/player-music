from pygame import mixer
from tkinter import *
from PIL import Image, ImageTk
import os


root = Tk() 
root.title('Music player')

def playsong():
    currentsong = playlist.get(ACTIVE)
    mixer.music.load(currentsong)
    mixer.music.play()

def pausesong():
    mixer.music.pause()

def nextsong():
    if playlist.size() > 1:
        current_index = playlist.curselection()
        next_index = current_index[0] + 1 if current_index else 0
        if next_index < playlist.size():
            playlist.selection_clear(0, END)
            playlist.selection_set(next_index)
            playsong()

def previoussong():
    if playlist.size() > 1:
        current_index = playlist.curselection()
        prev_index = current_index[0] - 1 if current_index else 0
        if prev_index >= 0:
            playlist.selection_clear(0, END)
            playlist.selection_set(prev_index)
            playsong()



mixer.init() 
playlist = Listbox(root, selectmode=SINGLE, bg="black", fg="white", font=('arial', 15), width=40) 
playlist.grid(columnspan=5)
os.chdir = os.listdir()
#os.chdir("./musique/sons/")
songs = os.listdir("./musique")


for s in songs: 
    playlist.insert(END, s)

play_img = ImageTk.PhotoImage(Image.open("./images/play.png").resize((30, 30)))
stop_img = ImageTk.PhotoImage(Image.open("./images/stop.png").resize((30, 30)))
next_img = ImageTk.PhotoImage(Image.open("./images/next.png").resize((30, 30)))
prev_img = ImageTk.PhotoImage(Image.open("./images/prev.png").resize((30, 30)))



prevbtn = Button(root, image=prev_img, command=previoussong)
prevbtn.grid(row=1, column=0)

playbtn = Button(root, image=play_img, command=playsong)
playbtn.grid(row=1, column=1)

stopbtn = Button(root, image=stop_img, command=pausesong)
stopbtn.grid(row=1, column=2)

nextbtn = Button(root, image=next_img, command=nextsong)
nextbtn.grid(row=1, column=3)



mainloop() 