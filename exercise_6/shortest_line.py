# This program searches for the line which has least words in it

def get_longest_line(text):
    words_in_longest_line = 12                     # ვიცი, რომ ყველაზე გრძელი ხაზი 12 სიტყვვისგან შედგება
    shortest_line = ''
    for line in text:
        line = line.strip().split(" ")
        if len(line) < words_in_longest_line > 4:  # ეს იმიტომ ჩავუსვი, რომ აშკარად სათაურებს მიბრუნებდა ამის გარეშე
            words_in_longest_line = len(line)      # 4 იქედან მივიღე, რომ მანამდე ყველა სათაური იყო 2, 3-ზე, სხვანაირად
            shortest_line = " ".join(line)         # როგორ მივიდე 4-მდე, არ ვიცი, ვერ მოვიფიქრე
    return shortest_line


def main():
    with open("poem.txt") as poem:
        print(f"'ვეფხისტყაოსანში' ყველაზე მოკლე ტაეპია: '{get_longest_line(poem)}'")


if __name__ == '__main__':
    main()
