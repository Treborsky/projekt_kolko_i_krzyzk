#!/usr/bin/python
# -*- coding: utf-8 -*-


class GameCheck(object):

    def __init__(self, board, size):
        self.player_points = 0
        self.comp_points = 0
        self.nr_of_turn = 1
        self.board = board
        self.size = size

    # sprawdzanie kolumn
    def column(self):
        size = self.size

        if self.size == 5:
            size = self.size - 1
        else:
            size = self.size

        for nr_col in range(size):
            total = 0
            total_2 = 0

            # sumowanie poszczegolnych kolumn
            for nr_row in range(size):
                total = total + self.board[nr_row][nr_col]

            if self.size == 5:
                for nr_row in range(1, self.size):
                    total_2 = total_2 + self.board[nr_row][nr_col]
            else:
                pass

            # sprawdzanie numeru tury
            if self.nr_of_turn % 2 == 1:
                if total == -size or total_2 == -size:
                    #print('wygraly krzyzyki')
                    return True  # funkcja zwraca True gdy wygrywa gracz krzyzyk

                if total == size or total_2 == size:
                    #print('wygrały kółka')
                    return False  # funkcja zwraca False gdy wygrywa kolko( I-tura: komputer)

            else:
                if total == size or total_2 == size:
                    return True

                if total == -size or total_2 == -size:
                    return False

    # sprawdzanie wierszy
    def rows(self):
        size = self.size

        if self.size == 5:
            size = self.size - 1

        for nr_row in range(size):
            total = 0
            total_2 = 0

            # sumowanie poszczegolnych wierszy
            for nr_col in range(size):
                total = total + self.board[nr_row][nr_col]

            if self.size == 5:
                for nr_col in range(1, self.size):
                    total_2 = total_2 + self.board[nr_row][nr_col]

            # sprawdzanie numeru tury
            if self.nr_of_turn % 2 == 1:
                if total == -size or total_2 == -size:
                    return True

                if total == size or total_2 == size:
                    return False

            else:
                if total == size or total_2 == size:
                    return True

                if total == -size or total_2 == -size:
                    return False

    # sprawdzanie skosow
    def slant(self):
        size = self.size

        if self.size == 5:
            size = self.size - 1

        if self.size > 2:
            total_1 = 0
            total_2 = 0

            # sumowanie skosu od lewego gornego rogu do prawego dolnego
            for nr_slant in range(size):
                total_1 = total_1 + self.board[nr_slant][nr_slant]

            # sumowanie skosu od lewego dolnego rogu do prawego gornego
            for nr_row, nr_col in zip(range(size), range(size - 1, -1, -1)):
                total_2 = total_2 + self.board[nr_row][nr_col]

            if self.size == 4 or self.size == 5:

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

            if self.size == 3:

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

        if self.size == 5:
            total_1 = 0
            total_2 = 0
            total_3 = 0
            total_4 = 0
            total_5 = 0
            total_6 = 0

            for nr_slant in range(1, 5):
                total_1 = total_1 + self.board[nr_slant][nr_slant]

            for nr_row, nr_col in zip(range(1, 5), range(4, 0, -1)):
                total_2 = total_2 + self.board[nr_row][nr_col]

            for nr_row, nr_col in zip(range(1, 5), range(3, -1, -1)):
                total_3 = total_3 + self.board[nr_row][nr_col]

            for nr_row, nr_col in zip(range(4), range(4, 0, -1)):
                total_4 = total_4 + self.board[nr_row][nr_col]

            for nr_row, nr_col in zip(range(1, 5), range(4)):
                total_5 = total_5 + self.board[nr_row][nr_col]

            for nr_row, nr_col in zip(range(4), range(1, 5)):
                total_6 = total_6 + self.board[nr_row][nr_col]

            # sprawdzanie numeru tury
            if self.nr_of_turn % 2 == 1:
                if total_1 == -4 or total_2 == -4 or total_3 == -4 or total_4 == -4 or total_5 == -4 or total_6 == -4:
                    return True

                if total_1 == 4 or total_2 == 4 or total_3 == 4 or total_4 == 4 or total_5 == 4 or total_6 == 4:
                    return False

            else:
                if total_1 == 4 or total_2 == 4 or total_3 == 4 or total_4 == 4 or total_5 == 4 or total_6 == 4:
                    return True

                if total_1 == -4 or total_2 == -4 or total_3 == -4 or total_4 == -4 or total_5 == -4 or total_6 == -4:
                    return False

    # sprawdzanie kwadratow
    def square(self):
        number = self.size - 1
        size = self.size

        if self.size == 5:
            size = self.size - 1

        if self.size > 3:
            for nr_row in range(number):
                total_1 = 0
                total_2 = 0
                total_3 = 0
                total_4 = 0

                # sprawdzanie kwadratow z kolumn nr 1 i 2
                for nr_col in range(2):
                    total_1 = total_1 + self.board[nr_row][nr_col] + self.board[nr_row + 1][nr_col]

                # sprawdzanie kwadratow z kolumn nr 2 i 3
                for nr_col in range(1, 3):
                    total_2 = total_2 + self.board[nr_row][nr_col] + self.board[nr_row + 1][nr_col]

                # sprawdzanie kwadratow z kolumn nr 3 i 4
                for nr_col in range(2, 4):
                    total_3 = total_3 + self.board[nr_row][nr_col] + self.board[nr_row + 1][nr_col]

                # sprawdzanie kwadratow z kolumn nr 4 i 5
                if self.size == 5:
                    for nr_col in range(3, 5):
                        total_4 = total_4 + self.board[nr_row][nr_col] + self.board[nr_row + 1][nr_col]

                # sprawdzanie numeru tury
                if self.nr_of_turn % 2 == 1:
                    if total_1 == -size or total_2 == -size or total_3 == -size or total_4 == -size:
                        return True

                    if total_1 == size or total_2 == size or total_3 == size or total_4 == size:
                        return False

                else:
                    if total_1 == size or total_2 == size or total_3 == size or total_4 == size:
                        return True

                    if total_1 == -size or total_2 == -size or total_3 == -size or total_4 == -size:
                        return False
        else:
            return None

    # funkcja sprawdzajaca wszystkie mozliwosci
    def check(self):
        if self.size > 3:
            if GameCheck.rows(self) or GameCheck.column(self) or GameCheck.slant(self) or GameCheck.square(self):
                self.nr_of_turn = self.nr_of_turn + 1
                self.player_points = self.player_points + 1
                #print('wygrały krzyżyki')
                return -1  # wygrywa gracz ( I-tura: krzyzyk)

            elif ((GameCheck.rows(self) is False) or (GameCheck.column(self) is False) or (
                    GameCheck.slant(self) is False) or (GameCheck.square(self) is False)):
                self.nr_of_turn = self.nr_of_turn + 1
                self.comp_points = self.comp_points + 1
                #print('wygrały kółka')
                return 1  # wygrywa komp (I-tura: kolko)

            else:
                self.nr_of_turn = self.nr_of_turn + 1
                #print('remis')
                return 0  # remis
        else:
            if GameCheck.rows(self) or GameCheck.column(self) or GameCheck.slant(self):
                self.nr_of_turn = self.nr_of_turn + 1
                self.player_points = self.player_points + 1
                #print('wygrały krzyżyki')
                return -1  # wygrywa gracz ( I-tura: krzyzyk)

            elif ((GameCheck.rows(self) is False) or (GameCheck.column(self) is False) or (
                    GameCheck.slant(self) is False)):
                self.nr_of_turn = self.nr_of_turn + 1
                self.comp_points = self.comp_points + 1
                #print('wygrały kółka')
                return 1  # wygrywa komp (I-tura: kolko)

            else:
                self.nr_of_turn = self.nr_of_turn + 1
                #print('remis')
                return 0  # remis
