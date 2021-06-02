import random

MIN_NUMBER = 15
MAX_NUMBER = 95


def main():
    number_of_users_correct_answer = 0
    while number_of_users_correct_answer < 3:
        first_number = random.randint(MIN_NUMBER, MAX_NUMBER)
        second_number = random.randint(MIN_NUMBER, MAX_NUMBER)
        print(f"What is {first_number} + {second_number}? ")
        user_answer = int(input("Your answer: "))
        correct_answer = first_number + second_number
        if user_answer == correct_answer:
            number_of_users_correct_answer += 1
            print(f"Correct! You have gotten {number_of_users_correct_answer} correct in a row")
        else:
            number_of_users_correct_answer = 0
            print(f"Incorrect! The expected answer is {correct_answer}")
    print("Congratulations! You mastered addition!")


if __name__ == '__main__':
    main()
