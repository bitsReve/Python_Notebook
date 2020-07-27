for num in range(10, 1000):
    if num >= 100:
        a = num // 100
        b = num // 10 % 10
        c = num % 10
        if a**3 + b**3 + c**3 == num:
            print(num)
    else:
        a = num // 10
        b = num % 10
        if a**3 + b**3 == num:
            print(num)
