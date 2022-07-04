import pygame
import time
import sys

import Piece
import Board

WIDTH = HEIGHT = 800
DIMENSION = 8

board = [['  ' for i in range(DIMENSION)] for i in range(DIMENSION)]

'''adds all the pieces to the appropriate squares'''


def board_setup():
    raise NameError("Unimplemented")


'''prints the board function'''


def print_board():
    raise NameError("Unimplemented")


'''move(selected_index). Takes in selected index and runs the move algorithm in pieces for the piece'''

def move(selected_index):
    raise NameError("Unimplemented")


'''I added some basic code that creates a grid on a blank canvas, from here we need to create a TILE class
that should have all the entities that go along with tiles like the chess location (a1, a2) the index (0,0)(1,1)
current piece, color, etc'''

class Tile:
    def __int__(self, index: (int, int), chess_id, color, current_piece=' '):
        self.index = index
        self.chess_id = chess_id
        self.color = color
        self.current_piece = current_piece

    def draw(self, window):
        x, y = enumerate(self.index)
        pygame.draw.rect(window, self.color, (x, y, DIMENSION, DIMENSION))



'''Generates all tiles and defines the colors/specifications uses the draw function in tile'''
def tile_generator():
    raise NameError("unimplemented")

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

WHITE = (255, 255, 255)
GREY = (128, 128, 128)
YELLOW = (204, 204, 0)
BLUE = (50, 255, 255)
BLACK = (0, 0, 0)


def draw_grid(win, rows, width):
    gap = width // DIMENSION
    for i in range(rows):
        pygame.draw.line(win, WHITE, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, WHITE, (j * gap, 0), (j * gap, width))

def main():
    draw_grid(window, DIMENSION, WIDTH)
    pygame.display.update()

    while True:
        pygame.time.delay(50)

        # causes exit not to break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

main()
