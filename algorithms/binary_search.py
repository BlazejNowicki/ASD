# znajduje najmniejsze wystąpienie x
def binary_search(T, x):
    l = 0
    r = len(T)-1
    while l < r:
        mid = (l+r)//2
        if T[mid] >= x:
            r = mid
        else:
            l = mid+1
    return l if T[l] == x else None


T = list(range(15))
print(T)
for x in [3, 7, 8, 9, 14, 15, 1, -1]:
    print(binary_search(T, x))
