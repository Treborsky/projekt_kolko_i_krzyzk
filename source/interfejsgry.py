#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
import os
import sys
from source import fgraph, play_4x4, game_statistics, buttons
from typing import Tuple

pygame.init()


def quit_program():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit()

# okno gry
scr_width = 800
scr_hight = 600
screen = pygame.display.set_mode((scr_width, scr_hight))
win = pygame.image.load(buttons.sciezka_do_img('back_tic_tac_toe.png'))


# grafika planszy
def grafika_plansza(n: int):
    if n == 3:
        return pygame.image.load("./Plansze/Plansza_3x3_v1.png")
    elif n == 4:
        return pygame.image.load("./Plansze/plansza_4x4.png")
    elif n == 5:
        return pygame.image.load("./Plansze/plansza_5x5.PNG")

# grafika figur
crosssource = pygame.image.load("Plansze/x_3x3.png")
circlesource = pygame.image.load("Plansze/o_3x3.png")

# nazwa okna gry
pygame.display.set_caption("Tic Tac Toe")

clock = pygame.time.Clock()


# ekran główny
def game_intro(n: None = None):
    intro = True

    while intro:
        quit_program()

        screen.blit(win, (0, 0))

        button1 = buttons.Button(290, 220, 210, 60, '3x3', game_menu, 3)
        button2 = buttons.Button(290, 300, 210, 60, '4x4', game_menu, 4)
        button3 = buttons.Button(290, 380, 210, 60, '5x5', game_menu, 5)

        intro = not (button1.button_down or button2.button_down or button3.button_down)

        pygame.display.update()
        clock.tick(100)
    pass


def game_menu(n: int = None):

    def start(m: int = None):
        plansza(n, m)

    run = True

    pygame.time.wait(100)

    while run:
        quit_program()

        screen.blit(win, (0, 0))

        button1 = buttons.Button(290, 220, 210, 60, 'Normal', start, 1)
        button2 = buttons.Button(290, 300, 210, 60, 'Play with computer', start, 2)
        button3 = buttons.Button(290, 380, 210, 60, 'Game time', start, 3)
        button4 = buttons.Button(290, 460, 210, 60, 'Return', game_intro)

        run = not (button1.button_down or button2.button_down or button3.button_down or button4.button_down)

        pygame.display.update()
        clock.tick(100)
    pass


def plansza(n: int = None, m: int = None):
    game = True

    board = fgraph.Board(n)

    while game:

        screen.blit(pygame.transform.scale(grafika_plansza(n), (800, 600)), (0, 0))

        for figure in board.get_elements:
            if figure[0] == 1:
                screen.blit(pygame.transform.scale(circlesource, (87, 87)), figure[1])
            if figure[0] == -1:
                screen.blit(pygame.transform.scale(crosssource, (87, 87)), figure[1])

        # event handling TODO: <- zamknąć cały ten blok w jakiejś funkcji / klasie-interfejsie
        for event in pygame.event.get():
            # interfacing with the board
            if event.type == pygame.MOUSEBUTTONDOWN:
                try:
                    pos = pygame.mouse.get_pos()
                    if event.button == 1:
                        board.add_figure(pos[0], pos[1])
                except ValueError as error:
                    print(error)  # TODO: <- tutaj należy obsłużyć dany wyjątek
                    continue
                except IndexError as error:
                    print(error)  # TODO: <- tutaj należy obsłużyć dany wyjątek
                    break

            # game exit
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()

            # game end check
            winner = play_4x4.Game4x4(board=board.matrix).check()
            if winner == 1:
                print("wygrały kółka")
                game_menu(n)
            elif winner == -1:
                print("wygrały krzyżyki")
                game_menu(n)

        pygame.display.update()
        clock.tick(100)
    pass


# mian loop
def main_loop():
    game_intro(None)
    sys.exit()
