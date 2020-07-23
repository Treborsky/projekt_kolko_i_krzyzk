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
    def make_df(self) -> pd.DataFrame:
        record_df = pd.DataFrame({"b_size": self.b_size,
                                  "g_type": self.g_type,
                                  "start_fig": self.start_fig,
                                  "win_fig": self.win_fig})
        return record_df

    @staticmethod
    def make_empty_df() -> pd.DataFrame:
        empty_df = pd.DataFrame({"b_size": [0],
                                 "g_type": ['empty'],
                                 "start_fig": ['empty'],
                                 "win_fig": ['empty']})
        return empty_df


class GameHistoryFileManagement:

    def __init__(self, name: str = '../game_history.csv'):
        self.history: pd.DataFrame = self.try_history(name)
        self.create_new_file(name=name, df=self.history)

    @staticmethod
    def create_new_file(name, df: pd.DataFrame):
        df.to_csv(name, index=False)
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

    def add_record(self, new_record: Record = Record()):
        self.history.append(new_record, ignore_index=True)
        pass


h = GameHistoryFileManagement()

h.print_to_console()
