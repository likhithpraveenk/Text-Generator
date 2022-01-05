from nltk.util import ngrams
from collections import defaultdict
from random import choice, choices


def make_dictionary(arr: list) -> dict:
    heads = defaultdict(dict)
    for h, t in arr:
        heads[h][t] = heads[h].get(t, 0) + 1
    return heads


def generate_pseudo_sentence(dic: dict) -> list:
    word = get_first_word(dic)
    res = [word]
    while True:
        keys = list(dic[word].keys())
        weights = list(dic[word].values())
        [word] = choices(keys, weights)
        if len(res) >= 5 and is_last_word(word):
            res.append(word)
            break
        elif len(res) < 5 and is_last_word(word):
            continue
        else:
            res.append(word)
    return res


def get_first_word(dic: dict) -> str:
    arr = list(dic.keys())
    word = choice(arr)
    while not word[0].isupper() or is_last_word(word):
        word = choice(arr)
    arr.clear()
    return word


def is_last_word(word: str) -> bool:
    return word[-1] in (".", "!", "?")


if __name__ == "__main__":
    filename = input()
    with open(filename, "r", encoding="utf-8") as f:
        bigrams = list(ngrams(f.read().split(), 2))
        dictionary = make_dictionary(bigrams)
        for _ in range(10):
            sentence = generate_pseudo_sentence(dictionary)
            print(" ".join(sentence))
