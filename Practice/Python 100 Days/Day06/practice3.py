def is_prime(a):
    for num in range(1, int(a ** 0.5) + 1):
        if a % num == 0:
            return False
        else:
            return True

