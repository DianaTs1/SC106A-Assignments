# This program will count all words in text

def count_words(text):
    words_count = 0
    for line in text:
        line = line.split(" ")
        words_count += len(line)  # Add 'words_count' the number of words in each line
    return words_count


def main():
    with open("poem.txt") as poem:
        number_of_words = count_words(poem)
        print(f'"ვეფხისტყაოსანში" {number_of_words} სიტყვაა.')


if __name__ == '__main__':
    main()
