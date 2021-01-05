import tkinter
from tkinter import *
from tkinter import messagebox as mbox
from tkinter.font import Font, BOLD

from ReplyToPosts import *


class Reply:
    def __init__(self):
        self.top = Tk()
        self.top.title("Reply on a comment")
        self.top.geometry("400x400")
        self.top.eval('tk::PlaceWindow . center')
        # creating label
        self.keyword_search = Label(self.top, text="keyword_search", font='Helvetica 10 bold')
        self.keyword_search.pack()
        self.keyword_search.place(x=50, y=50)
        self.e1 = tkinter.Text(self.top, width=20, height=2, bg='white', fg='black')
        self.e1.pack()
        self.e1.place(x=50, y=90)
        # creating label
        labelFont3 = Font(family="Helvetica", size=10, weight=BOLD )
        Answer = Label(self.top, text="Answer", font=labelFont3)
        Answer.pack()
        Answer.place(x=50, y=160)
        self.e2 = tkinter.Text(self.top, width=20, height=2, bg='white', fg='black')
        self.e2.pack()
        self.e2.place(x=50, y=200)
        labelFont2 = Font(family="Helvetica", size=10, weight=BOLD,underline=1)
        line=Label(self.top, text="                                                                                  ", font=labelFont2,fg="white")
        line.pack()
        line.place(x=20, y=260)
        sbmitbtn=tkinter.Button(self.top, text="Submit",fg='white',bg="black", activebackground='white', activeforeground='black',
                          height=1, font='Helvetica 10 bold', command=self.helloCallBack)
        sbmitbtn.pack()
        sbmitbtn.place(x=50, y=320, height=30, width=300)
        self.top.mainloop()

    def helloCallBack(self):
        # put here what we want to do after click submit button
        reddit = CreateInstance()
        posts_replied_to = Read_ID_Post_From_File()
        if (self.e2.get("1.0",'end-1c')=='') or (self.e1.get("1.0",'end-1c')==''):
             mbox.showerror('Python Error Message', 'fill all fields it\'s required' )
        else:
            posts_replied_to=Reply_To_Posts(reddit, posts_replied_to, self.e1.get("1.0",'end-1c'),self.e2.get("1.0",'end-1c'))
            Update_File(posts_replied_to)



