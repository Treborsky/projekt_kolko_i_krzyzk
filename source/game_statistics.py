#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import List, Tuple


class Move:

    def __init__(self, x: int, y: int, player: bool):
        self.x_pos: int = x
        self.y_pos: int = y
        self.player: str = self.figure(player)

    @staticmethod
    def figure(val: bool) -> str:
        if val:
            return 'circle'
        else:
            return 'cross'

    def str(self):
        return '(' + str(self.x_pos) + ', ' + str(self.y_pos) + ')' + ', ' + self.player


class GameMode:

    def __init__(self, mode: int):
        self.mode: int = mode

    def str_game_mode(self):
        if self.mode == 1:
            return 'Normal'
        elif self.mode == 2:
            return 'Against the computer'
        elif self.mode == 3:
            return 'Timer'
        else:
            raise ValueError


class SingleGameScore:
    game_number: int = 1

    def __init__(self, size: int = None,  winner: bool = None, gamemode: GameMode = None):
        self.moves: List[Move] = []

        if gamemode is not None:
            self.game_mode: str = gamemode.str_game_mode()
        else:
            raise TypeError

        if size is not None:
            self.board_size: str = str(size)

        if winner is not None:
            self.winner: str = str(winner)

    def add_a_move(self, move: Move) -> None:
        self.moves += [move]

    def get_last_move(self) -> Move:
        return self.moves[-1]

    def str_all_moves(self) -> str:
        out_str = ''
        for move in self.moves:
            out_str += move.str()
        return out_str

    def print_single_game(self):
        out_str = 'Gra nr: '
        out_str += self.game_mode
        out_str += self.board_size + 'x' + self.board_size
        out_str += self.str_all_moves()
        return out_str
        pass


class GameHistory:
    game_history: List[SingleGameScore] = []

    def add_to_game_history(self, game: SingleGameScore = None) -> None:
        if game is not None:
            self.game_history += [game]
        else:
            raise TypeError
        pass

    def print_game_history(self) -> None:
        for game in self.game_history:
            game.print_single_game()
        pass
