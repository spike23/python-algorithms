
def print_formatted(number):
    """

    :param number: a single integer
    :return: print lines where each line contains the respective decimal, octal, capitalized hexadecimal, and binary
    values
    """
    width = len(bin(n)) - 2
    for i in range(1, number+1):
        print("{0:>{w}d} {0:>{w}o} {0:>{w}X} {0:>{w}b}".format(i, w=width))


if __name__ == '__main__':
    """
    17
    """
    n = int(input())
    print_formatted(n)
