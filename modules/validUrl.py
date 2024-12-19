import requests
from urllib.parse import urlparse

def is_valid_youtube_url(url):
    try:
        # Parse the URL to ensure it's a valid YouTube URL
        parsed_url = urlparse(url)
        if parsed_url.hostname != "www.youtube.com" and parsed_url.hostname != "youtube.com":
            return False

        # Send a GET request to the YouTube URL
        response = requests.get(url)

        # Check if the response status is 200 (OK)
        if response.status_code == 200:
            #print("Valid YouTube URL.")
            return True
        else:
            #print(f"Invalid YouTube URL. Status code: {response.status_code}")
            return False
    except Exception as e:
        #print(f"Error: {e}")
        return False

# Test the function
#url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Replace with your URL
#is_valid_youtube_url(url)
