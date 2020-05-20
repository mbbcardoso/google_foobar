#!/usr/bin/env python
# coding: utf-8

def sort_int(n, desc=False):
    s = [int(i) for i in n]
    s.sort(reverse=desc)    
    return ''.join(map(str, s))

def base_diff(x, y, b):
    x = [i for i in x]
    y = [i for i in y]
    diffs = []
    for i in range(1,len(x)+1):
        diff = int(x[-i]) - int(y[-i])
        if diff < 0:
            diff = b + int(x[-i]) - int(y[-i]) 
            for k in range(i+1,len(x)+1):
                if x[-k] != '0':
                    x[-k] = str(int(x[-k]) - 1)
                    break
                else:
                    x[-k] = str(b-1)
        diffs.append(diff)
    diffs.reverse()
    return int(''.join(map(str, diffs)))

def solution(n, b):
    k = len(n)
    ns = []
    while True:
        x = sort_int(n, True)
        y = sort_int(n)
        z = base_diff(x, y, b)
        next_n = str(z)
        for i in range(0,k - len(str(z))):
            next_n = '0' + next_n
        if next_n in ns:
            return len(ns[ns.index(next_n):])
        ns.append(next_n)
        n = next_n

