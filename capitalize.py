

def solve(s):
    """

    :param s: a single line of input containing the full name
    :return: the capitalized string
    """
    tmp_list = s.split(' ')
    new_lst = [i.capitalize() if i.isalpha() else i for i in tmp_list]
    res = ' '.join(new_lst)
    return res


if __name__ == '__main__':
    """
    chris alan
    """
    s = input()
    result = solve(s)
    print(result)
