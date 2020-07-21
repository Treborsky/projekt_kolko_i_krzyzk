#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Tuple
import random
# import numpy as np


def computer_move(board, mark_bool: bool) -> Tuple[int, int]:
    # def start_game(n):
    #     A = ([[0] * (n)] * (n))
    #     return A
    # board_arr = np.array(board)
    # board_transposed = np.transpose(board_arr)

    if mark_bool:
        mark_int = 1
    else:
        mark_int = -1

    def move_mark(poz_x, poz_y, mark, matrix):
        if matrix[poz_x % 3][poz_y % 3] == 0:
            # print(poz_x, poz_y)
            # print(matrix)
            return poz_x % 3, poz_y % 3
        else:
            return random_move(matrix, mark)

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

    def order_new(matrix):
        result_list = []
        for j in range(3):
            support_list = []
            for i in range(3):
                support_list.append(matrix[i][j])
            result_list.append(support_list)
        for i in range(3):
            support_list = []
            for j in range(3):
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
                if ordered_list[i][j] == 0:
                    return move_mark(j, i, mark, matrix)
        elif 3 <= i < 6:
            for j in range(3):
                if ordered_list[j][i % 3] == 0:
                    return move_mark(j, i % 3, mark, matrix)
        elif i == 6:
            for j in range(3):
                if ordered_list[i][j] == 0:
                    return move_mark(j, j, mark, matrix)
        elif i == 7:
            for j in range(3):
                if ordered_list[i][j] == 0:
                    return move_mark(j, 2 - j, mark, matrix)

    def heart_new(i, matrix, mark):
        ordered_list = order(matrix)
        if 1 <= i < 3:
            for j in range(3):
                if ordered_list[j][i % 3] == 0:
                    return move_mark(j, i % 3, mark, matrix)
        elif 3 <= i < 6:
            for j in range(3):
                if ordered_list[i][j] == 0:
                    return move_mark(j, i, mark, matrix)
        elif i == 6:
            for j in range(3):
                if ordered_list[i][j] == 0:
                    return move_mark(j, j, mark, matrix)
        elif i == 7:
            for j in range(3):
                if ordered_list[i][j] == 0:
                    return move_mark(j, 2 - j, mark, matrix)

    def rd():
        return random.choice([0, 1, 2])

    def random_move(matrix, mark):
        result_list = []
        for i in range(3):
            for j in range(3):
                if matrix[i][j] == 0:
                    result_list.append((i, j))
        move_tuple = random.choice(result_list)
        x = move_tuple[0]
        y = move_tuple[1]
        return move_mark(x, y, mark, matrix)

    def comp_moves(matrix, mark):
        ordered_list = order(matrix)
        check_acc = 0
        for i in range(len(ordered_list)):
            if how_much(mark, ordered_list[i]) == 2 and how_much(0, ordered_list[i]) == 1:
                check_acc = 1
                return heart(i, matrix, mark)
        for i in range(len(ordered_list)):
            if how_much(-mark, ordered_list[i]) == 2 and how_much(0, ordered_list[i]) == 1:
                check_acc = 1
                return heart(i, matrix, mark)
        for i in range(len(ordered_list)):
            if how_much(mark, ordered_list[i]) == 1 and how_much(0, ordered_list[i]) == 2:
                check_acc = 1
                return heart(i, matrix, mark)
        if check_acc == 0:
            v = 1
            x = 0
            y = 0
            while v != 0:
                x = rd()
                y = rd()
                v = matrix[x][y]
            return move_mark(x, y, mark, matrix)

    # return comp_moves(board_transposed, mark_int)
    return comp_moves(board, mark_int)
