# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
from functools import reduce


def str2float(L):
    def f(x, y):
        return 10*x + y
    n = L.index('.')
    s1 = list(map(int, [x for x in L[:n]]))
    s2 = list(map(int, [x for x in L[n+1:]]))
    return reduce(f, s1) + reduce(f, s2) / 10 ** len(s2)

    