#!/usr/bin/env python
# coding: utf-8

from fractions import Fraction, gcd

def zero_matrix(i,j):
    z_m = []
    for a in range(i):
        z_m_r = []
        for b in range(j):
            z_m_r.append(0)
        z_m.append(z_m_r)
    return z_m


def sq_zero_to_id(z_m):
    for i in range(0,len(z_m)):
        z_m[i][i] = 1   
    return z_m


def sub_matrix(a, b):
    sub = []
    for i in range(len(a)):
        sub_r = []
        for j in range(len(b)):
            sub_r.append(a[i][j]-b[i][j])
        sub.append(sub_r)
    return sub


def mult_matrix(a, b):
    z_m = zero_matrix(len(a), len(b[0]))
        
    for i in range(len(a)):
        for j in range(len(b[0])):
            for x in range(len(a[0])):
                z_m[i][j] += a[i][x]*b[x][j]
    return z_m    


# modified function from https://integratedmlai.com/matrixinverse
def inv_matrix(a):
    n = len(a)
    
    id_m = sq_zero_to_id(zero_matrix(n,n))      
 
    indices = list(range(n))
    for fd in range(n):
        fdScaler = Fraction(1,1) / a[fd][fd]
        for j in range(n):
            a[fd][j] *= fdScaler
            id_m[fd][j] *= fdScaler
        for i in indices[0:fd] + indices[fd+1:]: 
            crScaler = a[i][fd]
            for j in range(n): 
                a[i][j] = a[i][j] - crScaler * a[fd][j]
                id_m[i][j] = id_m[i][j] - crScaler * id_m[fd][j]
    return id_m


def fraction_matrix(a):
    nrows = len(a)
    ncols = len(a[0])
    fr_m = zero_matrix(nrows, ncols)
    for i in range(nrows):
        for j in range(ncols):
            if a[i][j] != 0:
                fr_m[i][j] = Fraction(a[i][j],sum(a[i]))
    return fr_m


def lcm(a, b):
    return int(abs(a*b) / gcd(a, b))


def simp_fractions(frs):
    nums = [f.numerator for f in frs]
    denoms = [f.denominator for f in frs]
    lcm_ = reduce(lcm, denoms)
    ratios = [int(lcm_/d) for d in denoms]
    new_nums = [int(nums[i]*ratios[i]) for i in range(len(ratios))]
    gcds = reduce(gcd,new_nums+[lcm_])
    simp_nums = [int(n/gcds) for n in new_nums]
    simp_denom = int(lcm_/gcds)
    return simp_nums+[simp_denom]    


def is_canonical(a):
    for i in range(1,len(a)):
        if sum(a[i]) != 0:
            if sum(a[i-1]) == 0:
                return False
    return True


def make_canonical(a):
    
    if is_canonical(a):
        return a
    
    nz_indices = []
    z_indices = []
    nzs = []
    zs = []
    for i in range(len(a)):
        if sum(a[i]) != 0:
            nz_indices.append(i)
            nzs.append(a[i])
        else:
            z_indices.append(i)
            zs.append(a[i])
    a_reordered = nzs + zs
    orig_indices = nz_indices + z_indices
    
    a_canon = zero_matrix(len(a_reordered),len(a_reordered))
    for i in range(len(a_reordered)):
        for j in range(len(a_reordered[0])):
            a_canon[i][j] = a_reordered[i][orig_indices[j]]
            
    return a_canon


# https://en.wikipedia.org/wiki/Absorbing_Markov_chain
# fundamental matrix: N = (It - Q)**-1
# the probability of being absorbed 
# in the absorbing state j
# when starting from transient state i
# is the (i,j)-entry of the matrix: B = NR
def solution(m):
    if len(m) == 1:
        return [1,1]
    # making sure matrix is canonical
    m = make_canonical(m)
    # transforming ints to Fractions
    fr_m = fraction_matrix(m)
    # getting It
    n = len(m)
    n_term = n - [sum(i) for i in m].count(0)
    idt = sq_zero_to_id(zero_matrix(n_term, n_term))
    # getting Q
    q = [i[:n_term] for i in fr_m[:n_term]]
    # getting N
    sub = sub_matrix(idt,q)
    n_m = inv_matrix(sub)
    # getting R
    r_m = [i[n_term:] for i in fr_m[:n_term]]
    # getting B
    b_m = mult_matrix(n_m, r_m)
    return (simp_fractions(b_m[0]))
