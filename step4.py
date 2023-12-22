def validString(input1: str) -> int:
    i = 0
    result = True
    while i < len(input1):
        if ord(input1[i]) <= 41 or ord(input1[i]) >= 65:
            result = False
        i += 1
    return result


def firstIndex(input1: str) -> int:
    i = 0
    while i < len(input1):
        if ord(input1[i]) == 42:
            return 1
        elif ord(input1[i]) == 43:
            return 0
        i += 1
    return -1


def lastIndex(input1: str) -> int:
    i = len(input1) - 1
    while i >= 0:
        if ord(input1[i]) == 42:
            return 42
        elif ord(input1[i]) == 43:
            return 43
        i -= 1
    return -1


def calculateSum(input1: str, sum: int, lastValue: int) -> int:
    i = 0
    v = 0
    while i < len(input1):
        if 48 <= ord(input1[i]) <= 57:
            v = v * 10 + ord(input1[i]) - ord('0')
            print("v", v)
        if ord(input1[i]) == 43 or ord(input1[i]) == 42 or i == len(input1) - 1:
            if ord(input1[i]) == 43 or (i == len(input1) - 1 and lastValue == 43):
                sum = sum + v
                v = 0
            if ord(input1[i]) == 42 or (i == len(input1) - 1 and lastValue == 42):
                sum = sum * v
                print("sum multiply",sum)
                v = 0
        i = i + 1
    return  sum


def evaluate(input1: str) -> int:
    if not validString(input1):
        return 0
    sum = firstIndex(input1)
    print("first",sum)
    lastValue = lastIndex(input1)
    print("last",lastValue)
    sum = calculateSum(input1, sum, lastValue)
    return sum


if __name__ == '__main__':
    #print(evaluate('36+4+10+2'))
    #print(evaluate('1*2'))
    print(evaluate('12*10+12'))
    # print(evaluate('0'))
