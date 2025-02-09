from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from transformers import pipeline  # Add this import
import ollama

def summarize_text(text, sentences_count=5):
    # Ensure text isn't too long for Sumy to handle by chunking it
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences_count)
    return " ".join(str(sentence) for sentence in summary)


# def summarize_to_html(summarized_text):
#     lines = summarized_text.split('\n')  # Split text into lines
#     html_lines = []

#     for line in lines:
#         if line.strip() == "":
#             continue  # Skip empty lines
#         # Check if the line is a heading (e.g., starts with a number or **)
#         if line.strip().startswith("**") or line.strip()[0].isdigit():
#             html_lines.append(f"<strong>{line.strip()}</strong><br>")
#         else:
#             html_lines.append(f"{line.strip()}<br>")
#     return "".join(html_lines)  # Combine lines into a single HTML string

def summarize_to_html(summarized_text):
    lines = summarized_text.split('\n')  # Split text into lines
    html_lines = []

    for line in lines:
        if line.strip() == "":
            continue  # Skip empty lines
        # Remove ### if present
        line = line.replace("###", "").strip()
        # Remove " and ' if present
        line = line.replace('"', '').replace("'", "")
        # Check if the line contains ** (bold text)
        if "**" in line:
            # Remove ** and wrap the content in <strong> tags
            line = line.replace("**", "")
            html_lines.append(f"<strong>{line.strip()}</strong><br>")
        else:
            html_lines.append(f"{line.strip()}<br>")

    return "".join(html_lines)  # Combine lines into a single HTML string


def abstractive_summarization(text):
    # Ensure the text is not too long for the model
    #summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    #summary = summarizer(text, max_length=100, min_length=30, do_sample=False)


    #response = ollama.chat(model="llama3", messages=[{"role": "user", "content": f"Summarize the following text: {text}"}])
    response = ollama.chat(model="deepseek-r1:1.5b", messages=[{"role": "user", "content": f"Summarize the following text with sub heading and points : {text}"}])


    #print(response)

    full_response = response["message"]["content"]

    apply_html = full_response.split("</think>")[-1].strip()

    summary = summarize_to_html(apply_html)
    #print(summary)
    #return summary[0]['summary_text']
    return summary
