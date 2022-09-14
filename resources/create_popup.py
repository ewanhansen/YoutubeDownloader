import customtkinter as ctk
import tkinter

class Popup:
    def Create(self, title, content, app):
        #create new window with title, content, from app
        new_window = ctk.CTkToplevel(app)
        new_window.title(title)
        new_window.geometry('500x50')
        error_label = ctk.CTkLabel(master=new_window, text=content)
        error_label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        return new_window