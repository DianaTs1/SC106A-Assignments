def get_letters_count(text):
    all_letters = ""                           # This will be the string containing ALL letters with no white space
    for line in text:
        line = line.strip().replace(" ", "")   # Separate lines, get rid of white space
        all_letters += line                    # Concatenate strings
    return len(all_letters)


def main():
    with open("poem.txt", encoding='utf-8' ) as poem:
        print(f'"ვეფხისტყაოსანში" {get_letters_count(poem)} ასოა.')


if __name__ == '__main__':
    main()