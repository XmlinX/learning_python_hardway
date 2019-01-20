from functools import reduce


def prod(L):
    return reduce(lambda x, y: x*y, L)


if __name__ == "__main__":
    L = [2, 3, 4, 5]
    a = prod(L)
    print(a)


