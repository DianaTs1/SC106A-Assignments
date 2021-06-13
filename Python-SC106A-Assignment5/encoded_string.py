def expand_encoded_string(encoded):
    result = ""
    new_dictionary = {}

    for i in range(len(encoded)):
        if i % 2 == 0:                                    # We know what letters are located on even indexes and 0
            new_dictionary[encoded[i]] = encoded[i + 1]   # For each letter/key, the value is what's on next index(i+1)

    for key in new_dictionary:
        for i in range(int(new_dictionary[key])):         # Do string concatenation [value] times for each letter/key
            result += key

    return result


def main():
    result = expand_encoded_string('B4')
    print(result)      # should print: BBBB

    result = expand_encoded_string('m1e2t1')
    print(result)      # should print: meet

    result = expand_encoded_string('B1o2k2e2p1e1r1!3')
    print(result)      # should print: Bookkeeper!!!


if __name__ == '__main__':
    main()
