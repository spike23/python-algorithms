def day_of_programmer(year):
    """

    :param year: a single integer denoting year y
    :return: the full date of Day of the Programmer during year y in the format dd.mm.yyyy,
    where dd is the two-digit day, mm is the two-digit month, and yyyy is y.
    """
    if year == 1918:
        return '26.09.1918'
    elif ((year <= 1917) & (year % 4 == 0)) or (
            (year > 1918) & (year % 400 == 0 or ((year % 4 == 0) & (year % 100 != 0)))):
        return '12.09.{}'.format(year)
    else:
        return '13.09.{}'.format(year)


if __name__ == '__main__':
    """
    2016
    1800
    2017
    """
    year = int(input().strip())
    result = day_of_programmer(year)
    print(result)
