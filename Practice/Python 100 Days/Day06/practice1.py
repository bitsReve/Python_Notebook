def greatest_common_divisor(a, b):
    (a, b) = (b, a) if b > a else (a, b)
    for factor in range(a, 0, -1):
        if a % factor == 0 and b % factor == 0:
            return factor


def least_common_multiple(a, b):
    (a, b) = (b, a) if b > a else (a, b)
    for multiple in range(1, a):
        if a * multiple % b == 0:
            return a * multiple


def lcm(x, y):
    """求最小公倍数"""
    return x * y // greatest_common_divisor(x, y)


if __name__ == '__main__':
    print(least_common_multiple(8, 6))
    print(lcm(8, 6))
