import random


def primary():
    print("This is a github tutorial.")

    f = open("quotes.txt", encoding="utf8")
    quotes = f.readlines()
    f.close()

    last = 13
    rnd = random.randint(0, last)
    print(quotes[rnd], end="")

    rnd = random.randint(0, last)
    print(quotes[rnd])

    f = open("quotes.txt", "a", encoding="utf8")
    f.write("Adding more lines to an existing text file." + "\n")
    f.close()


if __name__ == "__main__":
    primary()
