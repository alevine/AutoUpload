import Tkinter
import Tkconstants
import tkFileDialog

class AutoUploadGUI(Tkinter.Frame):

    def __init__(self, root):
        Tkinter.Frame.__init__(self, root)

        button_options = {'fill': Tkconstants.BOTH, 'padx': 10, 'pady': 10}

        Tkinter.Button(self, text='Choose Capture Folder', command=self.openfolder).pack(**button_options)

    def openfolder(self):
        return tkFileDialog.askdirectory(**{'initialdir': '.', 'mustexist': True})


if __name__ == '__main__':
    root = Tkinter.Tk()
    root.geometry("400x400")
    root.resizable(False, False)
    AutoUploadGUI(root).pack()
    root.mainloop()