# COLORS (r, g, b)
WHITE = (255, 255, 255)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)

# game settings
WIDTH = 500
HEIGHT = 600
FPS = 60
title = "Tic-Tac-Toe"
BGCOLOUR = DARKGREY

TILESIZE = 120
BOARD_SIZE = 3

MARGIN_X = int((WIDTH - (BOARD_SIZE * TILESIZE)) / 2)
MARGIN_Y = int((HEIGHT - (BOARD_SIZE * TILESIZE)) / 2)


def board_to_pixel(x, y):
    return MARGIN_X + TILESIZE * x, MARGIN_Y + TILESIZE * y
