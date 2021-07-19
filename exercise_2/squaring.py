def main():
    print('This program will square your number.')
    num = input('Enter your number: ')
    num = int(num)
    square_num = num * num
    print(f"{num}*{num} = {square_num}")

if __name__ == '__main__':
    main()
