from pytube import YouTube
from pytube import Playlist
from time import sleep
from tkinter import filedialog
import os

def Download(link):
    try:
        video = YouTube(link)
        print(f'Downloading Video: {video.title}')
    except:
        print("Invalid URL. Try Again.")
        return -1
    
    video = video.streams.filter(only_audio=True).first() 
    try:
        video.download()
        print("Download is completed successfully")
    except:
        print("An error has occurred")

def DownloadPlaylist(link):
    try:
        p = Playlist(link)
        print(f'Downloading Playlist: {p.title}')
    except:
        print("Invalid Playlist Link\n")
    
    try:
        for video in p.videos:
            print(f'Downloading: {video.title}')
            Download(video.watch_url)
        print("Download is completed successfully")
    except:
        print("An error has occurred")

print("Welcome to the Downloader")
while True:
    

    usrChoice = input("1) Single MP3\n2) Playlist of MP3s\n0) Exit\n(1/2/0)> ")
    if usrChoice in ['1','2']:
        print("Please select the directory where you wish to download to...")
        sleep(1)
        dirPath = filedialog.askdirectory(initialdir=".")
        os.chdir(dirPath)

        if usrChoice == '1':
            link = input("Enter the YouTube video URL: ")
            Download(link)
        else:
            link = input("Enter the YouTube Playlist URL: ")
            DownloadPlaylist(link)
    else:
        break
print("Thank you for using the downloader!")
        

