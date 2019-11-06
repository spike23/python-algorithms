

def min_max_sum(arr):
    count = 0
    for i in range(len(arr)):
        count += arr[i]
    min_val = count - max(arr)
    max_val = count - min(arr)
    return min_val, max_val


if __name__ == '__main__':
    """
    1 2 3 4 5
    """
    arr = list(map(int, input().rstrip().split()))
    min_val, max_val = min_max_sum(arr)
    print(min_val, max_val, end='')
