

def swap_case(s):
    """

    :param s: single line containing a string
    :return: the modified string
    """
    tmp_list = list(s)
    new_list = []
    for i in tmp_list:
        if i.isalpha() and i.islower():
            new_list.append(i.capitalize())
        elif i.isalpha() and i.isupper():
            new_list.append(i.lower())
        else:
            new_list.append(i)
    return ''.join(new_list)


if __name__ == '__main__':
    """
    HackerRank.com presents "Pythonist 2".
    """
    s = input()
    result = swap_case(s)
    print(result)
