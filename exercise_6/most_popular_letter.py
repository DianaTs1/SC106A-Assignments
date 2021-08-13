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

    times_appeared = max(letters_dict.values())        # This is the value of the key we are looking for
    key_list = list(letters_dict.keys())               # To find a key firs I created a list of all 33 letters
    val_list = list(letters_dict.values())             # Then the list of all the values for those letters
    position = val_list.index(times_appeared)          # This is the index where the value we're looking for is located
    popular_letter = key_list[position]                # Reaching that letter
    return popular_letter, times_appeared


def main():
    with open("poem.txt") as poem:
        popular_letter = get_popular_letter(poem)
        print(f'"ვეფხისტყაოსანში" ყველაზე ხშირად ({popular_letter[1]}-ჯერ) გამოყენებული ასოა "{popular_letter[0]}".')


if __name__ == '__main__':
    main()












# def get_text():
#     poem_list = []
#     with open("poem.txt") as poem:
#         for line in poem:
#             line = line.replace("  ", " ").strip().split(' ')
#             poem_list.append(line)
#     return poem_list
#
#
# # Create a dictionary where Key will be a letter the value will be times appeared
# def get_letters(text):
#     all_letters = {}
#     for line in text:
#         for word in line:
#             for letter in word:
#                 if letter in all_letters:
#                     all_letters[letter] +=1
#                 else:
#                     all_letters[letter] = 1
#     return all_letters
#
#
# # Returns the most popular letter and the quantity
# def get_most_popular_letter(dic):
#     popular_letter = ''
#     number_appeared = 0   # how many times the most popular word appears
#     for keys in dic:
#         if dic[keys] > number_appeared:
#             number_appeared = dic[keys]
#             popular_letter = keys
#     return number_appeared, popular_letter
#
#
# def main():
#     poem = get_text()
#     letters_dictionary = get_letters(poem)
#     popular_letter = get_most_popular_letter(letters_dictionary)
#     print(f'"ვეფხისტყაოსანში" ყველაზე ხშირად ({popular_letter[0]}-ჯერ) გამოყენებული ასოა: "{popular_letter[1]}".')
#
#
# if __name__ == '__main__':
#     main()