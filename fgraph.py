#!/usr/bin/python
# -*- coding: utf8 -*-

from typing import List, Tuple


class ThreeBoard:
    matrix: List[List[int]] = [[0 for x in range(0, 3)] for y in range(0, 3)]
    x_dimensions__: List[Tuple[int, int]] = [(146, 314), (326, 473), (487, 651)]
    y_dimensions__: List[Tuple[int, int]] = [(107, 234), (245, 354), (365, 493)]
    figure_list: List = []

    def __init__(self):
        self.state: bool = False

    def translate_pos(self, x_mouse_position, y_mouse_position) -> Tuple[int, int]:
        # translates the x-y position of the mouse into x,y coordinates on the backend 3x3 matrix
        x = -1
        y = -1
        for i in range(0, 3):
            if self.x_dimensions__[i][0] < x_mouse_position < self.x_dimensions__[i][1]:
                x = i
            if self.y_dimensions__[i][0] < y_mouse_position < self.y_dimensions__[i][1]:
                y = i
        if x == -1 or y == -1:
            raise ValueError("nie zaznaczono pola")
        else:
            return x, y

    def re_translate_pos(self, x, y) -> Tuple[int, int]:
        # returns the top left corner of the proper rectangle to put a figure in
        return self.x_dimensions__[x][0], self.y_dimensions__[y][0]

    def add_figure(self, x_mouse_position, y_mouse_position) -> None:
        # updates the state of the matrix and switches form x's to o's and the other way round
        try:
            xs, ys = self.translate_pos(x_mouse_position, y_mouse_position)
            self.update_elements(xs, ys)
            self.state = not self.state
        except ValueError as error:
            raise ValueError(error)
        pass

    def update_elements(self, i, j) -> None:
        # updates the matrix and adds the new figure to the list of figures for display
        if self.matrix[i][j] == 0:
            if self.state is True:
                self.matrix[i][j] = 1
            elif self.state is False:
                self.matrix[i][j] = -1
        else:
            raise ValueError("already filled")

        if len(self.figure_list) <= 9:
            self.figure_list += [(self.matrix[i][j], self.re_translate_pos(i, j))]
        else:
            raise IndexError("plansza pelna")
        pass

    @property
    def get_elements(self) -> List:
        # returns the list of elements that ought to be displayed
        return self.figure_list


class FourBoard:
    matrix: List[List[int]] = [[0 for x in range(0, 4)] for y in range(0, 4)]
    x_dimensions__: List[Tuple[int, int]] = [(143, 269), (280, 394), (407, 517), (529, 654)]
    y_dimensions__: List[Tuple[int, int]] = [(51, 171), (182, 295), (306, 415), (426, 545)]
    figure_list: List = []

    def __init__(self):
        self.state: bool = False

    def translate_pos(self, x_mouse_position, y_mouse_position) -> Tuple[int, int]:
        # translates the x-y position of the mouse into x,y coordinates on the backend 3x3 matrix
        x = -1
        y = -1
        for i in range(0, 4):
            if self.x_dimensions__[i][0] < x_mouse_position < self.x_dimensions__[i][1]:
                x = i
            if self.y_dimensions__[i][0] < y_mouse_position < self.y_dimensions__[i][1]:
                y = i
        if x == -1 or y == -1:
            raise ValueError("nie zaznaczono pola")
        else:
            return x, y

    def re_translate_pos(self, x, y) -> Tuple[int, int]:
        # returns the top left corner of the proper rectangle to put a figure in
        return self.x_dimensions__[x][0], self.y_dimensions__[y][0]

    def add_figure(self, x_mouse_position, y_mouse_position) -> None:
        # updates the state of the matrix and switches form x's to o's and the other way round
        try:
            xs, ys = self.translate_pos(x_mouse_position, y_mouse_position)
            self.update_elements(xs, ys)
            self.state = not self.state
        except ValueError as error:
            raise ValueError(error)
        pass

    def update_elements(self, i, j) -> None:
        # updates the matrix and adds the new figure to the list of figures for display
        if self.matrix[i][j] == 0:
            if self.state is True:
                self.matrix[i][j] = 1
            elif self.state is False:
                self.matrix[i][j] = -1
        else:
            raise ValueError("already filled")

        if len(self.figure_list) <= 16:
            self.figure_list += [(self.matrix[i][j], self.re_translate_pos(i, j))]
        else:
            raise IndexError("plansza pelna")
        pass

    @property
    def get_elements(self) -> List:
        # returns the list of elements that ought to be displayed
        return self.figure_list


class FiveBoard:
    matrix: List[List[int]] = [[0 for x in range(0, 5)] for y in range(0, 5)]
    x_dimensions__: List[Tuple[int, int]] = [(124, 225), (236, 331), (342, 438), (450, 546), (557, 659)]
    y_dimensions__: List[Tuple[int, int]] = [(17, 118), (129, 227), (239, 338), (349, 447), (459, 561)]
    figure_list: List = []

    def __init__(self):
        self.state: bool = False

    def translate_pos(self, x_mouse_position, y_mouse_position) -> Tuple[int, int]:
        # translates the x-y position of the mouse into x,y coordinates on the backend 3x3 matrix
        x = -1
        y = -1
        for i in range(0, 5):
            if self.x_dimensions__[i][0] < x_mouse_position < self.x_dimensions__[i][1]:
                x = i
            if self.y_dimensions__[i][0] < y_mouse_position < self.y_dimensions__[i][1]:
                y = i
        if x == -1 or y == -1:
            raise ValueError("nie zaznaczono pola")
        else:
            return x, y

    def re_translate_pos(self, x, y) -> Tuple[int, int]:
        # returns the top left corner of the proper rectangle to put a figure in
        return self.x_dimensions__[x][0], self.y_dimensions__[y][0]

    def add_figure(self, x_mouse_position, y_mouse_position) -> None:
        # updates the state of the matrix and switches form x's to o's and the other way round
        try:
            xs, ys = self.translate_pos(x_mouse_position, y_mouse_position)
            self.update_elements(xs, ys)
            self.state = not self.state
        except ValueError as error:
            raise ValueError(error)
        pass

    def update_elements(self, i, j) -> None:
        # updates the matrix and adds the new figure to the list of figures for display
        if self.matrix[i][j] == 0:
            if self.state is True:
                self.matrix[i][j] = 1
            elif self.state is False:
                self.matrix[i][j] = -1
        else:
            raise ValueError("already filled")

        if len(self.figure_list) <= 25:
            self.figure_list += [(self.matrix[i][j], self.re_translate_pos(i, j))]
        else:
            raise IndexError("plansza pelna")
        pass

    @property
    def get_elements(self) -> List:
        # returns the list of elements that ought to be displayed
        return self.figure_list
