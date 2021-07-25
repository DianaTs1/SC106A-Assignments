import random


def main():
    print("This program generates random numbers for you.")
    quantity_of_random_numbers = int(input("How many numbers would you like to generate? "))
    minimum_number = int(input("Enter the minimum number: "))
    maximum_number = int(input("Enter the maximum number: "))
    for i in range(quantity_of_random_numbers):
        random_number = random.randint(minimum_number, maximum_number)
        print(f"This time the function generated: {random_number}")


if __name__ == '__main__':
    main()
