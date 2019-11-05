

def diagonal_difference(arr):
    """

    :param arr: data array
    :return: the absolute difference between the sums of the matrix's two diagonals as a single integer
    """
    diff = 0
    v_len = len(arr)
    for idx in range(v_len):
        diff += arr[idx][idx]
        diff -= arr[idx][v_len-idx-1]
    return abs(diff)


if __name__ == '__main__':
    """
    3
    11 2 4
    4 5 6
    10 8 -12
    """
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonal_difference(arr)
    print(result)
