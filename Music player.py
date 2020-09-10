import pygame as py
import tkinter as tkr
import os


player=tkr.Tk()

player.title("audio player")

player.geometry("406x506")
os.chdir("C:\\Users\\Talha Habib\\Desktop\\song")
print(os.getcwd)
songlist=os.listdir()
volumee=tkr.Scale(player,from_=0.0 , to_=1.0,orient=tkr.HORIZONTAL,resolution=0.1)
playlist=tkr.Listbox(player,highlightcolor="blue",selectmode=tkr.SINGLE)
print(songlist)
for item in songlist:
    pos=0
    playlist.insert(pos,item)
    pos=pos+1
    

py.init()
py.mixer.init()
def Play():
    py.mixer.music.load(playlist.get(tkr.ACTIVE))
    py.mixer.music.play()
    py.mixer.music.set_volume(volumee.get())
    print (py.mixer.music.get_volume())
    print(volumee.get())    


    
def Exitplayer():
    py.mixer.music.stop()


def pause():
    py.mixer.music.pause()


def resume():
    py.mixer.music.unpause()



button1 = tkr.Button(player,  width = 5,height = 3,text="play",command=Play)
button2=tkr.Button(player,width=5,height=3,text="stop",command=Exitplayer)
button3=tkr.Button(player,width=5,height=3,text="pause",command=pause)
button4=tkr.Button(player,width=5,height=3,text="Resume",command=resume)




var=tkr.StringVar()
songtitle=tkr.Label(player,textvariable=var)



songtitle.pack()
button1.pack(fill="x")
button2.pack(fill="x")
button3.pack(fill="y")
button4.pack(fill="y")
volumee.pack(fill="y")
playlist.pack(fill="both",expand="yes")


player.mainloop()
    



