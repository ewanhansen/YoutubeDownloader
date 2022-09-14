from tkinter import *
import customtkinter as ctk
from resources.create_popup import Popup
from resources.download_video import DownloadVideo

#get app from tkinter
app = ctk.CTk()

#input variables
target_folder = StringVar()
download_type = StringVar(value='.mp3')

p = Popup() #new Popup object
d = DownloadVideo() #new DownloadVideo object

#command for download video button
def download_video():
    print(link_entry.get(), download_type, app)

    download = d.download(link_entry.get(), download_type.get(), app)
    print(link_entry.get(), download_type.get(), app)

#command for setting download type
def set_download_type(choice):
    download_button.configure(text='Download ' + choice)
    print(choice) 
        
#grid configuration
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure((0, 1), weight=1)

#create link input label
link_text = ''
link_label = ctk.CTkLabel(master=app, text="Video link:")
link_label.grid(row=0, column=0, sticky=W, padx=10, pady=20) #aligning to west because tkinter

#create link input entry
link_entry = ctk.CTkEntry(master=app, textvariable=link_text, width=300)
link_entry.grid(row=0, column=1, padx=10, pady=20)   

#create download select box
download_type_box = ctk.CTkComboBox(master=app, values=['.mp3', '.mp4'], command=set_download_type, variable=download_type)
download_type_box.grid(row=1, column=0, sticky='ew', padx=10, pady=20)

#create download button
download_button = ctk.CTkButton(master=app, text="Download .mp3", command=download_video, hover=True)
download_button.grid(row=1, column=1, sticky='ew', padx=10, pady=20)

#app custom things
app.title('Youtube Downloader')
app.resizable(False, False)
app.geometry('500x200')

#ctk theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app.mainloop()
