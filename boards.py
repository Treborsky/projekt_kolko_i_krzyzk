#!/usr/bin/python
#-*- coding: utf8 -*-

import numpy


class BoardThreeOnThree:
    # prywatne
    __A: list                 # krotka przechowujaca plansze 3x3
    __winning_figure:list   # krotka przechoujaca informacje o tym czy ktos wygral i kto
    __win_check_starting_positions:tuple        # krotka przechowujaca pozycje do sprawdzania

    def __init__(self):
        self.__A = [[0,0,0],[0,0,0],[0,0,0]]
        self.__winning_figure = [False, 0]
        self.__win_check_starting_positions = ((0,0),(1,0),(2,0))

    def win_check(self):
        self.__winning_figure = self.win_check()
        return self.__winning_figure

    def update_board(self, pos:tuple, value: int):
        self.__A[pos[0]][pos[1]] = value

    def win_check(self):
        rows = numpy.sum(self.__A, axis=1, keepdims=True)
        diagonals = self.sum_of_diagonals

        for x in rows:
            if abs(x)%3 == 0:
                return [True, x/3]

        for x in diagonals:
            if abs(x)%3 == 0:
                return [True, x/3]

    @property
    def sum_of_diagonals(self):
        sums:list = []
        for x in range (0,3):
            sums += [self.__A[x][x], self.__A[x][2-x]]
        return sums
