from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "Artificial Intelligence is transforming healthcare.",
    "Natural Language Processing helps computers understand human language.",
    "Text summarization is one of the most useful applications of NLP."
]

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(documents)

feature_names = vectorizer.get_feature_names_out()

print("Vocabulary:\n")
print(feature_names)

print("\nTF-IDF Matrix:\n")
print(tfidf_matrix.toarray())