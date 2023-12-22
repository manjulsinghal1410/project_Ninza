def validString(input1: str) -> int:
    i = 0
    result = True
    while i < len(input1):
        if ord(input1[i]) <= 41 or ord(input1[i]) >= 65:
            result = False
        i += 1
    return result


def calculateSum(input1: str) -> int:
    i = 0
    v = 0
    sum = 0
    lastIndex = 43
    while i < len(input1):
        if 48 <= ord(input1[i]) <= 57:
            v = v * 10 + ord(input1[i]) - ord('0')
        if ord(input1[i]) == 43 or ord(input1[i]) == 42 or (i == len(input1) - 1):
            if lastIndex == 43:
                sum = sum + v
                v = 0
            elif lastIndex == 42:
                sum = sum * v
                v = 0
            lastIndex = ord(input1[i])
        i = i + 1
    return  sum


def evaluate(input1: str) -> int:
    if not validString(input1):
        return 0
    sum = calculateSum(input1)
    return sum


if __name__ == '__main__':
    print(evaluate('36+4+10+2'))
    print(evaluate('1*2'))
    print(evaluate('12*10+12'))
    print(evaluate('0'))
    print(evaluate("abd34"))
    print(evaluate("+45+56"))
