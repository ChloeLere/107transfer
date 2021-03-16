#!/usr/bin/env python3

import sys
import math
import numpy as np

def calc_one_loop(num, den, x):
    f_num = 0
    f_den = 0
    t_den = den.split('*', len(den))
    s_den = len(t_den)
    t_num = num.split('*', len(num))
    s_num = len(t_num)
    while s_num > 0:
            s_num -= 1
            f_num = f_num * x + float(t_num[s_num])
    while s_den > 0:
        s_den -= 1
        f_den = f_den * x + float(t_den[s_den])
    if f_den != 0:
        return f_num / f_den
    return -84

def calc_transfer(argv, argc):
    f_num = 0
    f_den = 0
    stop = 0
    temp = argv[1]
    t_num = temp.split('*', len(argv[1]))
    s_num = len(t_num)
    temp2 = argv[2]
    t_den = temp2.split('*', len(argv[2]))
    s_den = len(t_den)
    st_num = s_num
    st_den = s_den
    x = 0
    res = 1
    for x in np.arange(0, 1.001, 0.001):
        while s_num > 0:
            s_num -= 1
            f_num = f_num * x + float(t_num[s_num])
        s_num = st_num
        while s_den > 0:
            s_den -= 1
            f_den = f_den * x + float(t_den[s_den])
        s_den = st_den
        if f_den != 0:
            res = f_num / f_den
        if argc <= 2:
            print("%.3f" % x ,"->", "{:.{n}f}".format(res,n = 5))
        if argc > 2:
            for i in np.arange(2, int(argc), 2):
                temp = calc_one_loop(argv[i + 1], argv[i + 2], x)
                if temp == -84:
                    stop = 1
                else:
                    res = res * temp
            if stop == 0:
                print("%.3f" % x ,"->", "{:.{n}f}".format(res,n = 5))
        res = 1
        f_num = 0
        f_den = 0
        stop = 0