def add(arr, n, level):
    if level == 1:
        arr[n] = True
    elif arr[n//level] is not None:
        add(arr[n//level], n%level, level//10)
    else:
        arr[n//level] = [None]*10
        add(arr[n//level], n%level, level//10)
    pass


def check(arr, n, level):
    if level == 1:
        if arr[n] == True:
            return True
        else:
            arr[n] = True
            return False
    elif arr[n//level] is None:
        add(arr, n, level)
        return False
    else:
        return check(arr[n//level], n%level, level//10)

n=8
main_arr = [None]*10
print(check(main_arr, 12, 10**n))
print(check(main_arr, 24, 10**n))
print(check(main_arr, 45, 10**n))
print(check(main_arr, 12, 10**n))
pass



