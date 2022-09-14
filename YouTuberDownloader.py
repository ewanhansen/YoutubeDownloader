from cgitb import text
from doctest import master
from inspect import _empty
from queue import Empty
import string
from tkinter import *
import tkinter
import customtkinter as ctk
import os
from tkinter import filedialog
from pytube import YouTube

#get app from tkinter
app = ctk.CTk()

target_folder = StringVar()
download_type = StringVar(value='.mp3')

def addTargetFolder():
    #filedialog for directory input and return it
    target_folder = filedialog.askdirectory(initialdir='/', title='Choose target folder...')
    return target_folder

def downloadVideo():
    #get link text from entry and target folder from addTargetFolder()
    link_text = link_entry.get()
    target_folder = addTargetFolder()

    #if no link input
    if link_text == '':
        print("No link input!")
        return

    #if no target folder
    if target_folder == '':
        print('No destination folder!')
        return

    #make youtube object and set audio filtering if type is .mp3
    yt = YouTube(link_text)
    if download_type.get() == '.mp3':
        audio = yt.streams.filter(only_audio=True).first()
        saved_file = audio.download(target_folder)
        base, ext = os.path.splitext(saved_file)
        new_file = base + '.mp3'
        os.rename(saved_file, new_file)
    else:
        #get highest res and download it to target folder as .mp3
        video = yt.streams.get_highest_resolution()
        video.download(target_folder)
    
    #get highest res and download it to target folder
    yd = yt.streams.get_highest_resolution()
    yd.download(target_folder)

    print('Downloaded ' + yd.title + ' to ' + target_folder)

def downloadTypeCallback(choice):
    download_button.configure(text='Download ' + choice)
    print(choice)

app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure((0, 1), weight=1)

#create link input label
link_text = ''
link_label = ctk.CTkLabel(master=app, text="Video link:")
link_label.grid(row=0, column=0, sticky=W) #aligning to west because tkinter

#create link input entry
link_entry = ctk.CTkEntry(master=app, textvariable=link_text, width=300)
link_entry.grid(row=0, column=1)   

download_type_box = ctk.CTkComboBox(master=app, values=['.mp3', '.mp4'], command=downloadTypeCallback, variable=download_type)
download_type_box.grid(row=2, column=0, sticky='ew', padx=20, pady=20)

#create download button
download_button = ctk.CTkButton(master=app, text="Download .mp3", command=downloadVideo, hover=True)
download_button.grid(row=2, column=1, sticky='ew', padx=20, pady=20)

#app custom things
app.title('Youtube Downloader')
app.resizable(False, False)
app.geometry('500x100')

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app.mainloop()
