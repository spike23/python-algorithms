

def staircase(n):
    """

    :param n: a single integer, , denoting the size of the staircase
    :return: None
    """
    for i in range(n):
        i += 1
        print(('#'*i).rjust(n))


if __name__ == '__main__':
    """
    6
    """
    n = int(input())
    staircase(n)
