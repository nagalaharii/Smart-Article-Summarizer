from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer

from utils.preprocessing import clean_text
def generate_summary(text):

    sentences = sent_tokenize(text)

    cleaned_sentences = []

    for sentence in sentences:
        cleaned = clean_text(sentence)
        cleaned_sentences.append(cleaned)

    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(cleaned_sentences)

    tfidf_array = tfidf_matrix.toarray()

    sentence_scores = {}

    for i in range(len(sentences)):
        score = sum(tfidf_array[i])
        sentence_scores[i] = score

    ranked_sentences = sorted(
        sentence_scores,
        key=sentence_scores.get,
        reverse=True
    )

    top_n = 2

    top_sentence_indices = ranked_sentences[:top_n]

    top_sentence_indices.sort()

    summary = ""

    for index in top_sentence_indices:
        summary += sentences[index] + " "

    return summary.strip()