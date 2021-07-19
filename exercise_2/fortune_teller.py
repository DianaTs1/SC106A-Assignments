def main():
    print("This program will tell you fortune")
    your_name = input('Enter your name: ')
    your_age = input('Enter your age: ')
    your_age = int(your_age)
    max_age = 100
    years_left = (max_age - your_age)
    print(f'Hello {your_name}, you have {years_left} years left!')

if __name__ == '__main__':
    main()
