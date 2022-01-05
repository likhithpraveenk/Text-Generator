from nltk.util import ngrams
from collections import defaultdict


def make_dictionary(arr):
    heads = defaultdict(dict)
    for h, t in arr:
        heads[h][t] = heads[h].get(t, 0) + 1

    return heads


if __name__ == "__main__":
    filename = input()
    with open(filename, "r", encoding="utf-8") as f:
        bigrams = list(ngrams(f.read().split(), 2))
        dictionary = make_dictionary(bigrams)
        while True:
            head = input()
            if head == "exit":
                break
            try:
                tails = dictionary[head]
                print(f"Head: {head}")
                for tail, val in tails.items():
                    print(f"Tail: {tail}\tCount: {val}")
            except KeyError:
                print("Key Error. The requested word is not in the model. Please input another word.")
            except (TypeError, ValueError):
                print("Type Error. Please input an integer.")
            except IndexError:
                print("Index Error. Please input a value that is not greater than the number of all bigrams.")
