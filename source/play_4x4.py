#!/usr/bin/python
# -*- coding: utf-8 -*-


class Game4x4(object):

    def __init__(self, board):
        self.player_points = 0
        self.comp_points = 0
        self.nr_of_turn = 1
        self.board = board

    # sprawdzanie kolumn
    def column(self):

        for nr_col in range(4):
            total = 0

            # sumowanie poszczegolnych kolumn
            for nr_row in range(4):
                total = total + self.board[nr_row][nr_col]

            # sprawdzanie numeru tury
            if self.nr_of_turn % 2 == 1:
                if total == -4:
                    return True  # funkcja zwraca True gdy wygrywa gracz krzyzyk

                if total == 4:
                    return False  # funkcja zwraca False gdy wygrywa kolko( I-tura: komputer)

            else:
                if total == 4:
                    return True

                if total == -4:
                    return False

    # sprawdzanie wierszy
    def rows(self):

        for nr_row in range(4):
            total = 0

            # sumowanie poszczegolnych wierszy
            for nr_col in range(4):
                total = total + self.board[nr_row][nr_col]

            # sprawdzanie numeru tury
            if self.nr_of_turn % 2 == 1:
                if total == -4:
                    return True

                if total == 4:
                    return False

            else:
                if total == 4:
                    return True

                if total == -4:
                    return False

    # sprawdzanie skosow
    def slant(self):
        total_1 = 0
        total_2 = 0

        # sumowanie skosu od lewego gornego rogu do prawego dolnego
        for nr_slant in range(4):
            total_1 = total_1 + self.board[nr_slant][nr_slant]

        # sumowanie skosu od lewego dolnego rogu do prawego gornego
        for nr_row, nr_col in zip(range(4), range(3, -1, -1)):
            total_2 = total_2 + self.board[nr_row][nr_col]

        # sprawdzanie numeru tury
        if self.nr_of_turn % 2 == 1:
            if total_1 == -4 or total_2 == -4:
                return True

            if total_1 == 4 or total_2 == 4:
                return False

        else:
            if total_1 == 4 or total_2 == 4:
                return True

            if total_1 == -4 or total_2 == -4:
                return False

    # sprawdzanie kwadratow
    def square(self):

        for nr_row in range(3):
            total_1 = 0
            total_2 = 0
            total_3 = 0

            # sprawdzanie kwadratow z kolumn nr 1 i 2
            for nr_col in range(2):
                total_1 = total_1 + self.board[nr_row][nr_col] + self.board[nr_row + 1][nr_col]

            # sprawdzanie kwadratow z kolumn nr 2 i 3
            for nr_col in range(1, 3):
                total_2 = total_2 + self.board[nr_row][nr_col] + self.board[nr_row + 1][nr_col]

            # sprawdzanie kwadratow z kolumn nr 3 i 4
            for nr_col in range(2, 4):
                total_3 = total_3 + self.board[nr_row][nr_col] + self.board[nr_row + 1][nr_col]

            # sprawdzanie numeru tury
            if self.nr_of_turn % 2 == 1:
                if total_1 == -4 or total_2 == -4 or total_3 == -4:
                    return True

                if total_1 == 4 or total_2 == 4 or total_3 == 4:
                    return False

            else:
                if total_1 == 4 or total_2 == 4 or total_3 == 4:
                    return True

                if total_1 == -4 or total_2 == -4 or total_3 == -4:
                    return False

    # funkcja sprawdzajaca wszystkie mozliwosci
    def check(self):

        if Game4x4.rows(self) or Game4x4.column(self) or Game4x4.slant(self) or Game4x4.square(self):
            self.nr_of_turn = self.nr_of_turn + 1
            self.player_points = self.player_points + 1
            return -1   # wygrywa gracz ( I-tura: krzyzyk)

        elif ((Game4x4.rows(self) is False) or (Game4x4.column(self) is False) or (Game4x4.slant(self) is False) or (Game4x4.square(self) is False)):
            self.nr_of_turn = self.nr_of_turn + 1
            self.comp_points = self.comp_points + 1
            return 1    # wygrywa komp (I-tura: kolko)

        else:
            self.nr_of_turn = self.nr_of_turn + 1
            return 0    # remis
