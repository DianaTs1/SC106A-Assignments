def average(arr):
    return round(sum(arr)/len(arr), 2)


# calculates median in a sorted array
def median(arr):
    arr.sort()
    if len(arr) % 2 == 1:
        index = int((len(arr) - 1) / 2)
        return arr[index]
    else:
        index2 = int(len(arr)/2)
        index1 = index2-1
        average = (arr[index1] + arr[index2]) / 2
        return average


def main():
    # Create an empty array where inputs (number) will be appended
    array = []
    while True:
        number = input("Enter your number (Q to quit): ")
        if number == "Q":
            break
        else:
            array.append(float(number))
    if len(array) > 0:
        print(F"You entered {len(array)} numbers, here are some stats: "
              F"\nsum: {sum(array)}, min: {min(array)}, max: {max(array)}, \naverage: {average(array)}, median: {median(array)}")


if __name__ == '__main__':
    main()
