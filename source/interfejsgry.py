#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
import sys
import time
from source import fgraph, buttons, game_end, CheckMate


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
def grafika_plansza(b_size: int):
    if b_size == 3:
        return pygame.image.load("./Plansze/Plansza_3x3_v1.png")
    elif b_size == 4:
        return pygame.image.load("./Plansze/plansza_4x4.png")
    elif b_size == 5:
        return pygame.image.load("./Plansze/plansza_5x5.PNG")


# grafika figur
crosssource = pygame.image.load("Plansze/x_3x3.png")
circlesource = pygame.image.load("Plansze/o_3x3.png")

# nazwa okna gry
pygame.display.set_caption("Tic Tac Toe")

clock = pygame.time.Clock()
white = (255, 255, 255)
font = pygame.font.Font(None, 30)

# ekran główny
def game_intro(void = None):
    intro = True

    while intro:
        quit_program()

        screen.blit(win, (0, 0))

        button1 = buttons.Button(290, 220, 210, 60, '3x3', game_menu, 3)
        button2 = buttons.Button(290, 300, 210, 60, '4x4', game_menu, 4)
        button3 = buttons.Button(290, 380, 210, 60, '5x5', game_menu, 5)
        button4 = buttons.Button(290, 460, 210, 60, 'Exit', sys.exit)

        intro = not (button1.button_down or button2.button_down or button3.button_down or button4.button_down)

        pygame.display.update()
        clock.tick(100)
    pass


def game_menu(size: int = None):

    def start(g_type: int = None):
        plansza(size, g_type)

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


def plansza(size: int = None, g_type: int = None):
    game = True

    board = fgraph.Board(size)
    start_time = time.time()

    while game:

        screen.blit(pygame.transform.scale(grafika_plansza(size), (800, 600)), (0, 0))

        for figure in board.get_elements:
            if figure[0] == 1:
                screen.blit(pygame.transform.scale(circlesource, (87, 87)), figure[1])
            if figure[0] == -1:
                screen.blit(pygame.transform.scale(crosssource, (87, 87)), figure[1])

        # event handling
        for event in pygame.event.get():
            # interfacing with the board
            if event.type == pygame.MOUSEBUTTONDOWN:

                pos = pygame.mouse.get_pos()

                if event.button == 1:
                    board.add_figure(pos[0], pos[1])                                # here adding a new cross/circle

                    if g_type == 2:                                                 # here optional computer move mordo
                        board.computers_move()

                    #winner = game_end.ChekingBoard(board=board.matrix, size=size).check()  # here checking for a win
                    winner = CheckMate.GameCheck(board=board.matrix, size=size).check()

                    if winner == 1:                                                 # TODO: rewrite it's ugly
                        print("wygrały kółka")                                      # TODO: exception handling mordo
                        break
                    elif winner == -1:
                        print("wygrały krzyżyki")
                        break

            if event.type == pygame.QUIT:                                           # here checking for a quit event
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()
        if g_type == 3:
            time_limit = 5

            elapsed_time = time.time() - start_time
            timer = time_limit - int(elapsed_time)
            output_string = "Time left: 0:{0:02}".format(timer)
            text = font.render(output_string, True, white)

            screen.blit(text, [30, 50])
            if elapsed_time > time_limit:
                print("Game over")
                game_menu()

        pygame.display.update()
        clock.tick(100)

    game_menu(size)
    pass


# mian loop
def main_loop():
    game_intro()
    sys.exit()
