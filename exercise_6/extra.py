# ეს არის კოდი, რომელიც ქმნის აბსურდს
import random


def get_all_words():
    words = []                                # ეს არის ლისტი ყველა ისეთი სიტყვის
    with open("poem.txt") as poem:            # რომლის ასოების სიმრავლეც 6-ზე ნაკლებია
        for line in poem:                     # გრძელ სიტყვებთან თამაში რთული აღმოჩნდა
            line = line.strip().split(" ")
            for word in line:
                if len(word) < 6:
                    words.append(word)
    return words


def game(words):
    while True:
        # რენდომად ავარჩიოთ სიტყვა, რომელსაც მომხმარებელი გამოიცნობს
        random_word_index = random.randint(0, len(words))
        word_as_list = []
        random_word_normal = words[random_word_index]

        # რენდომად არჩეული სიტყვა გადავაქციოთ ლისტად და ლისტში შემავალი ელემენტები რენდომად დავაგენერიროთ
        for x in random_word_normal:
            word_as_list.insert(random.randint(0, len(word_as_list)), x)
        random_word_funky = "".join(word_as_list)

        print(f'გამოიცანიი სიტყვა, რომელიც შედგება შემდეგი ასოებისგან: {random_word_funky}')
        answer = input("შეიყვანეთ სწორი ვერსია ან აკრიფე Q თამაშის შესაწყეტად: ")

        if answer.strip().upper() == "Q":
            print("მადლობა თამაშისთვის და გახსოვდეს:"
                  "\n'თუ თავი შენი შენ გახლავს, ღარიბად არ იხსენები!'")
            break
        if random_word_normal == answer.strip():
            print(f"ყოჩაღ, '{answer}' სწორი პასუხია!")
        else:
            print(f"'{answer}' არასწორი პასუხია, სწორი პასუხია '{random_word_normal}'!")


def main():
    words_to_play = get_all_words()
    print('ეკრანზე გამოისახება "ვეფხისტყაოსნიდან" სიტყვები, სადაც ასოები შემთხვევითად არის განაწილებული.'
          '\nშენი მისიაა, გამოიცნო რა სიტყვა დაწერა შოთამ ამ ასოებით. \n')
    game(words_to_play)



if __name__ == '__main__':
    main()
