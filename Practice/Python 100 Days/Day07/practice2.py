import random


def code_generator(length=4):
    source = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    last_pos = len(source) - 1
    code = ''
    while length > 0:
        index = random.randint(0, last_pos)
        code += source[index]
        length -= 1
    return code


if __name__ == '__main__':
    code = code_generator()
    print(code)
