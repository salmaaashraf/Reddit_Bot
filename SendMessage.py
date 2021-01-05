import tkinter
from tkinter import *
from tkinter import messagebox as mbox
from tkinter.font import Font, BOLD

from ReplyToPosts import send_message, CreateInstance


class SendMessage:
    def __init__(self):
        self.top = Tk()
        self.top.title("Send Messsage")
        self.top.geometry("400x450")
        self.top.eval('tk::PlaceWindow . center')
        '''filename = PhotoImage(file = "D:\FCIA-HU\level3\CONCEPTS\sections\hana.png")
        background_label = Label(self.top, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        '''
        # creating label
        self.UserName = Label(self.top, text="UserName ", font='Helvetica 10 bold')
        self.UserName.pack()
        self.UserName.place(x=50, y=20)
        self.e1 = tkinter.Text(self.top, width=20, height=2, bg='white', fg='black')
        self.e1.pack()
        self.e1.place(x=50, y=50)
        # creating label
        labelFont3 = Font(family="Helvetica", size=10, weight=BOLD)
        Titel = Label(self.top, text="Titel", font=labelFont3)
        Titel.pack()
        Titel.place(x=50, y=105)
        self.e2 = tkinter.Text(self.top, width=20, height=2, bg='white', fg='black')
        self.e2.pack()
        self.e2.place(x=50, y=135)
        Subject = Label(self.top, text="Message", font=labelFont3)
        Subject.pack()
        Subject.place(x=50, y=190)
        self.e3 = tkinter.Text(self.top, width=30, height=8, bg='white', fg='black')
        self.e3.pack()
        self.e3.place(x=50, y=220)
        sbmitbtn = tkinter.Button(self.top, text="send", fg='white', bg="black", activebackground='white',
                                  activeforeground='black',
                                  height=1, font='Helvetica 10 bold', command=self.helloCallBack)
        sbmitbtn.pack()
        sbmitbtn.place(x=50, y=400, height=30, width=300)
        self.top.mainloop()

    def helloCallBack(self):
        # put here what we want to do after click submit button
        if (self.e2.get("1.0", 'end-1c') == '') or (self.e1.get("1.0", 'end-1c') == ''):
            mbox.showerror('Python Error Message', 'Username and title are required')
        else:
            reddit = CreateInstance()
            send_message(reddit, self.e1.get("1.0", 'end-1c'), self.e2.get("1.0", 'end-1c'),self.e3.get("1.0", 'end-1c'))
            self.top.destroy()
