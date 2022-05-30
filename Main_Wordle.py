# pygame demo 0 - window only

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import pygwidgets
from UI.Wordle_constants import*
from UI.Keyboard import*
from UI.Grid import*
from Logic.Rule import Rule


# 2 - Define constants
FRAMES_PER_SECOND = 30
MAX_TRIAL = 6
WORD_LENGTH = 5

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
 
# 4 - Load assets: image(s), sound(s),  etc.

# 5 - Initialize variables
oKeyboard = Keyboard(window)
oGrid = Grid(window)
oRule = Rule()
trial = 0
column = 0
word = []
isSolved = False

title = pygwidgets.DisplayText(window, (270, 20), 'Wordle', fontSize=40, justified='center')
won = pygwidgets.DisplayText(window, (240, 50), value='You Won!!!', fontSize=50, textColor=GREEN, justified='center', nickname=None)
lost =pygwidgets.DisplayText(window, (240, 50), value='You Lost! \n'+ 'Word was ' + oRule.get_secret(), fontSize=30, textColor=(255,0,0), justified='center', nickname=None)
invalid =pygwidgets.DisplayText(window, (240, 50), value='Invalid Word!' , fontSize=30, textColor=(255,0,0), justified='center', nickname=None)


# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end program 
        if event.type == pygame.QUIT:           
            pygame.quit()  
            sys.exit()

        if not isSolved and trial != MAX_TRIAL:
            
            isPressed, pressedChar = oKeyboard.handleEvent(event)
            if isPressed:
                if pressedChar == 'BACKSPACE' and column > 0:
                    column -=1
                    oGrid.setText(trial, column, '')
                    word.pop()
                if pressedChar == 'RETURN' and column == 5:
                    if oRule.isValidWord(''.join(word)):
                        column = 0
                        trial += 1
                        isSolved, inWord, inLoc = oRule.solve(word)
                        oGrid.update(trial-1,word, inWord, inLoc)
                        oKeyboard.update(word, inWord, inLoc)
                        word = []
                    # else:
                    #     timeStarted = time.time()
                    #     while time.time() - timeStarted < 10:
                    #         invalid.draw()
                    #         print('test')
                        
                    
                elif pressedChar not in ['BACKSPACE', 'RETURN'] and column < WORD_LENGTH  and trial < MAX_TRIAL:
                    oGrid.setText(trial, column, pressedChar)
                    word.append(pressedChar)
                    column +=1
                
        
                      

    # 8 - Do any "per frame" actions
    
    # 9 - Clear the window
    window.fill(WHITE)
    
    # 10 - Draw all window elements

    title.draw()
    oKeyboard.draw()
    oGrid.draw()
    if isSolved:
        won.draw()
    else:
        if  trial == MAX_TRIAL:
            lost.draw()
    if pressedChar == 'RETURN' and column == 5:
        if not oRule.isValidWord(''.join(word)):
            invalid.draw()
                

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait


