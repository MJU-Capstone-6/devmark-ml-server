from sklearn.feature_extraction.text import CountVectorizer
import joblib
from konlpy.tag import Kkma


def kkma_tokenizer(text):
    kkma = Kkma()
    use_tags = ["N", "O"]  # 여러 태그를 확인할 수 있도록 리스트를 사용합니다.
    word_tag = kkma.pos(text)
    words = [
        word
        for word, tag in word_tag
        if (len(word) > 1) and any(tag.startswith(tag_) for tag_ in use_tags)
    ]
    return words


vectorizer = CountVectorizer(tokenizer=kkma_tokenizer)
word_model = joblib.load("model/KCNB.pkl")
sentence = "Python으로 코딩 공부하기"
sentence_count = vectorizer.transform([sentence])
print(word_model.predict(sentence_count))
