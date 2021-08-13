def get_two_letters_words(text):
    words = []

    for line in text:
        line = line.strip(). split(" ")
        for word in line:
            if len(word) == 2:
                words.append(word)

    return len(words)


def main():
    with open("poem.txt") as poem:
        print(f'"ვეფხისტყაოსანში ორასოიანი სიტყვები {get_two_letters_words(poem)}-ჯერ არის ნახსენები.')


if __name__ == '__main__':
    main()