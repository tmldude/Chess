import pygame
import time
import sys

from Piece import Pieces
import Board

board = [['  ' for i in range(8)] for i in range(8)]
pieces = {}  # Dictionary to assign piece names to their respective images

WIDTH = HEIGHT = 800

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

WHITE = (255, 255, 255)
GREY = (128, 128, 128)
YELLOW = (204, 204, 0)
BLUE = (50, 255, 255)
BLACK = (0, 0, 0)

def init_pieces():
    piece_names = ['white_king', 'white_queen', 'white_rook', 'white_bishop', 'white_knight', 'white_pawn',
                   'black_king', 'black_queen', 'black_rook', 'black_bishop', 'black_knight', 'black_pawn']
    for p in piece_names:
        new_piece = Pieces()
        new_piece.name = p
        new_piece.color = p[0]
        new_piece.image = "piece_images/" + p + ".png"

        pieces[p] = new_piece


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
        x, y = self.index
        scale = WIDTH/8
        pygame.draw.rect(window, self.color, (x * scale, y * scale, scale, scale))



'''Generates all tiles and defines the colors/specifications uses the draw function in tile'''
def tile_generator(win, num_row):
    font = pygame.font.Font(None, 25)
    all_tiles = []
    tile_count = 0
    last_color_white = True
    for i in range(num_row):
        last_color_white = not last_color_white
        for j in range(num_row):
            temp_color = BLACK
            if not last_color_white:
                temp_color = WHITE
            last_color_white = not last_color_white
            temp_tile = Tile()
            temp_tile.index = (i, j)
            temp_tile.chess_id = str(chr(j + 65)) + str(i + 1)
            temp_tile.color = temp_color
            all_tiles.append(temp_tile)
            temp_tile.draw(win)

            text = font.render(temp_tile.chess_id, True, YELLOW)
            text_rect = text.get_rect(center=(i * (WIDTH / 8) + (WIDTH / 8) - 15, j * (WIDTH / 8) + (WIDTH / 8) - 10))
            window.blit(text, text_rect)

    return all_tiles





def draw_grid(win, rows, width):
    gap = width // 8
    for i in range(rows):
        pygame.draw.line(win, WHITE, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, WHITE, (j * gap, 0), (j * gap, width))

'''
does not work yet, placing pieces might have to do with a dictionary and the board and has to be done 
individually 
def place_pieces(win, all_tiles):
    for i in range(4):
        for j in range(8):
            all_tiles
            img = pygame.image.load('bird.png')
            img.convert()
'''


def main():
    pygame.init()
    init_pieces()
    #draw_grid(window, 8, WIDTH)
    all_tiles = tile_generator(window, 8)
    pygame.display.update()

    while True:
        pygame.time.delay(50)

        # causes exit not to break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()
