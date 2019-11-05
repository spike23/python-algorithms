

def is_leap(year):
    """

    :param year: the year that needs to be checked
    :return: a boolean value
    """
    leap = False
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        leap = True
        return leap
    return leap


if __name__ == '__main__':
    year = int(input())
    print(is_leap(year))
