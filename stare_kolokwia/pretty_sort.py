from random import randint


def decompose(num: int):
    digits = [0]*10
    while True:
        digits[num % 10] += 1
        num //= 10
        if num < 1:
            break
    return digits


def single(num: int):
    digits = decompose(num)
    ans = 0
    for digit in digits:
        if digit == 1:
            ans += 1
    return 9 - ans


def multiple(num: int):
    digits = decompose(num)
    ans = 0
    for digit in digits:
        if digit > 1:
            ans += 1
    return ans


def counting_sort(A: list, B: list, key):
    length = len(A)
    C = [0]*10
    for i in range(length):
        C[key(A[i])] += 1
    for i in range(1, 10):
        C[i] = C[i-1] + C[i]
    for i in range(length-1, -1, -1):
        index = key(A[i])
        B[C[index]-1] = A[i]
        C[index] -= 1


def pretty_sort(T: list):
    TT = [0]*len(T)
    counting_sort(T, TT, multiple)
    counting_sort(TT, T, single)


if __name__ == "__main__":
    n = 10
    T = [randint(0, 10**4) for _ in range(n)]
    pretty_sort(T)
    print(T)
