


from rake_nltk import Rake
def main2():
    # Uses stopwords for english from NLTK, and all puntuation characters by
    # default
    r = Rake()



    sample_file = open("caption.txt", 'r', encoding="iso-8859-1")
    text = sample_file.read()
    r.extract_keywords_from_text(text)
    keywords=r.get_ranked_phrases()

    j= open("hashesfromcaption.txt", "w+")
    for i in keywords:
        j.write("#"+i)

    print("Keywords:", keywords)

