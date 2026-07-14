import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download resources (only the first time)
nltk.download("stopwords")
nltk.download("punkt")
nltk.download("punkt_tab")

text = "Artificial Intelligence is transforming the world."

words = word_tokenize(text)

stop_words = set(stopwords.words("english"))

filtered_words = []

for word in words:
    if word.lower() not in stop_words:
        filtered_words.append(word)

print("Original Words:")
print(words)

print("\nAfter Removing Stop Words:")
print(filtered_words)