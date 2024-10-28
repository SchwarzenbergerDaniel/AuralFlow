# importing packages 
from pytubefix import YouTube 
import os 
  
def downloadFromURL(url):
    yt = YouTube(str(url)) 
    
    video = yt.streams.filter(only_audio=True).first() 
    
    destination = os.path.dirname(__file__)+"\\downloads"
    
    # download 
    print("Download")
    out_file = video.download(output_path=destination) 
    
    # save 
    base, ext = os.path.splitext(out_file) 
    new_file = base + '.mp3'
    os.rename(out_file, new_file) 
    
    print(yt.title, "has been downloaded.")
