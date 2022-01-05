# from nltk import word_tokenize
from collections import Counter


if __name__ == "__main__":
    filename = input()
    with open(filename, "r", encoding="utf-8") as f:
        # tokens = word_tokenize(f.read())
        tokens = f.read().split()
        print("Corpus statistics")
        print(f"All tokens: {len(tokens)}")
        print(f"Unique tokens: {len(Counter(tokens))}")
        while True:
            ind = input()
            if ind == "exit":
                break
            try:
                ind = int(ind)
                print(tokens[ind])
            except (TypeError, ValueError):
                print("Type Error. Please input an integer.")
            except IndexError:
                print("Index Error. Please input an integer that is in the range of the corpus.")
