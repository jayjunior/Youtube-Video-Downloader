from pytube import YouTube
import sys

def download_video(url) -> str:
    try:
        yt = YouTube(url)

        videos = yt.streams.filter()
        video = videos.get_by_resolution("720p")
        print(f"Dowloading {video.title}...")
        path = video.download(timeout=10)
        print("Downlaod completed")
        return path
    except:
        print("Something went Wrong !! check the url and the internet connection")
    
    return None


if(len(sys.argv) > 2):
    print("Script should be run just with one argument denoting the url of the file to download")
if(len(sys.argv) == 2):
    url = sys.argv[1]
    download_video(url)