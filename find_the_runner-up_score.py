

if __name__ == '__main__':
    """
    5
    2 3 6 6 5
    """
    n = int(input())
    arr = list(map(int, input().split()))
    new_arr = set(arr)
    res = sorted(list(new_arr), reverse=True)[1]
    print(res)
