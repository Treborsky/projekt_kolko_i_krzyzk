#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List


# konwencja taka, jak wszędzie indziej -1 to krzyżyk 1 to kółko
class ChekingBoard:  # TODO: exception handling

    def __init__(self, board: List[List[int]] = None, size: int = None):
        self.board_ = board
        self.n = size

    # sprawdzanie kolumn
    def cols(self) -> int:
        for x in range(0, self.n):
            winner = 0
            for y in range(0, self.n):
                winner += self.board_[x][y]
            if winner == self.n:
                return 1
            elif winner == -self.n:
                return -1
        return 0

    def rows(self) -> int:
        for y in range(0, self.n):
            winner = 0
            for x in range(0, self.n):
                winner += self.board_[x][y]
            if winner == self.n:
                return 1
            elif winner == -self.n:
                return -1
        return 0

    def slant(self) -> int:
        # lewy górny róg
        winner = 0
        for x in range(0, self.n):
            winner += self.board_[x][x]
        if winner == self.n:
            return 1
        elif winner == -self.n:
            return -1
        # prawy górny róg
        winner = 0
        for x in range(0, self.n):
            winner += self.board_[x][-x-1]
        if winner == self.n:
            return 1
        elif winner == -self.n:
            return -1
        return 0

    def square(self) -> int:
        if self.n > 3:
            a = 0
            b = 0
            c = 1
            d = 1
            for i in range(0, self.n - 1):
                for j in range(0, self.n - 1):
                    winner = self.board_[a+j][b+i] + self.board_[a+j][d+i] + \
                             self.board_[c+j][b+i] + self.board_[c+j][d+i]
                    if winner == 4:
                        return 1
                    elif winner == -4:
                        return -1
                    else:
                        continue
            return 0
        else:
            return 0

    def check(self) -> int:
        cols = self.cols()
        rows = self.rows()
        slants = self.slant()
        squares = self.square()
        if cols != 0:
            return cols
        elif rows != 0:
            return rows
        elif slants != 0:
            return slants
        elif squares != 0:
            return squares
        else:
            return 0
