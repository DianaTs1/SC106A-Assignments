def read_list():
    number_list = []
    while True:
        number = int(input("Enter value (0 to stop): "))
        if number == 0:
            break
        number_list.append(number)
    return number_list


def remove_duplicates(num_list):
    single_characters = []
    for elem in num_list:
        if elem not in single_characters:
            single_characters.append(elem)
    return single_characters


def main():
    num_list = read_list()
    print("Original list entered by user: ")
    print(num_list)

    no_duplicates = remove_duplicates(num_list)
    print("List with duplicates removed: ")
    print(no_duplicates)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
