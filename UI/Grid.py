import pygame
import pygwidgets
from pygame.locals import *
from UI.Wordle_constants import*

class Grid():

    def __init__(self, window):
        self.window = window
        self.grid_dic = {}

        for i in range(6):
            for j in range(5):
                self.grid_dic[str(i)+str(j)] = pygwidgets.DisplayText(window, loc=(115 + j*(85), 100+i*(85)), value='', fontSize=45, width=79, height=79, textColor=BLACK, backgroundColor=None, justified='center', nickname=None)

    def setText(self,row, column, newChar):
        self.grid_dic[str(row)+str(column)].setValue('\n'+ newChar)
    
    def update(self, i, word, inWord, inLoc):
        for j in range(5):
            if inLoc[j]:
                color = GREEN
            elif inWord[j]:
                color = ORANGE
            else:
                color = DARK_GRAY
            self.grid_dic[str(i)+str(j)] = pygwidgets.DisplayText(self.window, loc=(115 + j*(85), 100+i*(85)), value='\n' + word[j], fontSize=45, width=79, height=79, textColor=WHITE, backgroundColor=color, justified='center', nickname=None)


    def draw(self):
        for i in range(6):
            for j in range(5):
                pygame.draw.rect(self.window,  BLACK, (115 + j*(85), 100+i*(85), 80, 80), width=1)
                self.grid_dic[str(i)+str(j)].draw()

