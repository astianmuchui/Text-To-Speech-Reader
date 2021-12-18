import tkinter
from tkinter import *
from tkinter import messagebox
import pyttsx3
def read():
    if label.get() == '':
        messagebox.showerror("Please write some text to be read")
    else:
        engine = pyttsx3.init()
        engine.say(label.get())
        engine.runAndWait()


sys = Tk()
sys.configure(background="black")
sys.title("Text to speech")
label = StringVar()
int_label = Label(sys, text="Type to get started",font=("fantasy",18),fg="#2fa4e7",pady=15,padx=5)
int_label.configure(background="black")
int_label.grid(row=1,column=1,sticky=W)
_input = Entry(sys, textvariable=label, border=1, width=25)
_input.configure(background="skyblue")
_input.grid(row=3,column=1, sticky=W,padx=40,pady=80)
btn = Button(sys, text="Read text", width=14, background="#083a55",command=read)
btn.grid(row=3,column=2, sticky=W,padx=0,pady=80)
sys.geometry("500x500")
sys.mainloop()