from nltk.corpus import wordnet as wn

def count_underscore(word):
    i = 0
    for l in word:
        if l == '_':
            i += 1
    return i


def get_n_length_words( n):
    words = list(wn.words())
    nLength = set()
    for word in words:
        i = count_underscore(word)
        if len(word) - i == n:
            word = word.replace('_', '')
            nLength.add(word.upper())
    return sorted(nLength)

print(get_n_length_words(4))