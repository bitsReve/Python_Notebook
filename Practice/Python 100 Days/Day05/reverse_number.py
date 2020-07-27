num = int(input('Enter your number:'))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num = num // 10
print('Your number reversed is %d' % reversed_num)
