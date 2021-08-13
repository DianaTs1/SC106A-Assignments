# This code counts every line including titles
def count_lines(text):
    number_of_lines = 0
    for line in text:
        number_of_lines += 1
    return number_of_lines

#
def count_lines_accurately(text):
    number_of_lines = 0
    for line in text:
        # გამოვრიცხოთ 1, 2 და 3 სიტყვიანი სათაურები
        if len(line.split(" ")) >= 4:  # shortest_line.py-დან ვიცი, რომ ყველაზე მოკლე ტაეპი 4 სიტყვიანია
            number_of_lines += 1
    return number_of_lines


def main():
    with open('poem.txt', encoding='utf-8') as poem:
        # print(f'"ვეფხისტყაოსანი" შედგება {count_lines(poem)} ხაზისგან.')
        print(f'"ვეფხისტყაოსანი" შედგება {count_lines_accurately(poem)} ხაზისგან')


if __name__ == '__main__':
    main()

