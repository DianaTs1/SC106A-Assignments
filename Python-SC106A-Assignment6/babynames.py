"""
File: babynames.py
------------------
Add your comments here
"""

import sys


def add_data_for_name(name_data, year, rank, name):

    """
    Adds the given year and rank to the associated name in the name_data dictionary.

    Input:
        name_data (dictionary): dict holding baby name data
        year (int): the year of the data entry to add
        rank (int): the rank of the data entry to add
        name (str): the name of the data entry to add

    >>> name_data = {}
    >>> add_data_for_name(name_data, 2000, 10, 'Nick')
    >>> name_data
    {'Nick': {2000: 10}}
    >>> add_data_for_name(name_data, 2000, 200, 'Sonja')
    >>> name_data
    {'Nick': {2000: 10}, 'Sonja': {2000: 200}}
    >>> add_data_for_name(name_data, 2000, 100, 'Sonja')
    >>> name_data
    {'Nick': {2000: 10}, 'Sonja': {2000: 100}}
    """

    if name in name_data:
        if year in name_data[name]:
            if name_data[name][year] > rank:
                name_data[name][year] = rank
        else:
            name_data[name][year] = rank
    else:
        name_data[name] = {year: rank}


def add_file(name_data, filename):
    """
    >>> name_data = {}
    >>> add_file(name_data, 'data/small/small-2000.txt')
    >>> name_data
    {'A': {2000: 1}, 'B': {2000: 1}, 'C': {2000: 2}}
    >>> name_data = {}
    >>> add_file(name_data, 'data/small/small-2010.txt')
    >>> name_data
    {'C': {2010: 1}, 'D': {2010: 1}, 'A': {2010: 2}, 'E': {2010: 2}}
    >>> name_data = {'A': {2000: 1}, 'B': {2000: 1}, 'C': {2000: 2}}
    >>> add_file(name_data, 'data/small/small-2010.txt')
    >>> name_data
    {'A': {2000: 1, 2010: 2}, 'B': {2000: 1}, 'C': {2000: 2, 2010: 1}, 'D': {2010: 1}, 'E': {2010: 2}}
    """

    with open(filename) as file:
        # Get the first line (year) of each file
        year = file.readline()
        year = int(year.strip())

        # Get each line of the file and turn it info list
        for line in file:
            line = line.strip()
            line = line.split(",")

            # Strip each element of the line list
            for elem in range(len(line)):
                line[elem] = line[elem].strip()

            # Reach to the first(rank), second(male_name) and third(female_name) elements of the list
            rank = int(line[0])
            for name in range(1, len(line)):
                add_data_for_name(name_data, year, rank, line[name])


def read_files(filenames):
    name_data = {}
    for file in range(len(filenames)):
        add_file(name_data, filenames[file])
    return name_data


def search_names(name_data, target):
    list_of_matching_names = []

    for key in name_data:
        if target.lower() in key.lower():
            list_of_matching_names.append(key)

    return list_of_matching_names


def print_names(name_data):
    """
    (This function is provided for you)
    Given a name_data dictionary, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    Input:
        name_data (dictionary): a dictionary containing baby name data organized by name
    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    # (This function is provided for you)

    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
