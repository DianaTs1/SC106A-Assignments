import random

def random_sentinel():
    while True:
        user_name = input("Enter your name (Q to quit): ")
        random_years = random.randint(1, 100)
        if user_name == "Q":
            break
        print(f'Hellos {user_name}! You have {random_years} years left!')


def main():
    random_sentinel()


if __name__ == '__main__':
    main()
