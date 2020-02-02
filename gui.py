import pygame
import sudoku

background_colour = (255,255,255)
(width, height) = (600, 600)
scr = pygame.display.set_mode((width, height))
scr.fill(background_colour)

pygame.display.flip()

class Grid:
    rows = 9
    cols = 9
    def __init__(self, missing):
        s = sudoku.Sudoku(9, 9, missing)

    def draw(self):
        for i in range(Grid.cols):
            if i % 3 == 0:
                pygame.draw.lines(scr, (0,0,0), False, [(width*i/9, 0), (width*i/9, height)], 3)
            else:
                pygame.draw.lines(scr, (0,0,0), False, [(width*i/9, 0), (width*i/9, height)], 1)

        for i in range(Grid.rows):
            if i % 3 == 0:
                pygame.draw.lines(scr, (0,0,0), False, [(0, height*i/9), (width, height*i/9)], 3)
            else:
                pygame.draw.lines(scr, (0,0,0), False, [(0, height*i/9), (width, height*i/9)], 1)

        pygame.display.flip()



g = Grid(3)
g.draw()

while 1:
    pass
