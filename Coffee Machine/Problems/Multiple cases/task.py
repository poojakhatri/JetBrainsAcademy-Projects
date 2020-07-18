def f1(x):
    x = x * x + 1
    return x


def f2(x):
    x = (1 / (x ** 2))
    return x


def f3(x):
    x = x * x - 1
    return x


def f(x):
    if x <= 0:
        return f1(x)

    elif 0 < x < 1:
        return f2(x)

    else:
        return f3(x)
