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
    def mark_conversion(mark_boolean):
        if mark_boolean:
            mark_int = 1
        else:
            mark_int = -1
        return mark_int

    # def entrance_transformation(matrix):
    #     result_list = []
    #     for i in range(3):
    #         support_list = []
    #         for j in range(3):
    #             support_list.append(matrix[j][i])
    #         result_list.append(support_list)
    #     return result_list
    #
    # def inverse_entrance_transformation(matrix):
    #     result_list = []
    #     for i in range(3):
    #         support_list = []
    #         for j in range(3):
    #             support_list.append(matrix[j][i])
    #         result_list.append(support_list)
    #     return result_list

    def move_marking(poz_x, poz_y, mark, matrix, n):

        if matrix[poz_x % n][poz_y % n] == 0:
            # print(poz_x, poz_y)
            # print(matrix)
            return poz_x % n, poz_y % n
        else:
            # return random_move(inverse_entrance_transformation(matrix), mark)
            return random_move(matrix, mark, n)

    def order(matrix):
        n = len(matrix)
        result_list = []

        for i in range(n):
            support_list = []
            for j in range(n):
                support_list.append(matrix[i][j])
            result_list.append(support_list)

        for j in range(n):
            support_list = []
            for i in range(n):
                support_list.append(matrix[i][j])
            result_list.append(support_list)

        support_list = []
        for i in range(n):
            support_list.append(matrix[i][i])
        result_list.append(support_list)

        support_list = []
        for i in range(n):
            support_list.append(matrix[i][n - 1 - i])
        # q = [matrix[0][2], matrix[1][1], matrix[2][0]]
        result_list.append(support_list)

        if n == 4:
            for i in range(3):
                for j in range(3):
                    support_list = [matrix[i][j], matrix[i][j + 1], matrix[i + 1][j], matrix[i + 1][j + 1]]
                    result_list.append(support_list)

        if n == 5:
            support_list = []
            for i in range(4):
                support_list.append(matrix[i + 1][i])
            result_list.append(support_list)

            support_list = []
            for i in range(4):
                support_list.append(matrix[i][i + 1])
            result_list.append(support_list)

            support_list = []
            for i in range(4):
                support_list.append(matrix[i][3-i])
            result_list.append(support_list)

            support_list = []
            for i in range(4):
                support_list.append(matrix[i + 1][4 - i])
            result_list.append(support_list)

        return result_list

    # def order_new(matrix):
    #     result_list = []
    #     for j in range(3):
    #         support_list = []
    #         for i in range(3):
    #             support_list.append(matrix[i][j])
    #         result_list.append(support_list)
    #     for i in range(3):
    #         support_list = []
    #         for j in range(3):
    #             support_list.append(matrix[i][j])
    #         result_list.append(support_list)
    #     support_list = []
    #     for i in range(3):
    #         support_list.append(matrix[i][i])
    #     result_list.append(support_list)
    #     support_list = []
    #     for i in range(3):
    #         support_list.append(matrix[i][2 - i])
    #     # q = [matrix[0][2], matrix[1][1], matrix[2][0]]
    #     result_list.append(support_list)
    #     return result_list

    def how_much(x, lst):
        s = 0
        for n in lst:
            if n == x:
                s += 1
        return s

    def heart_3x3(i, matrix, mark):
        ordered_list = order(matrix)
        if 0 <= i < 3:
            for j in range(3):
                if ordered_list[i][j] == 0:
                    return move_marking(i, j, mark, matrix, 3)
        elif 3 <= i < 6:
            for j in range(3):
                if ordered_list[j][i % 3] == 0:
                    return move_marking(j, i % 3, mark, matrix, 3)
        elif i == 6:
            for j in range(3):
                if ordered_list[i][j] == 0:
                    return move_marking(j, j, mark, matrix, 3)
        elif i == 7:
            for j in range(3):
                if ordered_list[i][j] == 0:
                    return move_marking(j, 2 - j, mark, matrix, 3)

    def heart_4x4(i, matrix, mark):
        ordered_list = order(matrix)
        if 0 <= i < 4:
            for j in range(4):
                if ordered_list[i][j] == 0:
                    return move_marking(i, j, mark, matrix, 4)
        elif 4 <= i < 8:
            for j in range(4):
                if ordered_list[j][i % 4] == 0:
                    return move_marking(j, i % 4, mark, matrix, 4)
        elif i == 8:
            for j in range(4):
                if ordered_list[i][j] == 0:
                    return move_marking(j, j, mark, matrix, 4)
        elif i == 9:
            for j in range(4):
                if ordered_list[i][j] == 0:
                    return move_marking(j, 3 - j, mark, matrix, 4)
        elif 9 < i <= 18:
            for j in range(4):
                if ordered_list[i][j] == 0:
                    return move_marking((i-10) // 3 + j//2, (i-10) % 3 + j % 2, mark, matrix, 4)

    # def in_a_row_move(i, line, matrix, mark):
    #     for j in range(5):
    #         if line[j] == -1:
    #             if line[j - 1] == 0:
    #                 return move_marking(i, j, mark, matrix, 5)
    tricky_five_list = [2, 1, 3, 0, 4]

    def heart_5x5(i, matrix, mark):
        ordered_list = order(matrix)
        if 0 <= i < 5:
            for j in tricky_five_list:
                if ordered_list[i][j] == 0:
                    return move_marking(i, j, mark, matrix, 5)
        elif 5 <= i < 10:
            for j in tricky_five_list:
                if ordered_list[j][i % 5] == 0:
                    return move_marking(j, i % 5, mark, matrix, 5)
        elif i == 10:
            for j in tricky_five_list:
                if ordered_list[i][j] == 0:
                    return move_marking(j, j, mark, matrix, 5)
        elif i == 11:
            for j in tricky_five_list:
                if ordered_list[i][j] == 0:
                    return move_marking(j, 4 - j, mark, matrix, 5)
        elif i == 12:
            for j in range(4):
                if ordered_list[i][j] == 0:
                    return move_marking(j + 1, j, mark, matrix, 5)
        elif i == 13:
            for j in range(4):
                if ordered_list[i][j] == 0:
                    return move_marking(j, j + 1, mark, matrix, 5)
        elif i == 14:
            for j in range(4):
                if ordered_list[i][j] == 0:
                    return move_marking(j, 3 - j, mark, matrix, 5)
        elif i == 15:
            for j in range(4):
                if ordered_list[i][j] == 0:
                    return move_marking(j + 1, 4 - j, mark, matrix, 5)

    # def heart_new(i, matrix, mark):
    #     ordered_list = order(matrix)
    #     if 1 <= i < 3:
    #         for j in range(3):
    #             if ordered_list[j][i % 3] == 0:
    #                 return move_marking(j, i % 3, mark, matrix)
    #     elif 3 <= i < 6:
    #         for j in range(3):
    #             if ordered_list[i][j] == 0:
    #                 return move_marking(j, i, mark, matrix)
    #     elif i == 6:
    #         for j in range(3):
    #             if ordered_list[i][j] == 0:
    #                 return move_marking(j, j, mark, matrix)
    #     elif i == 7:
    #         for j in range(3):
    #             if ordered_list[i][j] == 0:
    #                 return move_marking(j, 2 - j, mark, matrix)

    # def rd():
    #     return random.choice([0, 1, 2])
    def random_move(matrix, mark, n):
        result_list = []
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 0:
                    result_list.append((i, j))
        if result_list is None:
            return
        else:
            move_tuple = random.choice(result_list)
            x = move_tuple[0]
            y = move_tuple[1]
            return move_marking(x, y, mark, matrix, n)

    def comp_move_3x3(matrix, mark):
        ordered_list = order(matrix)
        print(ordered_list)
        for i in range(len(ordered_list)):
            if how_much(mark, ordered_list[i]) == 2 and how_much(0, ordered_list[i]) == 1:
                return heart_3x3(i, matrix, mark)
        for i in range(len(ordered_list)):
            if how_much(-mark, ordered_list[i]) == 2 and how_much(0, ordered_list[i]) == 1:
                return heart_3x3(i, matrix, mark)
        for i in range(len(ordered_list)):
            if how_much(mark, ordered_list[i]) == 1 and how_much(0, ordered_list[i]) == 2:
                return heart_3x3(i, matrix, mark)
        return random_move(matrix, mark, 3)

    def comp_move_4x4(matrix, mark):
        ordered_list = order(matrix)
        print(ordered_list)
        for i in range(len(ordered_list)):
            if how_much(mark, ordered_list[i]) == 3 and how_much(0, ordered_list[i]) == 1:
                return heart_4x4(i, matrix, mark)
        for i in range(len(ordered_list)):
            if how_much(-mark, ordered_list[i]) == 3 and how_much(0, ordered_list[i]) == 1:
                return heart_4x4(i, matrix, mark)
        for i in range(len(ordered_list)):
            if how_much(-mark, ordered_list[i]) == 2 and how_much(0, ordered_list[i]) == 2:
                return heart_4x4(i, matrix, mark)
        for i in range(len(ordered_list)):
            if how_much(mark, ordered_list[i]) == 2 and how_much(0, ordered_list[i]) == 2:
                return heart_4x4(i, matrix, mark)
        for i in range(len(ordered_list)):
            if how_much(mark, ordered_list[i]) == 1 and how_much(0, ordered_list[i]) == 3:
                return heart_4x4(i, matrix, mark)
        for i in range(len(ordered_list)):
            if how_much(-mark, ordered_list[i]) == 1 and how_much(0, ordered_list[i]) == 3:
                return heart_4x4(i, matrix, mark)
        return random_move(matrix, mark, 4)

    def free_row(mark, ordered_list) -> bool:
        if len(ordered_list) == 5:
            for i in (1, 2, 3):
                if ordered_list[i] == mark:
                    return False
        return True

    def comp_move_5x5(matrix, mark):
        ordered_list = order(matrix)
        print(ordered_list)

        for i in range(len(ordered_list)):
            if how_much(mark, ordered_list[i]) == 3 and how_much(0, ordered_list[i]) > 0 and free_row(-mark,
                                                                                                      ordered_list[i]):
                return heart_5x5(i, matrix, mark)
        for i in range(len(ordered_list)):
            if how_much(-mark, ordered_list[i]) == 3 and how_much(0, ordered_list[i]) > 0 and free_row(mark,
                                                                                                       ordered_list[i]):
                return heart_5x5(i, matrix, mark)
        for i in range(len(ordered_list)):
            if how_much(-mark, ordered_list[i]) == 2 and how_much(0, ordered_list[i]) > 1 and free_row(mark,
                                                                                                       ordered_list[i]):
                return heart_5x5(i, matrix, mark)
        for i in range(len(ordered_list)):
            if how_much(mark, ordered_list[i]) == 2 and how_much(0, ordered_list[i]) > 1 and free_row(-mark,
                                                                                                      ordered_list[i]):
                return heart_5x5(i, matrix, mark)
        for i in range(len(ordered_list)):
            if how_much(mark, ordered_list[i]) == 1 and how_much(0, ordered_list[i]) > 2 and free_row(-mark,
                                                                                                      ordered_list[i]):
                return heart_5x5(i, matrix, mark)
        for i in range(len(ordered_list)):
            if how_much(-mark, ordered_list[i]) == 1 and how_much(0, ordered_list[i]) > 2 and free_row(-mark,
                                                                                                       ordered_list[i]):
                return heart_5x5(i, matrix, mark)
        return random_move(matrix, mark, 5)
        pass

    def very_decision(matrix, mark):
        size = len(matrix)
        mark_int = mark_conversion(mark)
        if size == 3:
            return comp_move_3x3(matrix, mark_int)
        elif size == 4:
            return comp_move_4x4(matrix, mark_int)
        elif size == 5:
            return comp_move_5x5(matrix, mark_int)

    # return comp_move_3x3(entrance_transformation(board), mark_int)

    return very_decision(board, mark_bool)
