import tkinter
from tkinter import *
from Reply import *
from SendMessage import SendMessage


class Start:
    def __init__(self):
        self.root = Tk()
        self.root.title("Subreddit Monitor")
        self.root.geometry("400x400")
        Button1 = tkinter.Button(self.root, text="Replay on a comment", fg='white', bg="black",
                                 activebackground='white', activeforeground='black', height=1, font='Helvetica 10 bold',
                                 command=self.replay_on)
        Button2 = tkinter.Button(self.root, text="Send a message", fg='white', bg="black", activebackground='white',
                                 activeforeground='black', height=1, font='Helvetica 10 bold',
                                 command=self.send_message)
        Button1.pack()
        Button1.place(x=50, y=80, height=30, width=300)
        Button2.pack()
        Button2.place(x=50, y=250, height=30, width=300)
        self.root.mainloop()

    def replay_on(self):
        self.root.destroy()
        Reply()

    def send_message(self):
        self.root.destroy()
        SendMessage()



