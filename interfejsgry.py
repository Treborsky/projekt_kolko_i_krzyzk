#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
import os
import sys

pygame.init()
pygame.font.init()

def sciezkaDoImg(plik):
    return os.path.abspath(os.path.join("./img/", plik))

def quit_program():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit()

#okno gry
scr_width = 800
scr_hight = 600
screen = pygame.display.set_mode((scr_width, scr_hight))
win = pygame.image.load(sciezkaDoImg('back_tic_tac_toe.png'))

#grafika przycisków
but_main = pygame.image.load(sciezkaDoImg('button1to.png'))
but_high = pygame.image.load(sciezkaDoImg('button4osz.png'))
#grafika planszy
grafika_plansza_3x3 = pygame.image.load("./Plansze/Plansza_3x3_v1.png")
grafika_plansza_4x4 = pygame.image.load("./Plansze/plansza_4x4.png")

#nazwa okna gry
pygame.display.set_caption("Tic Tac Toe")

#colors
white = (255, 255, 255)

clock = pygame.time.Clock()


#klasa do tworzenia przycisków
class Button(object):
    def __init__(self, x, y, width, height, text, action=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color_font = white
        self.text = text
        self.action = action
        self.button_down = False

    #rysowanie przycisku i podświetlanie
        self.click = pygame.mouse.get_pressed()
        self.mouse = pygame.mouse.get_pos()
        if self.x + self.width > self.mouse[0] > self.x and self.y + self.height > self.mouse[1] > self.y:
            screen.blit(but_high, (self.x, self.y))
        else:
            screen.blit(but_main, (self.x, self.y))

        self.clicked()
        self.message_display(screen)

    #funkcja klikanie
    def clicked(self):

        if self.x + self.width > self.mouse[0] > self.x and self.y + self.height > self.mouse[1] > self.y:
            if self.button_down == False and self.action is not None:
                if self.click[0] == 1:
                    self.button_down = True
                    self.action()
                if self.click[0] == 0:
                    self.button_down = False
            elif self.button_down:
                self.button_down = False


    #wyświetlenie testu na ekranie
    def message_display(self, screen):
        font = pygame.font.SysFont('comicsans', 25)
        text_surface = font.render(self.text, True, white)
        text_rect = text_surface.get_rect()
        text_rect.center = ((self.x + (self.width / 2)), (self.y + (self.height / 2)))
        screen.blit(text_surface, text_rect)

#ekran główny
def game_intro():
    intro = True

    while intro:
        quit_program()

        screen.blit(win, (0, 0))

        button1 = Button(290, 220, 210, 60, '3x3', game_menu_3x3)
        button2 = Button(290, 300, 210, 60, '4x4', game_menu_4x4)
        button3 = Button(290, 380, 210, 60, '5x5', game_menu_5x5)


        pygame.display.update()
        clock.tick(20)

def game_menu_3x3():
    run = True

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if 290 + 210 > pos[0] > 290 and 220 + 60 > pos[1] > 60:
                    plansza_3()

        screen.blit(win, (0, 0))
        button1 = Button(290, 220, 210, 60, 'Normal')
        button2 = Button(290, 300, 210, 60, 'Play with computer', plansza_3)
        button3 = Button(290, 380, 210, 60, 'Game time', plansza_3)
        button4 = Button(290, 460, 210, 60, 'Return', game_intro)

        pygame.display.update()
        clock.tick(20)

def game_menu_4x4():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if 290 + 210 > pos[0] > 290 and 300 + 60 > pos[1] > 60:
                    plansza_4()

        screen.blit(win, (0, 0))
        button1 = Button(290, 220, 210, 60, 'Normal', plansza_4)
        button2 = Button(290, 300, 210, 60, 'Play with computer')
        button3 = Button(290, 380, 210, 60, 'Game time', plansza_4)
        button4 = Button(290, 460, 210, 60, 'Return', game_intro)

        pygame.display.update()
        clock.tick(20)

def game_menu_5x5():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if 290 + 210 > pos[0] > 290 and 380 + 60 > pos[1] > 60:
                    plansza_5()

        screen.blit(win, (0, 0))
        button1 = Button(290, 220, 210, 60, 'Normal', None)
        button2 = Button(290, 300, 210, 60, 'Play with computer', None)
        button3 = Button(290, 380, 210, 60, 'Game time')
        button4 = Button(290, 460, 210, 60, 'Return', game_intro)

        pygame.display.update()
        clock.tick(20)

def plansza_3():
    game = True

    while game:
        quit_program()

        screen.blit(pygame.transform.scale(grafika_plansza_3x3, (800, 600)), (0, 0))

        pygame.display.update()
        clock.tick(20)
def plansza_4():
    game = True

    while game:
        quit_program()

        screen.blit(pygame.transform.scale(grafika_plansza_4x4, (800, 600)), (0, 0))

        pygame.display.update()
        clock.tick(20)

def plansza_5():
    game = True

    while game:
        quit_program()

        screen.blit(win, (0,0))

        pygame.display.update()
        clock.tick(20)


#mian loop
game_intro()
game_menu_3x3()
game_menu_4x4()
game_menu_5x5()
plansza_3()
sys.exit()
