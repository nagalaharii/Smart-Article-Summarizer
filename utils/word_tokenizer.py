import nltk
from nltk.tokenize import word_tokenize

# Download tokenizer resources (only first time)
nltk.download("punkt")
nltk.download("punkt_tab")

text = "Artificial Intelligence is transforming healthcare."

words = word_tokenize(text)

print("Words:\n")

for i, word in enumerate(words, start=1):
    print(f"Word {i}: {word}")