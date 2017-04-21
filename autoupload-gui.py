from Tkinter import Frame, Button, Tk, Label
from Tkconstants import BOTH
from tkFileDialog import askdirectory


class AutoUploadGUI(Frame):

    def __init__(self, parent):
        self.parent = parent
        self.stopButton = None
        self.startButton = None
        self.chooseButton = None
        self.folderChoice = None
        self.title = None

        Frame.__init__(self, parent, background='white')

        self.initUI()

    def initUI(self):
        self.parent.title('AutoUpload')

        self.rowconfigure(2, pad=20)
        self.columnconfigure(0, pad=10)
        self.columnconfigure(1, pad=10)

        self.title = Label(self, text="AutoUpload by Aaron Levine", font='Arial 12', background='white', pady=10)
        self.title.grid(row=0, columnspan=2)

        self.folderChoice = Label(self, text='', font='Arial 7', width=35, height=2)
        self.folderChoice.grid(row=1, column=1)

        self.chooseButton = Button(self, text='Choose Capture Folder', command=self.openfolder, width=20)
        self.chooseButton.grid(row=1)

        self.startButton = Button(self, text='Start', command=None, background='green',
                                  activebackground='green', width=20)
        self.startButton.grid(row=2, column=0)

        self.stopButton = Button(self, text='Stop', command=None, state='disabled',
                                 background='red', activebackground='red', width=20)
        self.stopButton.grid(row=2, column=1)

        self.pack(fill=BOTH, expand=1)

    def openfolder(self):
        self.folderChoice['text'] = askdirectory(**{'initialdir': '.', 'mustexist': True})


if __name__ == '__main__':
    root = Tk()
    root.resizable(False, False)
    AutoUploadGUI(root)
    root.mainloop()