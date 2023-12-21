import typing


def splitInput(inputStr: str) -> typing.List[str]:
    return inputStr.split('+')


def getOrdValues(inputStr: str) -> int:
    v = 0
    for m in range(0,len(inputStr)):
        number = ord(inputStr[m]) - ord('0')
        v = v * 10 + number
    return v


if __name__ == '__main__':
    input1 = '36+4+10+2'
    modules = splitInput(input1)
    sum = 0
    for module in modules:
        number = getOrdValues(module)
        sum = sum + number

    print(sum)