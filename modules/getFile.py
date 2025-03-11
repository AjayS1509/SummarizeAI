import torch
import whisper
import pymongo
import gridfs
import tempfile
import os

def get_latest_audiofile():
    """
    Retrieves the latest uploaded audio file from MongoDB GridFS and transcribes it using Whisper.
    
    :return: Transcribed text from the audio file.
    """
    try:
        # Load MongoDB URI from environment variable
        MONGO_URI = os.getenv("MONGO_URI")
        if not MONGO_URI:
            raise ValueError("MONGO_URI is not set in environment variables.")

        # Connect to MongoDB
        client = pymongo.MongoClient(MONGO_URI)
        db = client["Audio_files"]  # Replace with your database name
        fs = gridfs.GridFS(db, collection="audio_files")

        # Get the latest uploaded file
        latest_file = db["audio_files.files"].find_one({}, sort=[("uploadDate", -1)])
        if not latest_file:
            raise FileNotFoundError("No audio files found in MongoDB.")

        audio_file_id = latest_file["_id"]  # Get ObjectId of the latest file
        print(f"Latest File ID: {audio_file_id}, Name: {latest_file['filename']}")

        # Retrieve file content
        audio_data = fs.get(audio_file_id).read()

        # Save to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
            temp_audio.write(audio_data)
            temp_audio_path = temp_audio.name  # Get the file path

        # Set device for Whisper
        device = "cuda" if torch.cuda.is_available() else "cpu"

        # Load Whisper model
        whisper_model = whisper.load_model("base", device=device)

        # Transcribe audio
        res = whisper_model.transcribe(temp_audio_path)
        text_data = res["text"]

        print("Transcribed Text:", text_data)
        return text_data

    except Exception as e:
        print(f"Error: {e}")
        return None

# Example Usage
# transcribed_text = get_latest_audiofile()
# print(transcribed_text)
