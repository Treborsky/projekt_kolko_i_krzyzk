#!/usr/bin/python
# -*- coding: utf8 -*-

from typing import List, Tuple
from source import comp
from source import ghistory as gh

x3_dimensions__: List[Tuple[int, int]] = [(146, 314), (326, 473), (487, 651)]
y3_dimensions__: List[Tuple[int, int]] = [(107, 234), (245, 354), (365, 493)]

x4_dimensions__: List[Tuple[int, int]] = [(143, 269), (280, 394), (407, 517), (529, 654)]
y4_dimensions__: List[Tuple[int, int]] = [(51, 171), (182, 295), (306, 415), (426, 545)]

x5_dimensions__: List[Tuple[int, int]] = [(124, 225), (236, 331), (342, 438), (450, 546), (557, 659)]
y5_dimensions__: List[Tuple[int, int]] = [(17, 118), (129, 227), (239, 338), (349, 447), (459, 561)]


class Board:    # TODO: exception handling ground-up

    figure_list: List = []

    def __init__(self, n):
        self.state: bool = False
        self.matrix: List[List[int]] = [[0 for x in range(0, n)] for y in range(0, n)]
        self.size: int = n
        self.x_dimensions__: List[Tuple[int, int]] = []
        self.y_dimensions__: List[Tuple[int, int]] = []
        if n == 3:
            self.x_dimensions__: List[Tuple[int, int]] = x3_dimensions__
            self.y_dimensions__: List[Tuple[int, int]] = y3_dimensions__
        elif n == 4:
            self.x_dimensions__: List[Tuple[int, int]] = x4_dimensions__
            self.y_dimensions__: List[Tuple[int, int]] = y4_dimensions__
        elif n == 5:
            self.x_dimensions__: List[Tuple[int, int]] = x5_dimensions__
            self.y_dimensions__: List[Tuple[int, int]] = y5_dimensions__

    @staticmethod
    def game_type_str(s: int) -> str:
        if s == 1:
            return 'norm'
        elif s == 2:
            return 'comp'
        elif s == 3:
            return 'time'

    @staticmethod
    def figure_str(f: int) -> str:
        if f == 1:
            return 'o'
        elif f == -1:
            return 'x'

    def translate_pos(self, x_mouse_position, y_mouse_position) -> Tuple[int, int]:
        # translates the x-y position of the mouse into x,y coordinates on the backend 3x3 matrix
        x = -1
        y = -1
        for i in range(0, self.size):
            if self.x_dimensions__[i][0] < x_mouse_position < self.x_dimensions__[i][1]:
                x = i
            if self.y_dimensions__[i][0] < y_mouse_position < self.y_dimensions__[i][1]:
                y = i
        if x == -1 or y == -1:
            print("nice man")
            return 0, 0
            # raise ValueError("nie zaznaczono pola")
        else:
            return x, y

    def re_translate_pos(self, x, y) -> Tuple[int, int]:
        # returns the top left corner of the proper rectangle to put a figure in
        return self.x_dimensions__[x][0], self.y_dimensions__[y][0]

    def update_elements(self, i, j) -> None:
        # updates the matrix and adds the new figure to the list of figures for display
        if self.matrix[i][j] == 0:
            if self.state is True:
                self.matrix[i][j] = 1
            elif self.state is False:
                self.matrix[i][j] = -1
        #else:
            #raise ValueError("already filled")
        else:
            return
        if len(self.figure_list) <= self.size*self.size:
            self.figure_list += [(self.matrix[i][j], self.re_translate_pos(i, j))]
        #else:
            #raise IndexError("plansza pelna")
        pass

    def add_figure(self, x_mouse_position, y_mouse_position) -> None:
        # updates the state of the matrix and switches form x's to o's and the other way round
        #try:
        xs, ys = self.translate_pos(x_mouse_position, y_mouse_position)
        self.update_elements(xs, ys)
        self.state = not self.state
        #except ValueError as error:
         #   raise ValueError(error)
        pass

    def computers_move(self) -> None:
        raw_move = comp.computer_move(self.matrix, self.state)
        if raw_move is not None:
            self.update_elements(i=raw_move[0], j=raw_move[1])
            self.state = not self.state

    def save_game(self, gtype: int = 1):
        board_size = self.size
        game_type = self.game_type_str(gtype)

        last_position = self.get_last_coordinates
        winning_int = self.matrix[last_position[0]][last_position[1]]
        winning_figure: str = self.figure_str(winning_int)

        first_move = self.figure_list[0][1]
        starting_int = self.matrix[first_move[0]][first_move[1]]
        starting_figure: str = self.figure_str(starting_int)

        return gh.Record(board_size, game_type, starting_figure, winning_figure).make_df()

    @property
    def get_elements(self) -> List:
        # returns the list of elements that ought to be displayed
        return self.figure_list

    @property
    def get_last_coordinates(self) -> Tuple[int, int]:
        # returns the last coordinates the were updated
        last_update = self.figure_list[-1]
        last_graphic_pos = last_update[1]
        coords = self.translate_pos(last_graphic_pos[0], last_graphic_pos[1])
        return coords
