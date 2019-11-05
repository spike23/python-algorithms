def count_substring(string, sub_string):
    """

    :param string:  original string
    :param sub_string: substring
    :return: the integer number indicating the total number of occurrences of the substring in the original string
    """
    cnt = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            cnt += 1
    return cnt


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
