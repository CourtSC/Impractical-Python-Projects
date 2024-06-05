# Python3 - Converts a string to pig latin.

"""
To form Pig Latin, you take an English word that begins with a consonant, move that
consonant to the end, and then add 'ay' to the end of the word. If the word begins with
a vowel, you simply add 'way' to the end of the word.
"""


def main():
    userInput = input("\nEnter a string to convert to pig latin.\n\n")
    wordList = userInput.split(" ")
    newString = ""
    for word in wordList:
        specialChar = False

        if newString != "":
            newString += " "

        if not word[-1].isalpha():
            specialChar = word[-1]
            word = word[:-1]

        if not word[0].isalpha():
            newString += word
        elif word[0].lower() in ["a", "e", "i", "o", "u"]:
            newString += f"{word}way"
        else:
            newString += f"{word[1:]}{word[0]}ay"

        if specialChar:
            newString += specialChar

        newString = newString.lower().capitalize()

    print(f"\n\n{newString}")


if __name__ == "__main__":
    main()
