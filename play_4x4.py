#board = [[0, 0, 0, 0],
#         [0, 0, 0, 0],
#         [0, 0, 0, 0],
#         [0, 0, 0, 0]]


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

            for nr_row in range(4):
                total = total + self.board[nr_row][nr_col]

            if self.nr_of_turn % 2 == 1:
                if total == 4:
                    self.player_points = self.player_points + 1
                    self.nr_of_turn = self.nr_of_turn + 1
                    quit()

                if total == -4:
                    self.comp_points = self.comp_points + 1
                    self.nr_of_turn = self.nr_of_turn + 1
                    quit()
            else:
                if total == -4:
                    self.player_points = self.player_points + 1
                    self.nr_of_turn = self.nr_of_turn + 1
                    quit()

                if total == 4:
                    self.comp_points = self.comp_points + 1
                    self.nr_of_turn = self.nr_of_turn + 1
                    quit()

    # sprawdzanie wierszy
    def rows(self):

        for nr_row in range(4):
            total = 0

            for nr_col in range(4):
                total = total + self.board[nr_row][nr_col]

            if self.nr_of_turn % 2 == 1:
                if total == 4:
                    self.player_points = self.player_points + 1
                    self.nr_of_turn = self.nr_of_turn + 1
                    quit()

                if total == -4:
                    self.comp_points = self.comp_points + 1
                    self.nr_of_turn = self.nr_of_turn + 1
                    quit()
            else:
                if total == -4:
                    self.player_points = self.player_points + 1
                    self.nr_of_turn = self.nr_of_turn + 1
                    quit()

                if total == 4:
                    self.comp_points = self.comp_points + 1
                    self.nr_of_turn = self.nr_of_turn + 1
                    quit()

    # sprawdzanie skosow
    def slant(self):
        total_1 = 0
        total_2 = 0

        for nr_slant in range(4):
            total_1 = total_1 + self.board[nr_slant][nr_slant]

        for nr_row, nr_col in zip(range(4), range(3, -1, -1)):
            total_2 = total_2 + self.board[nr_row][nr_col]

        if self.nr_of_turn % 2 == 1:
            if total_1 == 4 or total_2 == 4:
                self.player_points = self.player_points + 1
                self.nr_of_turn = self.nr_of_turn + 1
                quit()

            if total_1 == -4 or total_2 == -4:
                self.comp_points = self.comp_points + 1
                self.nr_of_turn = self.nr_of_turn + 1
                quit()
        else:
            if total_1 == -4 or total_2 == -4:
                self.player_points = self.player_points + 1
                self.nr_of_turn = self.nr_of_turn + 1
                quit()

            if total_1 == 4 or total_2 == 4:
                self.comp_points = self.comp_points + 1
                self.nr_of_turn = self.nr_of_turn + 1
                quit()

    # sprawdzanie kwadratow
    def square(self):

        for nr_row in range(3):
            total_1 = 0
            total_2 = 0
            total_3 = 0

            for nr_col in range(2):
                total_1 = total_1 + self.board[nr_row][nr_col] + self.board[nr_row + 1][nr_col]

            for nr_col in range(1, 3):
                total_2 = total_2 + self.board[nr_row][nr_col] + self.board[nr_row + 1][nr_col]

            for nr_col in range(2, 4):
                total_3 = total_3 + self.board[nr_row][nr_col] + self.board[nr_row + 1][nr_col]

            if self.nr_of_turn % 2 == 1:
                if total_1 == 4 or total_2 == 4 or total_3 == 4:
                    self.player_points = self.player_points + 1
                    self.nr_of_turn = self.nr_of_turn + 1
                    quit()

                if total_1 == -4 or total_2 == -4 or total_3 == -4:
                    self.comp_points = self.comp_points + 1
                    self.nr_of_turn = self.nr_of_turn + 1
                    quit()
            else:
                if total_1 == -4 or total_2 == -4 or total_3 == -4:
                    self.player_points = self.player_points + 1
                    self.nr_of_turn = self.nr_of_turn + 1
                    quit()

                if total_1 == 4 or total_2 == 4 or total_3 == 4:
                    self.comp_points = self.comp_points + 1
                    self.nr_of_turn = self.nr_of_turn + 1
                    quit()

    # funkcja sprawdzajaca wszystkie mozliwosci
    def check(self):
        Game4x4.rows(self)
        Game4x4.column(self)
        Game4x4.slant(self)
        Game4x4.square(self)
