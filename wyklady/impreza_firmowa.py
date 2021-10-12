class Employee:
    def __init__(self, fun):
        self.emp = []
        self.f = -1
        self.g = -1
        self.fun = fun


def f(v: Employee):
    if v.f >= 0:
        return v.f
    x = v.fun
    for u in v.emp:
        x += g(u)
    y = g(v)
    v.f = max(x, y)
    return v.f


def g(v: Employee):
    if v.g >= 0:
        return v.g
    v.g = 0
    for u in v.emp:
        v.g += f(u)
    return v.g

#            a(7)
#         /   |    \
#      b(3)   c(5)   d(11)
#     /  |    |     |     \
# x(13) y(17) z(19) u(23)  v(29)


if __name__ == "__main__":
    a, b, c, d, x, y, z, u, v = (Employee(i)
                                 for i in [7, 3, 5, 11, 13, 17, 19, 23, 29])
    a.emp = [b, c, d]
    b.emp = [x,y]
    c.emp = [z]
    d.emp = [u, v]

    print(f(a))