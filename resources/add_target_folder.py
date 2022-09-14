from tkinter import filedialog

class TargetFolder():
    def GetTargetFolder(self):
        #filedialog for directory input and return it
        target_folder = filedialog.askdirectory(initialdir='/', title='Choose target folder...')
        return target_folder 