import pygame
import time
import sys

from pygame import MOUSEBUTTONDOWN, MOUSEBUTTONUP

from Piece import Pieces
import Board


WIDTH = HEIGHT = 800
DIMENSIONS = 8
SQUARE = WIDTH // DIMENSIONS

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

WHITE = (255, 255, 255)
GREY = (128, 128, 128)
YELLOW = (204, 204, 0)
BLUE = (50, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (195, 216, 228)  # Made these in case pure white and black interfere with the
DARK_BLUE = (78, 109, 128)    # colors of the pieces


board = [['  ' for i in range(8)] for i in range(8)]

pieces = {}  # Dictionary to assign piece names to their piece objects
''' To access piece images call from dictionary pieces. Ex: pieces['white_king'] '''

piece_names = ['white_king', 'white_queen', 'white_rook', 'white_bishop', 'white_knight', 'white_pawn',
               'black_king', 'black_queen', 'black_rook', 'black_bishop', 'black_knight', 'black_pawn']
for p in piece_names:
    new_piece = Pieces()
    new_piece.name = p
    new_piece.color = p[0]
    new_piece.image = "piece_images/" + p + ".png"

    pieces[p] = new_piece

# assigned indexes to pieces using the pieces dictionary
piece_loc = {(0, 0): pieces["white_rook"], (0, 1): pieces["white_knight"],
    (0, 2): pieces["white_bishop"], (0, 3): pieces["white_king"], (0, 4): pieces["white_queen"],
    (0, 5): pieces["white_bishop"],(0, 6): pieces["white_knight"],(0, 7): pieces["white_rook"],
    (1, 0): pieces["white_pawn"], (1, 1): pieces["white_pawn"], (1, 2): pieces["white_pawn"],
    (1, 3): pieces["white_pawn"], (1, 4): pieces["white_pawn"], (1, 5): pieces["white_pawn"],
    (1, 6): pieces["white_pawn"], (1, 7): pieces["white_pawn"],
    (2, 0): " ", (2, 1): " ", (2, 2): " ", (2, 3): " ", (2, 4): " ", (2, 5): " ", (2, 6): " ", (2, 7): " ",
    (3, 0): " ", (3, 1): " ", (3, 2): " ", (3, 3): " ", (3, 4): " ", (3, 5): " ", (3, 6): " ", (3, 7): " ",
    (4, 0): " ", (4, 1): " ", (4, 2): " ", (4, 3): " ", (4, 4): " ", (4, 5): " ", (4, 6): " ", (4, 7): " ",
    (5, 1): " ", (5, 2): " ", (5, 3): " ", (5, 4): " ", (5, 5): " ", (5, 6): " ", (5, 7): " ",
    (6, 0): pieces["black_pawn"], (6, 1): pieces["black_pawn"], (6, 2): pieces["black_pawn"],
    (6, 3): pieces["black_pawn"],
    (6, 4): pieces["black_pawn"], (6, 5): pieces["black_pawn"],(6, 6): pieces["black_pawn"],
    (6, 7): pieces["black_pawn"], (7, 0): pieces["black_rook"], (7, 1): pieces["black_knight"],
    (7, 2): pieces["black_bishop"], (7, 3): pieces["black_king"], (7, 4): pieces["black_queen"],
    (7, 5): pieces["black_bishop"], (7, 6): pieces["black_knight"], (7, 7): pieces["black_rook"]}

# places the pieces on the board given the index
for key_coord in piece_loc:
    x_c, y_c = key_coord
    try:
        board[x_c][y_c] = piece_loc.get(key_coord).name
    except AttributeError:
        board[x_c][y_c] = piece_loc.get(key_coord)

print(piece_loc)

'''adds all the pieces to the appropriate squares'''


def board_setup():
    raise NameError("Unimplemented")


'''prints the board function'''


def print_board():
    for i in range(8):
        print(board[i])


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

    def draw(self, win):
        x, y = self.index
        scale = WIDTH/DIMENSIONS
        pygame.draw.rect(win, self.color, (x * scale, y * scale, scale, scale))

    def get_center(self):
        x, y = self.index
        scale = WIDTH / DIMENSIONS
        return x * scale + (scale/2), y * scale + (scale/2)

    # def is_int(self, piece):
    # if piece.


'''Generates all tiles and defines the colors/specifications uses the draw function in tile'''


def tile_generator(win):
    font = pygame.font.Font(None, 25)
    all_tiles = []
    tile_count = 0
    last_color_white = True
    for i in range(DIMENSIONS):
        last_color_white = not last_color_white
        for j in range(DIMENSIONS):
            temp_color = DARK_BLUE
            opposite_color = WHITE
            if not last_color_white:
                temp_color = WHITE
                opposite_color = BLACK
            last_color_white = not last_color_white

            temp_tile = Tile()
            temp_tile.index = (i, j)
            temp_tile.chess_id = str(chr(j + 65)) + str(i + 1)
            temp_tile.color = temp_color
            all_tiles.append(temp_tile)
            temp_tile.draw(win)

            text = font.render(temp_tile.chess_id, True, opposite_color)
            text_rect = text.get_rect(center=(i * SQUARE + SQUARE - 15, j * SQUARE + SQUARE - 10))
            window.blit(text, text_rect)

    return all_tiles


def draw_grid(win, rows, width):
    gap = width // 8
    for i in range(rows):
        pygame.draw.line(win, WHITE, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, WHITE, (j * gap, 0), (j * gap, width))

''' 
    Implemented piece rendering, only bishops for now. I imagine to get starting position correct
    we will need to set current_piece in the tile_gen function above
'''
def place_pieces(win, all_tiles):
    for key in piece_loc:
        x_co, y_co = key
        try:
            img = pygame.image.load(piece_loc[key].image)
            img.convert()
            win.blit(img, pygame.Rect(x_co * SQUARE + 20, y_co * SQUARE + 20, SQUARE, SQUARE))
        except AttributeError:
            pass

def main():
    pygame.init()
    print_board()
    # draw_grid(window, DIMENSIONS, WIDTH)
    all_tiles = tile_generator(window)
    place_pieces(window, all_tiles)
    pygame.display.update()

    while True:
        pygame.time.delay(50)

        # causes exit not to break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                moving = True
            elif event.type == MOUSEBUTTONUP:
                moving = False


if __name__ == "__main__":
    main()

