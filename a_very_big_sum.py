

def a_very_big_sum(ar):
    """

    :param ar: data arraay
    :return: integer sum of the elements in the array
    """
    return sum(ar)


if __name__ == '__main__':
    """
    5
    1000000001 1000000002 1000000003 1000000004 1000000005
    """
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = a_very_big_sum(ar)
    print(result)
