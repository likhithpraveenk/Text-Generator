from nltk.util import ngrams
from collections import defaultdict
from random import choice, choices


def make_dictionary(arr: list) -> dict:
    heads = defaultdict(dict)
    for h1, h2, t in arr:
        h = (h1, h2)
        heads[h][t] = heads[h].get(t, 0) + 1
    return heads


def generate_pseudo_sentence(dic: dict) -> list:
    h1, h2 = get_first_word(dic)
    res = [h1, h2]
    i = 0
    while True:
        if i >= 20:
            return generate_pseudo_sentence(dic)
        word = get_tail(dic, h1, h2)
        if len(res) >= 5 and is_last_word(word):
            res.append(word)
            break
        elif is_last_word(word):
            i += 1
            continue
        else:
            res.append(word)
            h1, h2 = res[-2], res[-1]
    return res


def get_first_word(dic: dict) -> tuple[str, str]:
    arr = list(dic.keys())
    h1, h2 = choice(arr)
    while not h1[0].isupper() or is_last_word(h1):
        h1, h2 = choice(arr)
    arr.clear()
    return h1, h2


def get_tail(dic: dict, h1: str, h2: str) -> str:
    keys = list(dic[(h1, h2)].keys())
    weights = list(dic[(h1, h2)].values())
    [word] = choices(keys, weights)
    keys.clear()
    weights.clear()
    return word


def is_last_word(word: str) -> bool:
    return word[-1] in (".", "!", "?")


if __name__ == "__main__":
    filename = input()
    with open(filename, "r", encoding="utf-8") as f:
        trigrams = list(ngrams(f.read().split(), 3))
        dictionary = make_dictionary(trigrams)
        for _ in range(10):
            sentence = generate_pseudo_sentence(dictionary)
            print(" ".join(sentence))
