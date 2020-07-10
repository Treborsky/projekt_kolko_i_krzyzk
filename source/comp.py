#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Tuple
import random


def computer_move(board, mark_bool: bool)->Tuple[int,int]:
    # def start_game(n):
    #     A = ([[0] * (n)] * (n))
    #     return A

    if mark_bool:
        mark=1
    else:
        mark=-1

    def ruch(poz_x, poz_y, matrix):
        if matrix[poz_x % 3][poz_y % 3] == 0:
            return poz_x%3, poz_y%3

    def order(matrix):
        lst = []
        for i in range(3):
            lstt = []
            for j in range(3):
                lstt.append(matrix[i][j])
            lst.append(lstt)
        for j in range(3):
            lstt = []
            for i in range(3):
                lstt.append(matrix[i][j])
            lst.append(lstt)
        lsttt = []
        for i in range(3):
            lsttt.append(matrix[i][i])
        lst.append(lsttt)
        q = [matrix[0][2], matrix[1][1], matrix[2][0]]
        lst.append(q)
        return lst

    def how_much(x, lst):
        s = 0
        for n in lst:
            if n == x:
                s += 1
        return s

    def fajen(i, A):
        B = order(A)
        if i >= 0 and i < 3:
            for j in range(3):
                if B[i][j] == 0:
                    return ruch(j, i, A)
        elif (i >= 3 and i < 6):
            for j in range(3):
                if B[j][i % 3] == 0:
                    return ruch(j, i, A)
        elif i == 6:
            for j in range(3):
                if B[i][j] == 0:
                    return ruch(j, j, A)
        elif i == 7:
            for j in range(3):
                if B[i][j] == 0:
                    return ruch(j, 2 - j, A)

    def rd():
        return random.choice([0, 1, 2])

    def comp_moves(A):
        Ord = order(A)
        for i in range(len(Ord)):
            if how_much(mark, Ord[i]) == 2:
                return fajen(i, A)

        for i in range(len(Ord)):
            if how_much(-mark, Ord[i]) == 2:
                return fajen(i, A)

        for i in Ord:
            if how_much(mark, Ord) == 1 and how_much(-mark, Ord) == 0:
                return fajen(i, A)

        L = 1
        while L != 0:
            x = rd()
            y = rd()
            L = A[x][y]
        return ruch(x, y, A)

    return comp_moves(board)
