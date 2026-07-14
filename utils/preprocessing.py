import nltk
import string

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
# Download required NLTK resources (only needed the first time)
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")
nltk.download("wordnet")

# Create objects
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))
def clean_text(text):
    # Convert text to lowercase
    text = text.lower()

    # Split text into words
    words = word_tokenize(text)

    cleaned_words = []

    # Process each word
    for word in words:

        # Remove punctuation
        if word in string.punctuation:
            continue

        # Remove stop words
        if word in stop_words:
            continue

        # Lemmatize the word
        word = lemmatizer.lemmatize(word)

        cleaned_words.append(word)

    return " ".join(cleaned_words)