import os
from pymongo import MongoClient
import gridfs

# MongoDB Atlas Connection URI (Replace <username>, <password>, <dbname> accordingly)
MONGO_URI = os.getenv("MONGO_URI")

# Local storage directory
LOCAL_AUDIO_DIR = "./audio_files"
os.makedirs(LOCAL_AUDIO_DIR, exist_ok=True)  # Ensure directory exists

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client.get_database("Audio_files")  # Replace with your database name
fs = gridfs.GridFS(db, collection="audio_files")  # Use "audio_files" collection


def upload_to_mongodb(file_path, filename):
    """
    Uploads an MP3 file to MongoDB GridFS, replacing the existing file if it exists.
    
    :param file_path: Path to the local MP3 file
    :param filename: Filename for storing in MongoDB
    """
    try:
        # Check if a file with the same name exists and delete it
        existing_file = db["audio_files.files"].find_one({"filename": f"{filename}.mp3"})
        if existing_file:
            fs.delete(existing_file["_id"])
            print(f"Old file '{filename}.mp3' deleted from MongoDB.")

        # Read file and upload to MongoDB GridFS
        with open(file_path, "rb") as f:
            file_id = fs.put(f, filename=f"{filename}.mp3")
            print(f"File uploaded to MongoDB successfully! File ID: {file_id}")

    except Exception as e:
        print(f"Upload error: {e}")


