def checkBit(number, checkBit):
    for i in range(checkBit):
        number >>= 1

    if number & 1:
        return 1
    else:
        return 0


if __name__ == "__main__":
    A = int(input())
    B = int(input())

    print(checkBit(A, B))
