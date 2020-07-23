#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd


class Record:

    def __init__(self, board_size: int = 3, game_type: str = 'norm',
                 starting_figure: str = 'x', winning_figure: str = 'x'):
        self.b_size = board_size
        self.g_type = game_type
        self.start_fig = starting_figure
        self.win_fig = winning_figure

    @property
    def make_df(self):
        record_df = pd.DataFrame({"b_size": self.b_size,
                                  "g_type": self.g_type,
                                  "start_fig": self.start_fig,
                                  "win_fig": self.win_fig})
        return record_df


class GameHistoryFileManagement:

    def __init__(self):
        self.history = pd.read_csv("../game_history.csv")

    def print_to_console(self, beg: int = 0, end: int = -1):
        print(self.history.iloc[beg:end])

    def add_record(self, new_record: Record = Record()):
        self.history.append(new_record, ignore_index=True)
        pass
