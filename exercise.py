from tkinter import Tk,Radiobutton,Grid,Pack,Label,Checkbutton

class Window(object):

    def __init__(self):
        self.window = Tk()
        self._radio_module()
        self.label_module()
        self.check_module()
        self.window.mainloop()

    def _radio_module(self):
        self.radio1 = Radiobutton(self.window, text='ssss')
        self.radio1.pack()

    def label_module(self):
        self.label1 = Label(self.window,text='sss')
        self.label1.pack()

    def check_module(self):
        self.check1 = Checkbutton(self.window,text='asd')
        self.check1.pack()

if __name__ == '__main__':
    window = Window()