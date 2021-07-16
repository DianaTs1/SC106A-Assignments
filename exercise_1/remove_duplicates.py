"""""
Remove duplicates from a given list and return a new list 
"""""


# def remove_duplicates(list):
#     new_list = []
#     for elem in list:
#         if elem not in new_list:
#             new_list.append(elem)
#     return new_list

def remove_duplicates(lst):
    new_list = []
    [new_list.append(elem) for elem in lst if elem not in new_list]
    return new_list


def main():
    my_list = [2, 5, 6, 7, 8, 8, 8]
    my_list2 = [2, 5, 6, 7, 8, 9, 9, 2, 5, 8, 8, 8]
    print(remove_duplicates(my_list))
    print(remove_duplicates(my_list2))



if __name__ == "__main__":
    main()