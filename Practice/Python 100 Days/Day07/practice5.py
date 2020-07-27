def is_leap_year(x):
    return x % 4 == 0 and x % 100 != 0 or x % 400 == 0


def which_day(year, month, date):
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30],
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    ][is_leap_year(year)]
    days = date
    for i in range(0, month - 1):
        days += days_of_month[i]
    return days


if __name__ == '__main__':
    print(which_day(2020, 7, 22))
