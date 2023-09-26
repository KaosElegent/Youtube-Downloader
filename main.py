from pytube import YouTube

def Download(link):
    try:
        video = YouTube(link)
    except:
        print("Invalid URL. Try Again.")
        return -1
    
    video = video.streams.get_highest_resolution()
    try:
        video.download()
        print("Download is completed successfully")
    except:
        print("An error has occurred")


link = input("Enter the YouTube video URL: ")
Download(link)