from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from transformers import pipeline  # Add this import

def summarize_text(text, sentences_count=5):
    # Ensure text isn't too long for Sumy to handle by chunking it
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences_count)
    return " ".join(str(sentence) for sentence in summary)


def abstractive_summarization(text):
    # Ensure the text is not too long for the model
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
    print(summary)
    return summary[0]['summary_text']
