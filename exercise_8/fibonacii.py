def fibonacci(n):
    """
    >>> fibonacci(0)
    1
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    2
    >>> fibonacci(3)
    3
    >>> fibonacci(4)
    5
    >>> fibonacci(8)
    34
    >>> fibonacci(12)
    233
    """
    if n == 0 or n == 1:
        return 1
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
    return result

    # # მანამდე ესე მეწერა უბრალოდ
    # if n == 0:
    #     return 0
    # if n == 1:
    #     return 1
    # else:
    #     result = fibonacci(n-1) + fibonacci(n-2)
    # return result


def main():
    print(fibonacci(10))
    print(fibonacci(20))
    print(fibonacci(3))
    print(fibonacci(0))
    print(fibonacci(5))


if __name__ == '__main__':
    main()
