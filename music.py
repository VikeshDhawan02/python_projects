#importing required libraries
import pygame
from pygame import mixer
from tkinter import *
import os

#defining required funcitons like : play, pause, stop, resume
def playsong():
    currentsong=playlist.get(ACTIVE) #Getting the songs from our playlist
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("Playing")
    mixer.music.play() #playing the selected song

def pausesong():
    songstatus.set("Paused")
    mixer.music.pause() #pausing the selected song

def stopsong():
    songstatus.set("Stopped")
    mixer.music.stop() #stoping the selected song

def resumesong():
    songstatus.set("Resuming")
    mixer.music.unpause()     #resuming the current song

#name of music player
root=Tk()
root.title("Vikesh's Music Player")

mixer.init()
songstatus=StringVar()
songstatus.set("choosing")

#playlist loading and other designing stuff

playlist=Listbox(root,selectmode=SINGLE,bg="orange",fg="Black",font=('Helvetica',15),width=40)
playlist.grid(columnspan=5)

os.chdir(r'C:\Users\VIKESH\Documents\python\music_playlist')
songs=os.listdir()
for s in songs:
    playlist.insert(END,s)

playbtn=Button(root,text="Play",command=playsong)
playbtn.config(font=('Helvetica',20),bg="white",fg="green",padx=7,pady=7)
playbtn.grid(row=1,column=0)

pausebtn=Button(root,text="Pause",command=pausesong)
pausebtn.config(font=('Helvetica',20),bg="black",fg="white",padx=7,pady=7)
pausebtn.grid(row=1,column=1)

stopbtn=Button(root,text="Stop",command=stopsong)
stopbtn.config(font=('Helvetica',20),bg="white",fg="red",padx=7,pady=7)
stopbtn.grid(row=1,column=2)

Resumebtn=Button(root,text="Resume",command=resumesong)
Resumebtn.config(font=('Helvetica',20),bg="black",fg="white",padx=7,pady=7)
Resumebtn.grid(row=1,column=3)

mainloop()