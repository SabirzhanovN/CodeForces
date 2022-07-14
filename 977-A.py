def definition(x) -> bool:
    x = str(x)
    # if x[-1] == 0:
    #     return True
    # else:
    #     return False
    return True if x[-1] == '0' else False


def subtraction(x):
    return x - 1


def division(x):
    return x // 10


def main():
    n, k = map(int, input().split())

    for i in range(k):
        # if definition(n) is True:
        #     n = division(n)
        # else:
        #     n = subtraction(n)
        n = division(n) if definition(n) is True else subtraction(n)
    return n


if __name__ == '__main__':
    print(main())
