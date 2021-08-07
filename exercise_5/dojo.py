def is_empty(a_list):
    if len(a_list) > 0:
        return True
    return False


def get_a_list_of_numbers(start, end):
    array = []
    for i in range(start, end):
        array.append(i)
    return array


def safe_pop(a_list):
    if len(a_list) == 0:
        return None
    return a_list.pop()


def safe_delete(a_list, elem):
    for element in a_list:
        if element == elem:
            a_list.remove(elem)
            return a_list

# OR
# def safe_delete2(a_list, elem):
#     if elem in a_list:
#         a_list.remove(elem)
#         return a_list


def delete_all(a_list, elem):
    for element in a_list:
        if element == elem:
            a_list.remove(elem)
    return a_list



def extend(list1, list2):
    list3 = []
    for elem in list1:
        list3.append(elem)
    for elem in list2:
        list3.append(elem)
    return list3


def count_occurrences(a_list, elem):
    number_occurrences = 0
    for element in a_list:
        if element == elem:
            number_occurrences += 1
    return number_occurrences


def main():
    print(is_empty([1]))
    print(get_a_list_of_numbers(1, 11))
    print(safe_pop([1, 2, 3, 7, 8, 9, 0, 1, 3]))
    print(safe_delete([1, 2, 3, 7, 8, 9, 0, 1, 0, 0], 0))
    # print(safe_delete2([1, 2, 3, 7, 8, 9, 0, 1, 0, 0], 7))
    print(delete_all([1, 2, 3, 7, 8, 9, 0, 1, 0, 0], 0))
    print(extend([1, 2, 3], [4, 5, 6]))
    print(count_occurrences([1, 5, 6, 6, 6, 4, 5, 4, 5], 4))

if __name__ == '__main__':
    main()
