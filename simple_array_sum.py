

def plus_minus(arr):
    """
    https://www.hackerrank.com/challenges/plus-minus/problem
    :param arr: data array
    :return: The proportions of occurrence
    """
    arr_len = len(arr)
    pos = sum(map(lambda x: x > 0, arr))
    neg = sum(map(lambda x: x < 0, arr))
    zer = sum(map(lambda x: x == 0, arr))
    return pos / arr_len, neg / arr_len, zer / arr_len


if __name__ == '__main__':
    """
    6
    -4 3 -9 0 4 1         
    """
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    a, b, c = plus_minus(arr)
    print(a)
    print(b)
    print(c)