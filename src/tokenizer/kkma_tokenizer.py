from konlpy.tag import Kkma


def kkma_tokenizer(text):
    kkma = Kkma()
    use_tags = ["N", "O"]
    word_tag = kkma.pos(text)
    words = [
        word
        for word, tag in word_tag
        if (len(word) > 1) and any(tag.startswith(tag_) for tag_ in use_tags)
    ]
    return words
