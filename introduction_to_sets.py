

def average(array):
    """

    :param array: the n space separated heights of the plants
    :return: the average height value on a single line
    """
    new_array = set(array)
    res = sum(new_array) / len(new_array)
    return res


if __name__ == '__main__':
    """
    10
    161 182 161 154 176 170 167 171 170 174
    """
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
