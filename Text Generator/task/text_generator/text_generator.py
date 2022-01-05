from nltk.util import ngrams


if __name__ == "__main__":
    filename = input()
    with open(filename, "r", encoding="utf-8") as f:
        tokens = f.read().split()
        bigrams = list(ngrams(tokens, 2))
        print(f"Number of bigrams: {len(bigrams)}")
        while True:
            ind = input()
            if ind == "exit":
                break
            try:
                ind = int(ind)
                print(f"Head: {bigrams[ind][0]} Tail: {bigrams[ind][1]}")
            except (TypeError, ValueError):
                print("Type Error. Please input an integer.")
            except IndexError:
                print("Index Error. Please input a value that is not greater than the number of all bigrams.")
