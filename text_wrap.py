import textwrap


def wrap(string, max_width):
    """

    :param string: input string
    :param max_width: width of a paragraph
    :return: the text wrapped paragraph
    """
    tmp_list = textwrap.wrap(string, max_width)
    new_str = '\n'.join(tmp_list)
    return new_str


if __name__ == '__main__':
    """
    ABCDEFGHIJKLIMNOQRSTUVWXYZ
    4
    """
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
