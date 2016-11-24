#!/usr/bin/python
# -*- coding:utf-8 -*-

import operator
#对于某二分类问题，若够早了10个正确率都是0.6的分类器，采用少数服从多数的原则进行最终分类，则最终分类正确率是多少？
#若构造100个分类器呢

def c(n, k):
    return reduce(operator.mul, range(n-k+1, n+1)) / reduce(operator.mul, range(1, k+1))


def bagging(n, p):
    s = 0
    for i in range(n / 2 + 1, n + 1):
        s += c(n, i) * p ** i * (1 - p) ** (n - i)
    return s


if __name__ == "__main__":
    for t in range(10, 101, 10):
        print t, '次采样正确率：', bagging(t, 0.6)


