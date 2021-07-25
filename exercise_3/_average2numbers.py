"""
the parentheses there used in a wrong way. the program was doing the division
first (num2/2) and then the sum. I also changed the name 'total' into 'average'
since it's more appropriate.
"""


def main():
    print("This program averages two numbers.")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    average = (num1 + num2) / 2
    print(f"The average is {average}.")


if __name__ == '__main__':
    main()
