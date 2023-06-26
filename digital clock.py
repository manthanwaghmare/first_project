from tkinter import Tk
from tkinter import Label
import time

window =Tk() #to display screen
window.title("Digital Clock") #the Title

#define function to show time
def clock_time():
    show_time = time.strftime("%H : %M : %S : %p" )
    clock_screen.config(text=show_time)
    clock_screen.after(1144,clock_time) # size of window

clock_screen = Label(window, font=('FreeMono',78), bg=('black'), fg=('snow')) #attributes of clock screen
clock_screen.pack(anchor="center")


clock_time()
window.mainloop()