# Returns the most popular letter and the quantity

def get_popular_letter(text):
    letters_dict = {}
    for line in text:
        line = line.strip().replace(" ", "")           # Turns each line into one long string
        for letter in line:
            if letter in letters_dict:
                letters_dict[letter] += 1
            else:
                letters_dict[letter] = 1

    times_appeared = min(letters_dict.values())        # This is the value of the key we are looking for
    key_list = list(letters_dict.keys())               # To find a key firs I created a list of all 33 letters
    val_list = list(letters_dict.values())             # Then the list of all the values for those letters
    position = val_list.index(times_appeared)          # This is the index where the value we're looking for is located
    popular_letter = key_list[position]                # Reaching that letter
    return popular_letter, times_appeared


def main():
    with open("poem.txt") as poem:
        popular_letter = get_popular_letter(poem)
        print(f'"ვეფხისტყაოსანში" ყველაზე იშვიათად ({popular_letter[1]}-ჯერ) გამოყენებული ასოა "{popular_letter[0]}".')


if __name__ == '__main__':
    main()
