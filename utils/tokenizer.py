import nltk
from nltk.tokenize import sent_tokenize

# Download tokenizer data (only needed the first time)
nltk.download('punkt_tab')

text = """
Artificial Intelligence is transforming healthcare by enabling early disease detection, personalized treatments, and faster medical research.

Natural Language Processing helps computers understand human language.

Text summarization is one of the most useful applications of NLP.
"""

sentences = sent_tokenize(text)

print("Sentences:\n")

for i, sentence in enumerate(sentences, start=1):
    print(f"Sentence {i}: {sentence}")