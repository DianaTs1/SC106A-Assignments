def greater_than_10(numbers):
    filtered_numbers = [number for number in numbers if number > 10]
    return filtered_numbers


def other_greater_than_10(num_list):
    final_list = []
    for elem in num_list:
        if elem > 10:
            final_list.append(elem)
    return final_list


def main():
    list1 = [20, 6, 12, -3, 14]
    result_list = greater_than_10(list1)
    print(result_list)      # should print [20, 12, 14]

    list2 = [16]
    result_list = other_greater_than_10(list2)
    print(result_list)      # should print [16]

    list3 = [1, 2, 3, 4]
    result_list = other_greater_than_10(list3)
    print(result_list)      # should print []

    list4 = []
    result_list = greater_than_10(list4)
    print(result_list)      # should print []


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
