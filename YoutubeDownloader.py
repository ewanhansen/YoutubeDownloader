from cgitb import text
from curses import newwin
from doctest import master
from genericpath import exists
from inspect import _empty
from queue import Empty
from re import RegexFlag
from sqlite3 import Row
import string
from tkinter import *
import tkinter
from typing_extensions import Self
from wsgiref import validate
import customtkinter as ctk
import os
from tkinter import filedialog
from pytube import YouTube
import pytube
import fnmatch

#get app from tkinter
app = ctk.CTk()

target_folder = StringVar()
download_type = StringVar(value='.mp3')

def addTargetFolder():
    #filedialog for directory input and return it
    target_folder = filedialog.askdirectory(initialdir='/', title='Choose target folder...')
    return target_folder

def CreatePopup(title, error,):
    new_window = ctk.CTkToplevel(app)
    new_window.title(title)
    new_window.geometry('500x50')
    error_label = ctk.CTkLabel(master=new_window, text=error)
    error_label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    return new_window
    

def downloadVideo():
    #get link text from entry and 
    link_text = link_entry.get()

     #if no link input
    if link_text == '':
        CreatePopup('Uh-oh', 'No valid link (try double-checking the URL)!')
        print("No link input!")
        return False

    #target folder from addTargetFolder()
    target_folder = addTargetFolder()
    #if no target folder
    if target_folder == '':
        CreatePopup('Uh-oh', 'No target folder!')
        return False
    
    try:
        yt = YouTube(link_text)
    except pytube.exceptions.RegexMatchError as err:
        CreatePopup('Uh-oh', 'The provided link is not valid.')
        return False
           
    downloading_window = CreatePopup('Downloading', 'Downloading ' + yt.title)
    
    try:
        #make youtube object and set audio filtering if type is .mp3
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
            
        #clean up the downloading window
        downloading_window.destroy()
    except FileExistsError as err:
        downloading_window.destroy()
        CreatePopup('Uh-oh', 'File already exists!')     
    
    return True

def downloadTypeCallback(choice):
    download_button.configure(text='Download ' + choice)
    print(choice)

def checkExistingFile(video_title):
    for file in target_folder('.'):
        if fnmatch.fnmatch(file, [video_title]):
            print(file)        
         
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
download_type_box = ctk.CTkComboBox(master=app, values=['.mp3', '.mp4'], command=downloadTypeCallback, variable=download_type)
download_type_box.grid(row=1, column=0, sticky='ew', padx=10, pady=20)

#create download button
download_button = ctk.CTkButton(master=app, text="Download .mp3", command=downloadVideo, hover=True)
download_button.grid(row=1, column=1, sticky='ew', padx=10, pady=20)

#app custom things
app.title('Youtube Downloader')
app.resizable(False, False)
app.geometry('500x200')

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app.mainloop()
