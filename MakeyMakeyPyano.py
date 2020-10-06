import tkinter as tk
import subprocess
from threading import Thread

def keypressesc(event):
    root.destroy()
    
def keypressup(event):
    play = Thread(target = subprocess.call, args = ([["afplay", "C.wav"]]))
    play.start()
    
def keypressdown(event):
    play = Thread(target = subprocess.call, args = ([["afplay", "D.wav"]]))
    play.start()
    
def keypressright(event):
    play = Thread(target = subprocess.call, args = ([["afplay", "E.wav"]]))
    play.start()
    
def keypressleft(event):
    play = Thread(target = subprocess.call, args = ([["afplay", "F.wav"]]))
    play.start()
    
def keypressspace(event):
    play = Thread(target = subprocess.call, args = ([["afplay", "G.wav"]]))
    play.start()

def keypressw(event):
    play = Thread(target = subprocess.call, args = ([["afplay", "A.wav"]]))
    play.start()

def keypressa(event):
    play = Thread(target = subprocess.call, args = ([["afplay", "B.wav"]]))
    play.start()

def keypresss(event):
    play = Thread(target = subprocess.call, args = ([["afplay", "C2.wav"]]))
    play.start()

def keypressd(event):
    play = Thread(target = subprocess.call, args = ([["afplay", "D2.wav"]]))
    play.start()

def keypressf(event):
    play = Thread(target = subprocess.call, args = ([["afplay", "E2.wav"]]))
    play.start()

def keypressg(event):
    play = Thread(target = subprocess.call, args = ([["afplay", "F2.wav"]]))
    play.start()
    
root = tk.Tk()
root.bind('<Up>', keypressup)
root.bind('<Down>', keypressdown)
root.bind('<Right>', keypressright)
root.bind('<Left>', keypressleft)
root.bind('<space>', keypressspace)
root.bind('<Escape>', keypressesc)
root.bind('<w>', keypressw)
root.bind('<a>', keypressa)
root.bind('<s>', keypresss)
root.bind('<d>', keypressd)
root.bind('<f>', keypressf)
root.bind('<g>', keypressg)
root.mainloop()
