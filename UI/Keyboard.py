import pygame
import pygwidgets
from pygame.locals import *
from UI.Wordle_constants import*

class Keyboard():
    X_GAP = 5
    KEY_WIDTH = 40
    
    def __init__(self, window):
        self.window = window
        self.key_dic = {}
        i = 1
        for char in 'QWERTYUIOP':
            self.key_dic[char] = pygwidgets.TextButton(self.window, (60+i*(Keyboard.KEY_WIDTH + Keyboard.X_GAP),622), char,fontSize=30, textColor=BLACK, upColor=GRAY, nickname=char, width=Keyboard.KEY_WIDTH)
            i += 1
        i = 1
        for char in 'ASDFGHJKL':
            self.key_dic[char] = pygwidgets.TextButton(self.window, (80+i*(Keyboard.KEY_WIDTH + Keyboard.X_GAP),669), char,fontSize=30, textColor=BLACK, upColor=GRAY, nickname=char, width=Keyboard.KEY_WIDTH)
            i += 1
        i = 1
        for char in 'ZXCVBNM':
            self.key_dic[char] = pygwidgets.TextButton(self.window, (125+i*(Keyboard.KEY_WIDTH + Keyboard.X_GAP),716), char,fontSize=30, textColor=BLACK, upColor=GRAY, nickname=char, width=Keyboard.KEY_WIDTH)
            i += 1
        self.ENTER = pygwidgets.TextButton(self.window, (40+ Keyboard.KEY_WIDTH + Keyboard.X_GAP,716), 'ENTER',fontSize=25, textColor=BLACK, upColor=GRAY, nickname='RETURN', width=2*Keyboard.KEY_WIDTH)
        self.DELETE = pygwidgets.TextButton(self.window, (125+8*(Keyboard.KEY_WIDTH + Keyboard.X_GAP),716), 'DEL',fontSize=25, textColor=BLACK, upColor=GRAY, nickname='BACKSPACE', width=1.5*Keyboard.KEY_WIDTH)
        self.ValidKeys = [k for k in self.key_dic.keys()]
        self.ValidKeys.append('RETURN')
        self.ValidKeys.append('BACKSPACE')
    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN:
                char = pygame.key.name(event.key).upper()
                if char in self.ValidKeys:
                    return True, char
        for key in self.key_dic:
            if self.key_dic[key].handleEvent(event):
                return True, self.key_dic[key].getNickname()
        for key in [self.ENTER, self.DELETE]:
            if key.handleEvent(event):
                return True, key.getNickname()
        return False, None
    
    def update(self, word, inWord, inLoc):
        for j in range(5):
            if inLoc[j]:
                color = GREEN
            elif inWord[j]:
                color = ORANGE
            else:
                color = DARK_GRAY
            self.key_dic[word[j]] = pygwidgets.TextButton(self.window, self.key_dic[word[j]].getLoc(), self.key_dic[word[j]].getNickname(),fontSize=30, textColor=WHITE, upColor=color, nickname=self.key_dic[word[j]].getNickname(), width=Keyboard.KEY_WIDTH)


    def draw(self):
        for key in self.key_dic:
            self.key_dic[key].draw()
        self.ENTER.draw()
        self.DELETE.draw()