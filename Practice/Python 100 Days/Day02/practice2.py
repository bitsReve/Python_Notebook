import math

r = float(input('Please input radius: '))
p = r * 2 * math.pi
a = 0.5 * math.pi * pow(r, 2)
print('The perimeter is %.1f, and the area is %.1f' % (p, a))
