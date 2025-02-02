#import yt_dlp
#from flask import send_file
#import os
from flask import jsonify
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
from urllib.parse import urlparse, parse_qs
from modules.summarize import abstractive_summarization

def hello():
    return "Hello, World!"

def content():
    return '''
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
            Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
            Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
            Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
            '''

def yt_transcript_api(url):
    try:
        # Extract Video ID
        video_id = extract_video_id(url)
        if not video_id:
            return {"error": "Invalid YouTube URL, could not extract video ID"}

        print(f"Extracted Video ID: {video_id}")  # Debugging Log

        # Fetch Transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        # Convert to Readable Text
        formatted_text = "\n".join([entry["text"] for entry in transcript])

        print("Transcript fetched successfully!")  # Debugging Log

        summary = abstractive_summarization(formatted_text)

        return {"transcript": summary}

    except Exception as e:
        print("Transcript API Error:", str(e))  # Log error on Vercel
        return {"error": str(e)}

def extract_video_id(url):
    """Extracts the YouTube video ID from various URL formats."""
    parsed_url = urlparse(url)
    if "youtube.com" in parsed_url.netloc:
        return parse_qs(parsed_url.query).get("v", [None])[0]
    elif "youtu.be" in parsed_url.netloc:
        return parsed_url.path.lstrip("/")
    return None
