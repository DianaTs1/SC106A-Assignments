import math


def main():
    print("Enter values to compute the Pythagorean theorem.")
    a = float(input("a: "))
    b = float(input("b: "))
    c = math.sqrt(a**2 + b**2)
    print(f'c = {c}')


if __name__ == '__main__':
    main()
