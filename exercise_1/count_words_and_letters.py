import string

"""
This program will count words and letters of each sentence
Only numbers and english alphabet letter should be counted
No single or double space should be considered as a word or a letter
"""


def count_words(sentence):
    sentence = sentence.strip()
    while '  ' in sentence:
        sentence = sentence.replace('  ', ' ')      # remove extra spaces around each word
    sentence_list = sentence.split(" ")
    return len(sentence_list)


def count_letters(sentence):
    list_of_letters = []
    for letter in sentence:
        if letter not in string.punctuation and letter != " ":
            list_of_letters.append(letter)
    return len(list_of_letters)


def main():
    sentence = input("Please type yor sentence here: ")
    print(f"There are {count_words(sentence)} words and {count_letters(sentence)} letters in your sentence!")


if __name__ == "__main__":
    main()
