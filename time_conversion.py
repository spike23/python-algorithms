from datetime import datetime


def time_conversion(s):
    """

    :param s: a time in 12-hour clock format
    :return: converted the given time in 24-hour format
    """
    return datetime.strptime(s, '%I:%M:%S%p').strftime('%H:%M:%S')


if __name__ == '__main__':
    """
    07:05:45PM
    """
    s = input()
    result = time_conversion(s)
    print(result)
