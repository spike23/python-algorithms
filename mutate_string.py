

def mutate_string(string, position, character):
    tmp_lst = list(string)
    for x in range(1, len(tmp_lst)):
        if x == position:
            tmp_lst[x] = character
    return ''.join(tmp_lst)


if __name__ == '__main__':
    """
    abracadabra
    5 k
    """
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
