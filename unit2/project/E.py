import sys


if __name__ == "__main__":
    phrase = input("Type your phrase: ")
    revphrase =' '.join(reversed(phrase.split()))
    print("The reversed phrase is: ",revphrase) 