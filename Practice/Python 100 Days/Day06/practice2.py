def is_palindromic_num(a):
    b = 0
    a1 = a
    while a1 != 0:
        b = b * 10 + a1 % 10
        a1 //= 10
    if a == b:
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_palindromic_num(121))

