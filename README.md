
# AI Notetaker for Inclusive Education

The AI Notetaker for Inclusive Education aims to transform video content, such as online lectures, webinars, or YouTube tutorials, into accessible and concise notes. This project is designed to support deaf and hearing-impaired individuals by converting audio-visual learning materials into text-based summaries and structured notes.


## Roadmap

- Front End UI Repo link - [https://github.com/AjayS1509/SummarizeAI_frontend](https://github.com/AjayS1509/SummarizeAI_frontendI/)

- Backend Server Repo link - [https://github.com/AjayS1509/SummarizeAI](https://github.com/AjayS1509/SummarizeAI/)


## Screenshots

![Summarize AI UI](https://github.com/user-attachments/assets/42519883-a3bc-4975-82b8-f412974558db)



## Documentation

To learn more about Next.js, take a look at the following resources:

- [python Documentation](https://www.python.org/) - learn about Python features and API.
- [Flask Documentation](https://flask.palletsprojects.com/en/stable/) - Backend for Flask
- [Models ollama Documentation](https://ollama.com/search/) - Models for Summarization



## Installation
```
Install my-project with python

```
- Create a virtual environment:
```
python -m venv venv
```
- Activate virtual environment:
```
source venv/Scripts/activate
```
- Install dependencies:
```
pip install -r requirements.txt
```
- Run app:
```
python app.py
```
    
## Structure 📂

```
Noteapp
├── .github/                     # GitHub-related files
├── audio_files/                 # Folder for storing audio files
├── handlers/                    # Request handlers
│   ├── __init__.py
│   ├── example.py
├── modules/                     # All functional modules
│   ├── __init__.py
│   ├── download.py
│   ├── modules.py
│   ├── old_codes.py             # Renamed for readability
│   ├── summarize.py
│   ├── valid_url.py             # Consistent naming convention
│   ├── whisper_summary.py       # Fixed typo
├── static/                      # Static files
│   ├── images/
│   ├── scripts/
│   ├── styles/
├── templates/                   # HTML templates
├── tests/                       # Unit tests
│   ├── __init__.py
├── .gitignore                   # Git ignore file
├── LICENSE                      # License file
├── README.md                    # Documentation
├── app.py                       # Main application entry point
├── requirements.txt             # Dependencies list
├── vercel.json                   # Vercel deployment config
└── venv/                        # Virtual environment (should be ignored in Git)
```

## Features

·  Speech-to-Text Conversion:
- Use YouTube's captions or APIs like Google Speech-to-Text or OpenAI Whisper to transcribe the video.
·  Summarization:
- Apply pre-trained LLMs (e.g., GPT models) to summarize the transcript into short, meaningful notes.
·  Highlight Key Points:
- Extract bullet points, important timestamps, or frequently mentioned topics.
·  Search and Organize:
- Add a feature to search for specific topics within the summarized notes.
- Organize summaries into categories or tags.
·  Multi-Language Support:
- Handle multilingual videos for broader applicability.
·  Visual Enhancements:
- Highlight critical phrases.
- Generate diagrams or flowcharts for visual learners (optional).
·  Export Options:
- Allow users to export notes in formats like PDF, Word, or Markdown.




## Tech Stack

**Client:** Nextjs, Typescript, TailwindCSS

**Server:** Python, Flask, ollama

**LLMs:** Deepseek-r1, Lamma3 


## Authors

- [@Ajay Soni](https://github.com/AjayS1509)
- [@Ashish Kumar](https://github.com/Ashishgithub2000)
- [@Harsh Kothari](https://github.com/HarshKothari22)
- [@Ekakshi Gajbhiye](https://github.com/Ekakshi-Gajbhiye)
- [@Snehal Sarode](https://github.com/snehalsarode25)


## Support

For support, email ajaypsoni1509@gmail.com

