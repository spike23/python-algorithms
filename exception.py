

def exception_example(n):
    """

    :param n: number of test cases
    :return: print the error code
    """
    for _ in range(n):
        a, b = input().split()
        try:
            print(int(a) // int(b))
        except Exception as e:
            print('Error Code: ' + str(e))


if __name__ == '__main__':
    """
    3
    1 0
    2 $
    3 1
    """
    n = int(input())
    exception_example(n)
