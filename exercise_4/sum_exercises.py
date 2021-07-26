def sum_of_all_numbers(n):
    sum = 0
    for i in range(n-1):
        i += 1
        sum += i
    return sum


def sum_of_odd_numbers(n):
    a = -1
    sum = 0
    for i in range(n//2):
        a += 2
        sum += a
    return sum


def sum_of_even_numbers(n):
    sum = 0
    for i in range((n - 1) // 2):
        i += 2
        sum += i
    return sum


def main():
    print(sum_of_all_numbers(10))    # should print 35 (really???)
    print(sum_of_all_numbers(501))   # should print 125250
    #
    print(sum_of_odd_numbers(12))    # 36
    print(sum_of_odd_numbers(503))   # 63001
    print(sum_of_odd_numbers(502))   # 63001
    #
    print(sum_of_even_numbers(12))   # 30
    print(sum_of_even_numbers(502))  # 62750
    print(sum_of_even_numbers(501))  # 62750


if __name__ == '__main__':
    main()
