def load_data(filename):
    """
    The function takes in the name of a datafile (string), which
    contains data on locations and their seven day cumulative number
    of infections.  The function returns a dictionary in which the
    keys are the locations in the data file, and the value associated
    with each key is a list of the (integer) values presenting the
    cumulative number of infections at that location.
    >>> load_data('disease1.txt')
    {'Evermore': [1, 1, 1, 1, 1, 1, 1], 'Vanguard City': [1, 2, 3, 4, 5, 6, 7], 'Excelsior': [1, 1, 2, 3, 5, 8, 13]}
    """
    final_dict = {}

    with open(filename) as file:
        for line in file:
            line = line.split(",")
            key = line[0].strip()
            for i in range(1, len(line)):
                value = int(line[i].strip())
                if key not in final_dict:
                    final_dict[key] = [value]
                else:
                    final_dict[key].append(value)

    return final_dict


def daily_cases(cumulative):
    """
    The function takes in a dictionary of the type produced by the load_data
    function (j.e., keys are locations and values are lists of seven values
    representing cumulative infection numbers).  The function returns a
    dictionary in which the keys are the same locations in the dictionary
    passed in, but the value associated with each key is a list of the
    seven values (integers) presenting the number of new infections each
    day at that location.
    >>> daily_cases({'Test': [1, 2, 3, 4, 4, 4, 4]})
    {'Test': [1, 1, 1, 1, 0, 0, 0]}
    >>> daily_cases({'Evermore': [1, 1, 1, 1, 1, 1, 1], 'Vanguard City': [1, 2, 3, 4, 5, 6, 7], 'Excelsior': [1, 1, 2, 3, 5, 8, 13]})
    {'Evermore': [1, 0, 0, 0, 0, 0, 0], 'Vanguard City': [1, 1, 1, 1, 1, 1, 1], 'Excelsior': [1, 0, 1, 1, 2, 3, 5]}
    """
    new_dictionary = {}

    for key in cumulative:
        value_list = cumulative.get(key).copy()   # Copy the information so the old version does not get updated
        for elem in range(1, len(value_list)):
            value_list[elem] = cumulative[key][elem] - cumulative[key][elem-1]
            new_dictionary[key] = value_list

    return new_dictionary

def main():
    filename = 'disease1.txt'

    data = load_data(filename)
    print(f"Loaded datafile {filename}:")
    print(data)

    print("Daily infections: ")
    print(daily_cases(data))


if __name__ == '__main__':
    main()




# def daily_cases(cumulative):
#     new_dictionary = {}
#
#     keys = list(cumulative.keys())                      # Getting the keys
#     for key in keys:
#         value_list = cumulative[key]                    # Getting the lists separately
#         for i in range(1, len(value_list)):             # Ignoring the first element
#             new_value = value_list[i]-value_list[i-1]   # This Calculates new cases every day
#
#             if key not in new_dictionary:
#                 new_dictionary[key] = [value_list[0]]   # Getting that ignored element and assign it as first value
#                 new_dictionary[key].append(new_value)   # Add the first subtracted value to the list
#             else:
#                 new_dictionary[key].append(new_value)   # Add the rest subtracted values to the list
#
#     return new_dictionary

