from zad3testy import runtests
from math import floor, log


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def fast_sort(tab, a):
    n = len(tab)
    T = [[] for _ in range(n+1)]
    for i in range(n):
        T[floor(n*log(tab[i], a))].append(tab[i])
    i = 0
    for bucket in T:
        insertion_sort(bucket)
        for value in bucket:
            tab[i] = value
            i += 1
    return tab


runtests(fast_sort)
