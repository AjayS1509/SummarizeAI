#import yt_dlp
#from flask import send_file
#import os
from flask import jsonify
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

def hello():
    return "Hello, World!"

def content():
    return '''
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
            Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
            Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
            Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
            '''
# def yt_audio_extractor(youtube_url):
#     print("1+")
#     AUDIO_FOLDER = os.path.join(os.getcwd(), 'audio_files')
#     if not os.path.exists(AUDIO_FOLDER):
#         os.makedirs(AUDIO_FOLDER)
#     ydl_opts = {
#             'format': 'bestaudio/best',  # Best audio quality
#             'postprocessors': [{
#                 'key': 'FFmpegAudioConvertor',
#                 'preferredcodec': 'mp3',
#                 'preferredquality': '192',
#             }],
#             'outtmpl': os.path.join(AUDIO_FOLDER, '%(id)s.%(ext)s'),  # Specify the folder to save audio
#         }
#     print("2+")
#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         info_dict = ydl.extract_info(youtube_url, download=True)
#         audio_file = f"{info_dict['id']}.mp3"  # The downloaded audio file in MP3 format

#     # Path to the audio file
#     audio_path = os.path.join(AUDIO_FOLDER, audio_file)

#     # Send the audio file to the client
#     return send_file(audio_path, as_attachment=True, download_name=audio_file)


def yt_transcript_api(url):

    try:
        video_id = url.split("v=")[-1]  # Extract video ID from the URL
        # Fetch the transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        # Format the transcript as text
        formatter = TextFormatter()
        formatted_text = formatter.format_transcript(transcript)

        # Print or save the transcript
        #print(formatted_text)
        # Optionally, you can save it to a file
        # with open("transcript.txt", "w") as f:
        #     f.write(formatted_text)
        return formatted_text

    except Exception as e:
        return None
        #print(f"Error: {e}")