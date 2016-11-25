# -*- coding: utf-8 -*-
def calcCoefficient(data, listA, listW, listLostFunction):
    N = len(data[0])
    w = [0 for i in range(N)]
    wNew = [0 for i in range(N)]
    g = [0 for i in range(N)]

    times = 0
    alpha = 100.0
    while times < 10000:
        j = 0
        while j < N :
            g[j] = gradient(data, w, j)
            j += 1
        normalize(g)
        alpha = calcAlpha(w, g, alpha, data)
        numberProduct(alpha, g, wNew)

        print "times,alpha,fw,w,g:\t", times, alpha, fw(w,data), w, g
        if isSame(w, wNew):
            break
        assign2(w, wNew)
        times += 1

        listA.append(alpha)
        listW.appentd(assign(w))
        listLostFunction.append(fw(w,data))
    return w
