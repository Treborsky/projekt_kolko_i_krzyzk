#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
import sys
import time
from source import fgraph, buttons, game_end, CheckMate
from source import ghistory as gh

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
hist_win = pygame.image.load(buttons.sciezka_do_img('back_game_history.png'))


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

# grafika wygranej i przegranej
win_end_screen = pygame.image.load("./Plansze/endgame_2.png")
lose_end_screen = pygame.image.load("./Plansze/endgame_1.png")
win_cross = pygame.image.load("./Plansze/cross_wins.png")
win_circle = pygame.image.load("./Plansze/circle_wins.png")
tie = pygame.image.load("./Plansze/tie.png")

# countdown timer
timer_font = pygame.font.SysFont('Consolas', 30)
timer_sec_3 = 5
timer_sec_4 = 15
timer_sec_5 = 20
timer_text_3 = timer_font.render("00:05", True, (255, 255, 255))
timer_text_4 = timer_font.render("00:15", True, (255, 255, 255))
timer_text_5 = timer_font.render("00:20", True, (255, 255, 255))

clock = pygame.time.Clock()
white = (255, 255, 255)
font = pygame.font.Font(None, 30)


def game_intro(void=None):
    intro = True

    def void_action(empty=None):
        pass

    while intro:
        quit_program()

        screen.blit(win, (0, 0))

        button1 = buttons.Button(290, 220, 210, 60, 'Normal', game_menu, 1)
        button2 = buttons.Button(290, 300, 210, 60, 'Play with computer', game_menu, 2)
        button3 = buttons.Button(290, 380, 210, 60, 'Game time', game_menu, 3)
        button4 = buttons.Button(290, 460, 210, 60, 'Game history', game_history, True)
        button5 = buttons.Button(290, 540, 210, 60, 'Exit', void_action)

        intro = not (button1.button_down or button2.button_down or button3.button_down or button5.button_down)

        pygame.display.update()
        clock.tick(100)

    return intro
    pass


def game_menu(g_type: int = None):

    def start(size: int = None):
        return plansza(size, g_type)

    def to_intro(empty=None):
        pass

    run = True

    pygame.time.wait(100)

    while run:
        quit_program()

        screen.blit(win, (0, 0))

        button1 = buttons.Button(290, 220, 210, 60, '3x3', start, 3)
        button2 = buttons.Button(290, 300, 210, 60, '4x4', start, 4)
        button3 = buttons.Button(290, 380, 210, 60, '5x5', start, 5)
        button4 = buttons.Button(290, 460, 210, 60, 'Return', to_intro)

        run = not (button1.button_down or button2.button_down or button3.button_down or button4.button_down)

        pygame.display.update()
        clock.tick(100)

    return game_intro()
    pass


def plansza(size: int = None, g_type: int = None):
    global timer_sec_5, timer_text_3, timer_text_4, timer_sec_3, timer_sec_4, timer_text_5
    game = True

    winner = None
    board = fgraph.Board(size)
    start_time = time.time()

    def reverse_move(nada=None):
        if g_type != 2:
            board.remove_last_figure()
        else:
            board.remove_last_figure()
            board.remove_last_figure()
        pass

    timer = pygame.USEREVENT + 1
    pygame.time.set_timer(timer, 1000)

    while game:

        screen.blit(pygame.transform.scale(grafika_plansza(size), (800, 600)), (0, 0))

        for figure in board.get_elements:
            if figure[0] == 1:
                screen.blit(pygame.transform.scale(circlesource, (87, 87)), figure[1])
            if figure[0] == -1:
                screen.blit(pygame.transform.scale(crosssource, (87, 87)), figure[1])

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:

                pos = pygame.mouse.get_pos()

                if event.button == 1:
                    board.add_figure(pos[0], pos[1])

                    winner = CheckMate.GameCheck(board=board.matrix, size=size).check()

                    if g_type == 2 and winner != 1 and winner != -1:
                        board.computers_move()

                    elif winner == 1:
                        print('wygrały kółka')
                        screen.blit(pygame.transform.scale(win_circle, (800, 600)), (0, 0))
                        pygame.display.update()
                        clock.tick(2)
                        game = False
                    elif winner == -1:
                        print('wygrały krzyżyki')
                        screen.blit(pygame.transform.scale(win_cross, (800, 600)), (0, 0))
                        pygame.display.update()
                        clock.tick(2)
                        game = False
                    elif winner == 0 and len(board.figure_list) == size*size:
                        print('remis')
                        screen.blit(pygame.transform.scale(tie, (800, 600)), (0, 0))
                        pygame.display.update()
                        clock.tick(2)
                        game = False

            if pygame.key.get_pressed()[pygame.K_BACKSPACE]:
                reverse_move()

            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()
            if g_type == 3:
                if event.type == timer:
                    if board.size == 3:
                        if timer_sec_3 > 0:
                            timer_sec_3 -= 1
                            timer_text_3 = timer_font.render("00:%02d" % timer_sec_3, True, (255, 255, 255))
                        elif timer_sec_3 == 0:
                            board.empty_elements_list()
                            timer_sec_3 = 5
                            timer_text_3 = timer_font.render("00:%02d" % timer_sec_3, True, (255, 255, 255))
                            game_intro()
                        else:
                            pygame.time.set_timer(timer, 0)
                    if board.size == 4:
                        if timer_sec_4 > 0:
                            timer_sec_4 -= 1
                            timer_text_4 = timer_font.render("00:%02d" % timer_sec_4, True, (255, 255, 255))
                        elif timer_sec_4 == 0:
                            board.empty_elements_list()
                            timer_sec_4 = 15
                            timer_text_4 = timer_font.render("00:%02d" % timer_sec_4, True, (255, 255, 255))
                            game_intro()
                        else:
                            pygame.time.set_timer(timer, 0)
                    if board.size == 5:
                        if timer_sec_5 > 0:
                            timer_sec_5 -= 1
                            timer_text_5 = timer_font.render("00:%02d" % timer_sec_5, True, (255, 255, 255))
                        elif timer_sec_5 == 0:
                            board.empty_elements_list()
                            timer_sec_5 = 20
                            timer_text_5 = timer_font.render("00:%02d" % timer_sec_5, True, (255, 255, 255))
                            game_intro()
                        else:
                            pygame.time.set_timer(timer, 0)

        if g_type == 3:
            if board.size == 3:
                screen.blit(timer_text_3, (32, 48))
                pygame.display.update()
            if board.size == 4:
                screen.blit(timer_text_4, (32, 48))
                pygame.display.update()
            if board.size == 5:
                screen.blit(timer_text_5, (32, 48))
                pygame.display.update()

        pygame.display.update()
        clock.tick(100)

    board.save_game(g_type, winner)
    board.empty_elements_list()
    pass


def game_history(open_game_hist=False) -> None:
    ghist = open_game_hist
    history = gh.GameHistoryFileManagement()

    def empty_func(empty=None):
        pass

    all_games = history.history_as_numpy_record_array()
    all_games = all_games[-24:]
    raw_text = history.header_string
    text = font.render(raw_text, True, white)

    record_font = pygame.font.Font(None, 28)

    while ghist:
        coords = [20, 20]
        quit_program()

        screen.blit(hist_win, (0, 0))

        # here print in text the records form csv file
        screen.blit(text, coords)
        coords[1] += 20
        for record in all_games:
            gnumber, gsize, gtype, sfig, wfig = record
            raw_record: str = str(gnumber) + '   ' + str(int(gsize)) + '      ' \
                + str(gtype) + '               ' + str(sfig) + '                            ' + str(wfig)
            formatted = record_font.render(raw_record, True, white)
            screen.blit(formatted, coords)
            coords[1] += 20

        button1 = buttons.Button(550, 540, 210, 60, 'Return', empty_func)

        ghist = not button1.button_down

        pygame.display.update()
        clock.tick(20)

    pass


# main loop
def main_loop():
    play = True
    while play:
        play = game_intro()
    sys.exit()
