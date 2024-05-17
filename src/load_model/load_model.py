from sklearn.feature_extraction.text import CountVectorizer
import joblib

word_model = joblib.load("")
vectorizer = CountVectorizer()
sentence = ""
sentence_count = vectorizer.transform([sentence])
print(word_model.predict(sentence_count))
