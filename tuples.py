

if __name__ == '__main__':
    """
    2
    1 2
    """
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))
