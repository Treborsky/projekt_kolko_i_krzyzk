#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
import os

pygame.init()
pygame.font.init()


def sciezka_do_img(plik):
    return os.path.abspath(os.path.join("./img/", plik))

# okno gry
scr_width = 800
scr_hight = 600
screen = pygame.display.set_mode((scr_width, scr_hight))
win = pygame.image.load(sciezka_do_img('back_tic_tac_toe.png'))

# grafika przycisków
but_main = pygame.image.load(sciezka_do_img('button1to.png'))
but_high = pygame.image.load(sciezka_do_img('button4osz.png'))

# colors
white = (255, 255, 255)


# klasa do tworzenia przycisków
class Button(object):
    def __init__(self, x, y, width, height, text, action=None, num=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color_font = white
        self.text = text
        self.action = action
        self.button_down = False
        self.num = num

    # rysowanie przycisku i podświetlanie
        self.click = pygame.mouse.get_pressed()[0]
        self.mouse = pygame.mouse.get_pos()
        if self.x + self.width > self.mouse[0] > self.x and self.y + self.height > self.mouse[1] > self.y:
            screen.blit(but_high, (self.x, self.y))

        else:
            screen.blit(but_main, (self.x, self.y))

        self.clicked()
        self.message_display()

    # funkcja klikanie
    def clicked(self):
        if self.x + self.width > self.mouse[0] > self.x and self.y + self.height > self.mouse[1] > self.y:
            if self.button_down is False and self.action is not None:
                if self.click:
                    self.button_down = True
                    self.action(self.num)
                if not self.click:
                    self.button_down = False
            elif self.button_down:
                self.button_down = False

    # wyświetlenie tekstu na ekranie
    def message_display(self):
        font = pygame.font.SysFont('comicsans', 25)
        text_surface = font.render(self.text, True, white)
        text_rect = text_surface.get_rect()
        text_rect.center = ((self.x + (self.width / 2)), (self.y + (self.height / 2)))
        screen.blit(text_surface, text_rect)
