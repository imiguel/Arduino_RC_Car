from Tkinter import *
import methods

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="QUIT", fg="red",command=frame.quit)
        self.button.pack()

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)



        self.hi_there.pack()


    ############################### Acoes dos botoes
    def say_hi(self):



        #tkMessageBox.FunctionName(title, message [, options])
        methods.helloWorld()


if __name__ == "__main__":
    root = Tk()
    root.minsize(700, 500)
    root.maxsize(500, 700)
    app = App(root)
    root.mainloop()