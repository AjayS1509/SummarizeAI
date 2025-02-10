import nltk
from nltk.data import find
from flask import Flask
from flask_cors import CORS  # Import Flask-CORS
from handlers.routes import configure_routes
  # Suppress INFO and WARNING logs

#import tensorflow as tf

# Check if WordNet is already downloaded
try:
    find("corpora/wordnet.zip")
except LookupError:
    nltk.download('wordnet')

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)  # This allows all origins (http://localhost:3000 can access http://localhost:5000)

# Configure your routes
configure_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
