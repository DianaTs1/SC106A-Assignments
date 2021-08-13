# This program searches for the line which has most letters

def fins_longest_line(text):
    longest_line = ''
    longest_line_length = 0
    for line in text:
        line_stripped = line.strip().replace(" ", "")
        if len(line_stripped) > longest_line_length:
            longest_line_length = len(line_stripped)
            longest_line = line.strip()
    return longest_line, longest_line_length


def main():
    with open("poem.txt") as poem:
        longest_line = fins_longest_line(poem)
        print(f'"ვეფხისტყაოსანში" ყველაზე მეტი ({longest_line[1]}) ასოა ტაეპში: \n"{longest_line[0]}."')


if __name__ == '__main__':
    main()

