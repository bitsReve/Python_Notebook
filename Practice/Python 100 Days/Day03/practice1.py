value = float(input('Please input the value: '))
unit = input('Please input the unit: ')
if unit == 'centimeter':
    print('Your value as inch unit is %f' % (value/2.54))
elif unit == 'inch':
    print('Your value as centimeter unit is %f' % (value*2.54))
else:
    print('Wrong unit')
