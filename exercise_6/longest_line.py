# This program searches for the line which has most words

def get_longest_line(text):
    words_in_longest_line = 0
    longest_line = ''
    for line in text:
        line = line.strip().split(" ")
        if len(line) > words_in_longest_line:
            words_in_longest_line = len(line)
            longest_line = " ".join(line)
    return longest_line


def main():
    with open("poem.txt") as poem:
        print(f'"ვეფხისტყაოსანში" ყველაზე მრავალსიტყვიანი ტაეპია:\n"{get_longest_line(poem)}"')


if __name__ == '__main__':
    main()