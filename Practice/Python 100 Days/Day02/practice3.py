y = int(input('Please input year: '))
is_leap = False
if y % 4 == 0 & y % 100 != 0:
    is_leap = True
if y % 400 == 0:
    is_leap = True

if is_leap:
    print('The year you input is leap year')
else:
    print('The year you input is not leap year')
