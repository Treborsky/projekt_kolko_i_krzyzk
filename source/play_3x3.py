#!/usr/bin/python
# -*- coding: utf-8 -*-


class Game3x3(object):

    def __init__(self, board):
        self.player_points = 0
        self.comp_points = 0
        self.nr_of_turn = 1
        self.board = board

    # sprawdzanie kolumn
    def column(self):

        for nr_col in range(3):
            total = 0

            # sumowanie poszczegolnych kolumn
            for nr_row in range(3):
                total = total + self.board[nr_row][nr_col]

            # sprawdzanie numeru tury
            if self.nr_of_turn % 2 == 1:
                if total == -3:
                    return True  # funkcja zwraca True gdy wygrywa gracz krzyzyk

                if total == 3:
                    return False  # funkcja zwraca False gdy wygrywa kolko( I-tura: komputer)

            else:
                if total == 3:
                    return True

                if total == -3:
                    return False

    # sprawdzanie wierszy
    def rows(self):

        for nr_row in range(3):
            total = 0

            # sumowanie poszczegolnych wierszy
            for nr_col in range(3):
                total = total + self.board[nr_row][nr_col]

            # sprawdzanie numeru tury
            if self.nr_of_turn % 2 == 1:
                if total == -3:
                    return True

                if total == 3:
                    return False

            else:
                if total == 3:
                    return True

                if total == -3:
                    return False

    # sprawdzanie skosow
    def slant(self):
        total_1 = 0
        total_2 = 0

        # sumowanie skosu od lewego gornego rogu do prawego dolnego
        for nr_slant in range(3):
            total_1 = total_1 + self.board[nr_slant][nr_slant]

        # sumowanie skosu od lewego dolnego rogu do prawego gornego
        for nr_row, nr_col in zip(range(3), range(2, -1, -1)):
            total_2 = total_2 + self.board[nr_row][nr_col]

        # sprawdzanie numeru tury
        if self.nr_of_turn % 2 == 1:
            if total_1 == -3 or total_2 == -3:
                return True

            if total_1 == 3 or total_2 == 3:
                return False

        else:
            if total_1 == 3 or total_2 == 3:
                return True

            if total_1 == -3 or total_2 == -3:
                return False

    # funkcja sprawdzajaca wszystkie mozliwosci
    def check(self):

        if Game3x3.rows(self) or Game3x3.column(self) or Game3x3.slant(self):
            self.nr_of_turn = self.nr_of_turn + 1
            self.player_points = self.player_points + 1
            return -1   # wygrywa gracz ( I-tura: krzyzyk)

        elif ((Game3x3.rows(self) is False) or (Game3x3.column(self) is False) or (Game3x3.slant(self) is False)):
            self.nr_of_turn = self.nr_of_turn + 1
            self.comp_points = self.comp_points + 1
            return 1    # wygrywa komp (I-tura: kolko)

        else:
            self.nr_of_turn = self.nr_of_turn + 1
            return 0    # remis
