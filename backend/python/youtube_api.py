from pytubefix import YouTube 
import os 
import requests


spring_boot = "localhost:8080"

def uploadFromURL(url):
    try:
        yt = YouTube(str(url))
        
        # Retrieve desired metadata
        video_info = {
            'title': yt.title,
            'author': yt.author,
            'length': yt.length,
            'views': yt.views,
            'publish_date': yt.publish_date.isoformat() if yt.publish_date else None
        }
        
        # Download audio stream
        video = yt.streams.filter(only_audio=True).first()
        destination = os.path.join(os.path.dirname(__file__), "downloads")
        out_file = video.download(output_path=destination)
        
        # Convert to mp3 format
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        
        # Upload audio file with metadata
        ''' 
        
        with open(new_file, "rb") as audio_file:
            requests.post(
                spring_boot+"/upload_song",
                files={'audio': audio_file},
                data=video_info  # Send all metadata fields
            )
        '''
        
        print(f"{video_info['title']} has been downloaded and uploaded. File path: {new_file}")
        os.remove(new_file)
        return True
    except:
        return False


def to8D(path):
    try :
        # TODO VIDEO TO 8D
        print("")
    except: 
        return None