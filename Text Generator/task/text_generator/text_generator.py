from nltk.util import ngrams
from collections import defaultdict
from random import choice, choices


def make_dictionary(arr: list) -> dict:
    heads = defaultdict(dict)
    for h, t in arr:
        heads[h][t] = heads[h].get(t, 0) + 1
    return heads


def generate_sentence(dic: dict, word: str) -> list:
    res = [word]
    for _ in range(9):
        keys = list(dic[word].keys())
        weights = list(dic[word].values())
        res += choices(keys, weights)
        word = res[-1]
    return res


if __name__ == "__main__":
    filename = input()
    with open(filename, "r", encoding="utf-8") as f:
        bigrams = list(ngrams(f.read().split(), 2))
        dictionary = make_dictionary(bigrams)
        first_word = choice(list(dictionary.keys()))
        for _ in range(10):
            sentence = generate_sentence(dictionary, first_word)
            print(" ".join(sentence))
            first_word = sentence[-1]
