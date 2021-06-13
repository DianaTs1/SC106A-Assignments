INPUT_FILE = 'bill2.txt'


# ხერხი 1
def calculate_total_expenses():
    final_dict = {}
    # Read a file and turn necessary key-values into a dictionary
    with open(INPUT_FILE) as file:
        for line in file:
            line = line.strip()
            key = line[line.find("[")+1:line.find("]")]             # Get a value in between brackets
            line = line.split(" ")                                  # Turn a string into a list
            value = int(line[- 1].replace("$", ""))       # Remove $, turn srt into int to make calculations

            if key in final_dict:
                final_dict[key] += value
            else:
                final_dict[key] = value

    return final_dict


"""
second try with tuples
"""
# def create_tuple():                                          # Separate for Stores and Money spent
#     stores = []
#     money = []
#     with open(INPUT_FILE) as file:
#         for line in file:
#             line = line.strip()
#             stores.append(line[line.find("[") + 1:line.rfind("]")])
#             line = line.split(" ")
#             money.append(int(line[len(line) - 1].replace("$", "")))
#     return list(zip(stores, money))
#
#
# def sum_tuple_values(zipped_lists):
#     final_dict = {}
#     for i in range(len(zipped_lists)):
#         key = zipped_lists[i][0]
#         value = zipped_lists[i][1]
#         if key in final_dict:
#             final_dict[key] += value
#         else:
#             final_dict[key] = value
#     return final_dict


def main():
    print("Your total expenses are:")
    final_dict = calculate_total_expenses()
    for key, value in final_dict.items():
        print(f"{key}: {value}")

    """
    Second try tests
    """
    # tpl = create_tuple()
    # final_dict = sum_tuple_values(tpl)
    # print("Your total expenses are:")
    # for key, value in final_dict.items():
    #     print(f"{key}: {value}")


if __name__ == '__main__':
    main()
