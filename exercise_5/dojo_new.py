def is_empty(a_list):
    return len(a_list) > 0


def safe_delete2(a_list, elem):
    if elem in a_list:
        a_list.remove(elem)
        return a_list


def delete_all(a_list, elem):
    while elem in a_list:
        a_list.remove(elem)
    return a_list


def main():
    print(is_empty([1]))
    print(delete_all([1, 2, 3, 7, 8, 9, 0, 1, 0, 0], 0))
    print(is_empty([1, 2]))


if __name__ == '__main__':
    main()
