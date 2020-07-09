#!/usr/bin/python
# -*- coding: utf-8 -*-

import random


def start_game(n):
    A = ([[0] * (n)] * (n))
    return A


def ruch(poz_x, poz_y, wart, A):
    if A[poz_x % 3][poz_y % 3] == 0:
        A[poz_x % 3][poz_y % 3] = wart  # ew zmienić tutaj
    return A


def order(A):
    lst = []
    for i in range(3):
        lstt = []
        for j in range(3):
            lstt.append(A[i][j])
        lst.append(lstt)
    for j in range(3):
        lstt = []
        for i in range(3):
            lstt.append(A[i][j])
        lst.append(lstt)
    lsttt = []
    for i in range(3):
        lsttt.append(A[i][i])
    lst.append(lsttt)
    q = [A[0][2], A[1][1], A[2][0]]
    lst.append(q)
    return lst


def ilew(x, lst):
    s = 0
    for n in lst:
        if n == x:
            s += 1
    return s


def fajen(i, A, mark):
    B = order(A)
    if i >= 0 and i < 3:
        for j in range(3):
            if B[i][j] == 0:
                ruch(j, i, mark, A)
    elif (i >= 3 and i < 6):
        for j in range(3):
            if B[j][i % 3] == 0:
                ruch(j, i, mark, A)
    elif i == 6:
        for j in range(3):
            if B[i][j] == 0:
                ruch(j, j, mark, A)
    elif i == 7:
        for j in range(3):
            if B[i][j] == 0:
                ruch(j, 2 - j, mark, A)


def rd():
    return random.choice([0, 1, 2])


def comp_moves(A, mark):
    Ord = order(A)
    for i in range(len(Ord)):
        if ilew(mark, Ord[i]) == 2:
            fajen(i, A, mark)
            return
    for i in range(len(Ord)):
        if ilew(-mark, Ord[i]) == 2:
            fajen(i, A, mark)
            return
    for i in Ord:
        if ilew(mark, Ord) == 1 and ilew(-mark, Ord) == 0:
            fajen(i, A, mark)
            return
    L = 1
    while L != 0:
        x = rd()
        y = rd()
        L = A[x][y]
    ruch(x, y, mark, A)
    return



