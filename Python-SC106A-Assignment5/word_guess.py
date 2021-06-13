import random


LEXICON_FILE = "TestLexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Initial number of guesses player starts with


# This function updates a word if the user guesses a letter correctly
def update_secret_word(dashed_word, secret_word, letter):
    temp_list = list(dashed_word)
    for i in range(len(secret_word)):
        if secret_word[i] == letter.upper():
            temp_list[i] = letter
    dashed_word = "".join(temp_list)
    return dashed_word


def get_word():
    with open(LEXICON_FILE) as file:
        lexicon = [line.strip() for line in file]
    index = random.randrange(len(lexicon))
    return lexicon[index]


def play_game(secret_word):
    dashed_word = '_' * len(secret_word)
    wrong_guess = 0

    while wrong_guess != INITIAL_GUESSES:
        if '_' not in dashed_word:
            print(f"Congratulations, the word is: {secret_word}")
            break

        print(f"The word now looks like this: {dashed_word}")
        print(f"You have {INITIAL_GUESSES - wrong_guess} guesses left")
        letter = input("Type a single letter here, then press enter: ").upper()

        if len(letter) > 1 or len(letter) == 0:
            print("Guess should only be a single character.")

        elif letter not in secret_word:
            wrong_guess += 1
            print(f"There are no {letter}'s in the word")

        else:
            print("The guess is correct")

        dashed_word = update_secret_word(dashed_word, secret_word, letter)

    else:
        print(f"Sorry, you lost. The secret word was: {secret_word}")


def repeat_game(secret_word):
    while True:
        answer = input("\nWould You like to play again? (Type 'Yes' or 'No'): ")
        if answer.upper().strip() == "YES":
            play_game(secret_word)
        elif answer.upper().strip() == "NO":
            print("Than you for playing, Amigo! See you next time!")
            break
        else:
            print("Please type 'Yes' or 'No'")


def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    print("Let's play a word guess game")
    secret_word = get_word()
    play_game(secret_word)
    repeat_game(secret_word)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()