MOON_WEIGHT_INDEX = 16.5 / 100


def main():
    print("This program will calculate your weight on the Moon")
    user_weight = (float(input("Enter your weight: ")))
    user_moon_weight = user_weight * MOON_WEIGHT_INDEX
    if user_moon_weight < 0:
        print("Sorry, you can't have a negative weight.")
    else:
        print(f"Your weight on the moon is {user_moon_weight}")


if __name__ == '__main__':
    main()
