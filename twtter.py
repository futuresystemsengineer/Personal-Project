def main():
    tweet = input("Input: ")
    print(f"Output: {shorten(tweet)}")


def shorten(word):
    vocales = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    resultado = ""
    for letter in word:
        if letter not in vocales:
            resultado += letter
    return resultado


if __name__ == "__main__":
    main()