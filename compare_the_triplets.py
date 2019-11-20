

def compare_triplets(a, b):
    total_a = 0
    total_b = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            total_a = total_a + 1
        elif a[i] < b[i]:
            total_b = total_b + 1
    return total_a, total_b


if __name__ == '__main__':
    """
    5 6 7
    3 6 10
    """
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    result = compare_triplets(a, b)
    print(result)
