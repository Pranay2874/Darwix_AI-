import nltk
import os

# Ensure punkt is downloaded locally
nltk_data_dir = os.path.join(os.getcwd(), "nltk_data")
os.makedirs(nltk_data_dir, exist_ok=True)
nltk.data.path.append(nltk_data_dir)

# NLTK occasionally has issues downloading without error handling
try:
    nltk.download('punkt', download_dir=nltk_data_dir, quiet=True)
    nltk.download('punkt_tab', download_dir=nltk_data_dir, quiet=True)
except Exception:
    pass

from nltk.tokenize import sent_tokenize

def split_into_segments(text, num_segments=3):
    sentences = sent_tokenize(text)
    if len(sentences) < num_segments:
        # If too few sentences, return each as its own segment
        return sentences

    # Distribute sentences into num_segments groups
    seg_len = len(sentences) // num_segments
    remainder = len(sentences) % num_segments
    segments = []
    start = 0
    for i in range(num_segments):
        end = start + seg_len + (1 if i < remainder else 0)
        segment = " ".join(sentences[start:end])
        segments.append(segment)
        start = end
    return segments
