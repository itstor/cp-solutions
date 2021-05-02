def reverse_words(text):
    return " ".join(str(i) for i in [t[::-1] for t in text.split(" ")])
