#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd


class Record:

    def __init__(self, board_size: int = 3, game_type: str = 'norm',
                 starting_figure: str = 'x', winning_figure: str = 'x'):
        self.datafr_type = pd.DataFrame({"b_size": [board_size],
                                         "g_type": [game_type],
                                         "start_fig": [starting_figure],
                                         "win_fig": [winning_figure]})
        self.dicttype = {"b_size": board_size,
                         "g_type": game_type,
                         "start_fig": starting_figure,
                         "win_fig": winning_figure}
        self.b_size = board_size
        self.g_type = game_type
        self.start_fig = starting_figure
        self.win_fig = winning_figure

    @staticmethod
    def make_empty_df() -> pd.DataFrame:
        empty_df = pd.DataFrame({"b_size": [],
                                 "g_type": [],
                                 "start_fig": [],
                                 "win_fig": []})
        return empty_df


class GameHistoryFileManagement:

    def __init__(self, name: str = 'game_history.csv'):
        self.history: pd.DataFrame = self.try_history(name)  # czy to wogóle działa?
        self.name = name

    @staticmethod
    def save_to_file(df: pd.DataFrame):
        df.to_csv('game_history.csv', index=False)
        pass

    @staticmethod
    def try_history(name: str) -> pd.DataFrame:
        try:
            return pd.read_csv(name)
        except FileNotFoundError:
            return GameHistoryFileManagement.make_empty_history()

    @staticmethod
    def make_empty_history() -> pd.DataFrame:
        return Record.make_empty_df()

    def print_to_console(self, beg: int = 0, end: int = -1):
        print(self.history.iloc[beg:end])

    def add_record(self, new_record: pd.DataFrame):
        self.history = self.history.append(new_record, ignore_index=True)
        pass
