import typing


def evaluate(input1: str) -> int:
    i = 0
    sum = 0
    v = 0
    while i < len(input1):
        if input1[i] != '+':
            v = v * 10 + ord(input1[i]) - ord('0')
        if input1[i] == '+' or i == len(input1) - 1:
            sum = sum + v
            v = 0
        i = i + 1
    return sum


if __name__ == '__main__':
    print(evaluate('36+4+10+2'))
    print(evaluate('1+2'))
    print(evaluate('12+12+12+12'))
    print(evaluate('0'))

