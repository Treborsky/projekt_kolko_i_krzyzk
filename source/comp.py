#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Tuple
import random


<<<<<<< HEAD
def computer_move_3x3(board, mark_bool: bool) -> Tuple[int, int]:
=======
def computer_move(board, mark_bool: bool)->Tuple[int,int]:
>>>>>>> ce1a9873537d6b6f6a31919d12cdc67b1b94e12c
    # def start_game(n):
    #     A = ([[0] * (n)] * (n))
    #     return A

    if mark_bool:
        mark_int = 1
    else:
        mark_int = -1

    def move_mark(poz_x, poz_y, mark, matrix):
        if matrix[poz_x % 3][poz_y % 3] == 0:
<<<<<<< HEAD
            return poz_x, poz_y
=======
            return((poz_x%3, poz_y%3))
>>>>>>> ce1a9873537d6b6f6a31919d12cdc67b1b94e12c

    def order(matrix):
        result_list = []
        for i in range(3):
            support_list = []
            for j in range(3):
                support_list.append(matrix[i][j])
            result_list.append(support_list)
        for j in range(3):
            support_list = []
            for i in range(3):
                support_list.append(matrix[i][j])
            result_list.append(support_list)
        support_list = []
        for i in range(3):
            support_list.append(matrix[i][i])
        result_list.append(support_list)
        support_list = []
        for i in range(3):
            support_list.append(matrix[i][2 - i])
        # q = [matrix[0][2], matrix[1][1], matrix[2][0]]
        result_list.append(support_list)
        return result_list

    def how_much(x, lst):
        s = 0
        for n in lst:
            if n == x:
                s += 1
        return s

    def heart(i, matrix, mark):
        ordered_list = order(matrix)
        if 0 <= i < 3:
            for j in range(3):
<<<<<<< HEAD
                if ordered_list[i][j] == 0:
                    return move_mark(j, i, mark, matrix)
        elif 3 <= i < 6:
            for j in range(3):
                if ordered_list[j][i % 3] == 0:
                    return move_mark(j, i, mark, matrix)
        elif i == 6:
            for j in range(3):
                if ordered_list[i][j] == 0:
                    return move_mark(j, j, mark, matrix)
        elif i == 7:
            for j in range(3):
                if ordered_list[i][j] == 0:
                    return move_mark(j, 2 - j, mark, matrix)
=======
                if B[i][j] == 0:
                    return ruch(j, i, mark, A)
        elif (i >= 3 and i < 6):
            for j in range(3):
                if B[j][i % 3] == 0:
                    return ruch(j, i, mark, A)
        elif i == 6:
            for j in range(3):
                if B[i][j] == 0:
                    return ruch(j, j, mark, A)
        elif i == 7:
            for j in range(3):
                if B[i][j] == 0:
                    return ruch(j, 2 - j, mark, A)
>>>>>>> ce1a9873537d6b6f6a31919d12cdc67b1b94e12c

    def rd():
        return random.choice([0, 1, 2])

<<<<<<< HEAD
    def comp_moves(matrix, mark):
        ordered = order(matrix)
        for i in range(len(ordered)):
            if how_much(mark, ordered[i]) == 2:
                return heart(i, matrix, mark)
        for i in range(len(ordered)):
            if how_much(-mark, ordered[i]) == 2:
                return heart(i, matrix, mark)
        for i in ordered:
            if how_much(mark, ordered) == 1 and how_much(-mark, ordered) == 0:
                return heart(i, matrix, mark)
        v = 1
        while v != 0:
            x = rd()
            y = rd()
            v = matrix[x][y]
        return move_mark(x, y, mark, matrix)

    return comp_moves(board, mark_int)
=======
    def comp_moves(A, mark):
        Ord = order(A)
        for i in range(len(Ord)):
            if how_much(mark, Ord[i]) == 2:
                return fajen(i, A, mark)

        for i in range(len(Ord)):
            if how_much(-mark, Ord[i]) == 2:
                return fajen(i, A, mark)

        for i in Ord:
            if how_much(mark, Ord) == 1 and how_much(-mark, Ord) == 0:
                return fajen(i, A, mark)

        L = 1
        while L != 0:
            x = rd()
            y = rd()
            L = A[x][y]
        ruch(x, y, mark, A)
        return
    return comp_moves(board, mark)
>>>>>>> ce1a9873537d6b6f6a31919d12cdc67b1b94e12c
