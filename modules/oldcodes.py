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


# def yt_transcript_api(url):

#     try:
#         video_id = url.split("v=")[-1]  # Extract video ID from the URL
#         # Fetch the transcript
#         transcript = YouTubeTranscriptApi.get_transcript(video_id)

#         # Format the transcript as text
#         formatter = TextFormatter()
#         formatted_text = formatter.format_transcript(transcript)

#         #print("!",formatted_text)

#         # Print or save the transcript
#         #print(formatted_text)
#         # Optionally, you can save it to a file
#         # with open("transcript.txt", "w") as f:
#         #     f.write(formatted_text)
#         return formatted_text
#         #return " test1"

#     except Exception as e:
#         return "Error on converting text"
#         #print(f"Error: {e}")