def get_popular_word(text):
    all_words = {}
    times_appear = 0
    popular_word = ''

    for line in text:
        line = line.strip().split(' ')   # deletes extra double-spaces, returns an individual array
        for word in line:
            if word in all_words:
                all_words[word] += 1
            else:
                all_words[word] = 1

            if all_words[word] > times_appear:
                times_appear = all_words[word]
                popular_word = word
    return popular_word


def main():
        with open('poem.txt', encoding='utf-8') as poem:
            print(f"'ვეფხისტრაოსანში' ყველაზე ხშირად გამოყენებული სიტყვაა: '{get_popular_word(poem)}'.")


if __name__ == '__main__':
    main()
