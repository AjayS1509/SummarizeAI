import yt_dlp
import os

# Ensure ffmpeg is available
ffmpeg_path = r"D:\ffmpeg\bin"
os.environ["PATH"] += os.pathsep + ffmpeg_path  # Add to PATH at runtime

def download_mp3(video_URL, destination, filename):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{destination}/{filename}.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ffmpeg_location': ffmpeg_path  # Explicitly provide ffmpeg location
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([video_URL])
            print("Download complete.")
        except Exception as e:
            print("Error in download:", str(e))

# Example usage
#download_mp3("https://www.youtube.com/watch?v=t45S_MwAcOw", "D:/Downloads", "speech1")
