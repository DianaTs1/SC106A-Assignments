
def main():
    print("This program subtracts one number from another.")
    try:
        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))
        subtract = first_number - second_number
        print(f"The result is {subtract}.")
    except ValueError:
        print("Please type a number")


if __name__ == '__main__':
    main()
