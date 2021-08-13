def get_single_words(text):
    single_words = []
    all_words = {}

    for line in text:
        line = line.strip(). split(" ")
        for word in line:
            if word in all_words:
                all_words[word] += 1
            else:
                all_words[word] = 1

    for key in all_words:
        if all_words[key] == 1:
            single_words.append(key)

    return len(single_words)


def main():
    with open("poem.txt") as poem:
        length = get_single_words(poem)
        print(f'"ვეფხისტყაოსანში {length} ისეთი სიტყვაა, რომელიც მხოლოდ ერთხელ არის ნახსენები.')


if __name__ == '__main__':
    main()




# def create_words_list():
#     with open("poem.txt") as poem:
#         list_of_lines = []
#         for line in poem:
#             line_words = line.replace("  ", " ").strip().split(' ')
#             for words in line_words:
#                 list_of_lines.append(words)
#         return list_of_lines
#
#
# # returns a dictionary of words where
# # value represents the number of times the word appears
# def count_individual_words(array):
#     all_words = {}
#     for elem in array:
#         if elem in all_words:
#             all_words[elem] += 1
#         else:
#             all_words[elem] = 1
#     return all_words
#
#
# # Returns both the number of single words and a list of those words
# def get_single_words(text):
#     single_words = []
#     individual_words = count_individual_words(text)
#     for key in individual_words:
#         if individual_words[key] == 1:
#             single_words.append(key)
#     return len(single_words), ", ".join(single_words)
#
#
# def main():
#     text = create_words_list()
#     print(f'\n"ვეფხისტყაოსანში" {get_single_words(text)[0]} ცალი ერთხელ ნახსენები სიტყვაა.')
#     question = input("\nგინდა იხილო ეს სიტყვები? ").strip()
#     if question == "კი":
#         print(f"These single words are: {get_single_words(text)[1]}")
#     if question == "არა" or question == "კი":
#         print('\nმადლობა!')
#
#
# if __name__ == '__main__':
#     main()
