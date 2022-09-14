from time import sleep
from resources.create_popup import Popup
from resources.add_target_folder import TargetFolder
from pytube import YouTube
import pytube
import os

p = Popup()
t = TargetFolder()

class DownloadVideo():
    def download(self, link, type, app):
        #get target folder from TargetFolder()
        target_folder = t.GetTargetFolder()

         #safety check for no link input
        if link == '':
            p.Create('Uh-oh', 'No valid link (try double-checking the URL)!', app)
            print("No link input!")
            return
               
        #safety check for no target folder
        if target_folder == '':
            p.Create('Uh-oh', 'No target folder!', app)
            return
    
        #link validation, try to created but if RegexMatch error, create Popup()
        try:
            yt = YouTube(link)
        except pytube.exceptions.RegexMatchError as err:
            p.Create('Uh-oh', 'The provided link is not valid.', app)
            return
           
        #create download window(doesn't always render before download slows program down)
        downloading_window = p.Create('Downloading', 'Downloading ' + yt.title, app)
    
        #downloading logic
        try:
            #make youtube object and set audio filtering if type is .mp3
            if type == '.mp3':
                audio = yt.streams.filter(only_audio=True).first()
                saved_file = audio.download(target_folder)
                base, ext = os.path.splitext(saved_file)
                new_file = base + '.mp3'
                os.rename(saved_file, new_file)
                downloading_window.destroy()
            else:
                #extension stuff is being done to try throw FileExistsError (avoid possible unlinking issues in premiere or other programs) NOT WORKING FOR SOME REASON
                video = yt.streams.get_highest_resolution()
                saved_file = video.download(target_folder)
                base, ext = os.path.splitext(saved_file)
                new_file = base + '.mp4'
                os.rename(saved_file, new_file)
                downloading_window.destroy()
        #handle file exists error and throw popup
        except FileExistsError as err:
            downloading_window.destroy()
            p.Create('Uh-oh', 'File already exists!', app)   
    
        return