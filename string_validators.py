

def string_validators(n):
    """

    :param n: a string
    :return:  find out if the string alphanumeric characters, alphabetical characters, digits, lowercase and uppercase
    characters
    """
    print(any(map(str.isalnum, n)))
    print(any(map(str.isalpha, n)))
    print(any(map(str.isdigit, n)))
    print(any(map(str.islower, n)))
    print(any(map(str.isupper, n)))


if __name__ == '__main__':
    """
    qA2
    """
    s = input()
    string_validators(s)




