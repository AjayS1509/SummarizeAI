import nltk
from nltk.data import find
from flask import Flask
from handlers.routes import configure_routes

# Check if WordNet is already downloaded
try:
    find("corpora/wordnet.zip")
except LookupError:
    nltk.download('wordnet')

app = Flask(__name__)

# Configure your routes
configure_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
