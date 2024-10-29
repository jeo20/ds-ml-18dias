from sklearn.feature_extraction.text import TfidfVectorizer

corpus = ['This is the first document.',
     'This document is the second document.',
     'And this is the third one.',
     'Is this the second document?',
     'Anyone have the first document?']

vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(corpus)
print(vectorizer.get_stop_words())
print(vectorizer.get_feature_names())
# summarize
print(vectorizer.vocabulary_)
print(vectorizer.idf_)
# summarize encoded vector
print(X.shape)
print(X.toarray())
print(X)

