import random


# Usually 'choice1' is considered to be made by a computer

def tie(choice1, choice2):
    if choice1 == choice2:
        print("It's a tie")


def computer_wins(choice1, choice2):
    if choice1 == 1 and choice2 == 3:
        print('You Lose! Rock crushes scissors')
    elif choice1 == 2 and choice2 == 1:
        print('You Lose! Paper beats rock')
    elif choice1 == 3 and choice2 == 2:
        print("You Lose! Scissors cut paper")


# adding there 'return True' parts so the program can calculate how many times the human won

def human_wins(choice1, choice2):
    if choice2 == 1 and choice1 == 3:
        print('You Win! Rock crushes scissors')
        return True
    elif choice2 == 2 and choice1 == 1:
        print('You Win! Paper beats rock')
        return True
    elif choice2 == 3 and choice1 == 2:
        print("You Win! Scissors cut paper")
        return True
    return False


def get_result(choice1, choice2):
    if human_wins(choice1, choice2):
        return True
    computer_wins(choice1, choice2)
    tie(choice1, choice2)
    return False


# adding these while loop so when the human types something different than 1, 2 or 3
# the program would not count that as a new round
def check_human_move():
    i = -1
    while i != 1 and i != 2 and i != 3:
        i = int(input("Your move(1, 2 or 3): "))
    return i


def main():
    amount_of_wins = 0
    for i in range(5):
        computer_choice = random.randint(1, 3)
        human_choice = check_human_move()
        if get_result(computer_choice, human_choice):
            amount_of_wins += 1
    print(f"You won " + str(amount_of_wins) + " rounds")


if __name__ == '__main__':
    main()
