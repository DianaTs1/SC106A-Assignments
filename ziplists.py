def zip2lists(list1, list2):
    final_list = []
    for i in range(len(list1)):
        pairs = []
        pairs.append(list1[i])
        pairs.append(list2[i])
        final_list.append(pairs)
    return final_list


def main():
    result_list = zip2lists(['a', 'b', 'c'], ['d', 'e', 'f'])
    print(result_list)      # should print [['a', 'd'], ['b', 'e'], ['c', 'f']]
    print(zip2lists(['one'], ['two']))
    print(zip2lists([], []))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
