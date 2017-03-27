from Tkinter import *


class App(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.button1 = Button(master, text="BYE!", fg="red", command=self.quit)
        self.button1.pack(side=LEFT)
        self.button2 = Button(master, text="Say something!", command=self.say)
        self.button2.pack(side=LEFT)

    def say(self):
        print "...something."


window = Tk()
app = App(window)
window.mainloop()
