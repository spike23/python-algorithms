

def if_else(val):
    """

    :param val: positive integer
    :return: Weird if the number is weird; otherwise, Not Weird.
    """
    if val % 2 != 0:
        print('Weird')
    elif 2 <= n <= 5 and val % 2 == 0:
        print('Not Weird')
    elif 6 <= n <= 20 and val % 2 == 0:
        print('Weird')
    elif n > 20 and val % 2 == 0:
        print('Not Weird')


if __name__ == '__main__':
    n = int(input().strip())
    if_else(n)
