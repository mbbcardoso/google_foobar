#!/usr/bin/env python
# coding: utf-8

# symbolic multiplication of univariate polynomials
def symb_mult(a, b):
    c = {}
    for i in a:
        for e in b:
            if i+e in c:
                c[i+e] += a[i] * b[e]
            else:
                c[i+e] = a[i] * b[e]
    return c

# following generating function described in
# https://math.stackexchange.com/questions/2081091
# by Dr. Wolfgang Hintze
def solution(n):
    a = {0: 1}
    for i in range(1,n+1):
        a = symb_mult(a, {i: 1, 0: 1})
    return a[n]-1

