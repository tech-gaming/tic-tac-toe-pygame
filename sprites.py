import pygame
from settings import *


class Icon:
    def __init__(self, x, y, text):
        self.x, self.y = x, y
        self.text = text

    def draw(self, screen):
        font = pygame.font.SysFont("Consolas", 70)
        text = font.render(self.text, True, WHITE)
        font_size = font.size(self.text)
        draw_x = self.x + (TILESIZE/2) - font_size[0] / 2
        draw_y = self.y + (TILESIZE/2) - font_size[1] / 2
        screen.blit(text, (draw_x, draw_y))


class Board:
    def __init__(self):
        self.board_list = [["" for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    def draw_board(self, screen):
        for row in range(0, TILESIZE * 2, TILESIZE):
            pygame.draw.line(screen, WHITE, (MARGIN_X + row + TILESIZE, MARGIN_Y), (MARGIN_X + row + TILESIZE, MARGIN_Y + BOARD_SIZE * TILESIZE), 4)

        for col in range(0, TILESIZE * 2, TILESIZE):
            pygame.draw.line(screen, WHITE, (MARGIN_X, MARGIN_Y + col + TILESIZE), (MARGIN_X + BOARD_SIZE * TILESIZE, MARGIN_Y + col + TILESIZE), 4)

    def is_clicked(self, mouse_x, mouse_y):
        for row in range(len(self.board_list)):
            for col in range(len(self.board_list[row])):
                x, y = board_to_pixel(col, row)
                if x <= mouse_x <= x + TILESIZE and y <= mouse_y <= y + TILESIZE and self.board_list[row][col] == "":
                    return row, col

        return None, None

    def is_board_full(self):
        return not any("" in row for row in self.board_list)


class UIElement:
    def __init__(self, x, y, text):
        self.x, self.y = x, y
        self.text = text

    def draw(self, screen, font_size):
        font = pygame.font.SysFont("Consolas", font_size)
        text = font. render(self.text, True, WHITE)
        screen.blit(text, (self.x, self.y))

