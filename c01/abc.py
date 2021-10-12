def check(n):
    sumt=0
    for i in range(1, n//2+1):
        if n%i==0:
            sumt += i
    if sumt == n:
        print(n)

for i in range(1, 100000):
    check(i)