import autoupload
import multiprocessing
from Tkinter import Frame, Button, Tk, Label, Text
from Tkconstants import BOTH, END
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

        self.init_ui()

    def init_ui(self):
        self.parent.title('AutoUpload')

        self.rowconfigure(2, pad=20)
        self.columnconfigure(0, pad=10)
        self.columnconfigure(1, pad=10)

        self.title = Label(self, text="AutoUpload by Aaron Levine", font='Arial 12', background='white', pady=10)
        self.title.grid(row=0, columnspan=2)

        self.folderChoice = Text(self, font='Arial 8', width=50, height=2, state='disabled')
        self.folderChoice.grid(row=1, column=1)

        self.chooseButton = Button(self, text='Choose Capture Folder', command=self.openfolder, width=20)
        self.chooseButton.grid(row=1)

        self.startButton = Button(self, text='Start', command=self.startapp, width=20)
        self.startButton.grid(row=2, column=0)

        self.stopButton = Button(self, text='Stop', command=self.stopapp, state='disabled', width=20)
        self.stopButton.grid(row=2, column=1, sticky='E', padx=5)

        self.pack(fill=BOTH, expand=1)

    def openfolder(self):
        self.folderChoice.config(state='normal')
        self.folderChoice.delete('1.0', END)
        self.folderChoice.tag_configure('tag-center', justify='center')
        self.folderChoice.insert(END, askdirectory(**{'initialdir': '.', 'mustexist': True}), 'tag-center')
        self.folderChoice.config(state='disabled')

    def startapp(self):
        global upload_process
        upload_process = multiprocessing.Process(target=autoupload.main,
                                                 args=(self.folderChoice.get('1.0', END).strip(),))
        upload_process.start()
        self.startButton.config(state='disabled')
        self.stopButton.config(state='normal')

    def stopapp(self):
        upload_process.terminate()
        self.stopButton.config(state='disabled')
        self.startButton.config(state='normal')


if __name__ == '__main__':
    root = Tk()
    root.resizable(False, False)
    AutoUploadGUI(root)
    root.mainloop()
