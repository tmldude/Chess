import pygame
import time
import sys

from pygame import MOUSEBUTTONDOWN

from Piece import Pieces

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
DARK_BLUE = (78, 109, 128)  # colors of the pieces

global WHITES_MOVE
WHITES_MOVE = True

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
             (0, 5): pieces["white_bishop"], (0, 6): pieces["white_knight"], (0, 7): pieces["white_rook"],
             (1, 0): pieces["white_pawn"], (1, 1): pieces["white_pawn"], (1, 2): pieces["white_pawn"],
             (1, 3): pieces["white_pawn"], (1, 4): pieces["white_pawn"], (1, 5): pieces["white_pawn"],
             (1, 6): pieces["white_pawn"], (1, 7): pieces["white_pawn"],
             (2, 0): " ", (2, 1): " ", (2, 2): " ", (2, 3): " ", (2, 4): " ", (2, 5): " ", (2, 6): " ", (2, 7): " ",
             (3, 0): " ", (3, 1): " ", (3, 2): " ", (3, 3): " ", (3, 4): " ", (3, 5): " ", (3, 6): " ", (3, 7): " ",
             (4, 0): " ", (4, 1): " ", (4, 2): " ", (4, 3): " ", (4, 4): " ", (4, 5): " ", (4, 6): " ", (4, 7): " ",
             (5, 1): " ", (5, 2): " ", (5, 3): " ", (5, 4): " ", (5, 5): " ", (5, 6): " ", (5, 7): " ",
             (6, 0): pieces["black_pawn"], (6, 1): pieces["black_pawn"], (6, 2): pieces["black_pawn"],
             (6, 3): pieces["black_pawn"],
             (6, 4): pieces["black_pawn"], (6, 5): pieces["black_pawn"], (6, 6): pieces["black_pawn"],
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

'''prints the board function'''


def print_board():
    for i in range(8):
        print(board[i])


'''move(selected_index). Takes in selected index and runs the move algorithm in pieces for the piece'''


def move(selected_index):
    raise NameError("Unimplemented")


class Tile:
    def __int__(self, index: (int, int), chess_id, color, current_piece=' '):
        self.index = index
        self.chess_id = chess_id
        self.color = color
        self.current_piece = current_piece

    def draw(self, win):
        x, y = self.index
        scale = WIDTH / DIMENSIONS
        pygame.draw.rect(win, self.color, (x * scale, y * scale, scale, scale))

    def get_center(self):
        x, y = self.index
        scale = WIDTH / DIMENSIONS
        return x * scale + (scale / 2), y * scale + (scale / 2)

    # def is_int(self, piece):
    # if piece.


'''Generates all tiles and defines the colors/specifications uses the draw function in tile'''


def tile_generator(win):
    font = pygame.font.Font(None, 25)
    all_tiles = []
    tile_count = 0
    last_color_white = True
    for i in range(DIMENSIONS):
        row = []
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

            temp_tile.current_piece = piece_loc.get((i, j))
            row.append(temp_tile)
        all_tiles.append(row)
    return all_tiles


''' Depreciated '''


def draw_grid(win, rows, width):
    gap = width // 8
    for i in range(rows):
        pygame.draw.line(win, WHITE, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, WHITE, (j * gap, 0), (j * gap, width))


''' Places pieces and their images on starting tiles. '''


def place_pieces(win, all_tiles):
    for key in piece_loc:
        x_co, y_co = key
        try:
            piece_loc[key].active_image = pygame.image.load(piece_loc[key].image)
            piece_loc[key].active_image.convert()
            win.blit(piece_loc[key].active_image, pygame.Rect(x_co * SQUARE + 20, y_co * SQUARE + 20, SQUARE, SQUARE))
        except AttributeError:
            pass


def get_tile(mouse_pos):
    x, y = mouse_pos
    file = x // SQUARE
    rank = y // SQUARE
    return file, rank


''' Returns an array of every legal move for a player's turn '''


def get_legal_moves(tile):
    moves = []
    for r in range(DIMENSIONS):
        for c in range(DIMENSIONS):
            piece_color = piece_loc[(r, c)][0]  # For first letter of color.
            if piece_color == 'w' and WHITES_MOVE:
                if piece_loc[(r, c)[6] == 'p']:
                    moves.append(get_pawn_moves(r, c))
                elif piece_loc[(r, c)[6] == 'b']:
                    moves.append(get_bishop_moves(r, c))
                elif piece_loc[(r, c)[6] == 'r']:
                    moves.append(get_rook_moves(r, c))
                elif piece_loc[(r, c)[6] == 'q']:
                    moves.append(get_queen_moves(r, c))
                elif piece_loc[(r, c)[6] == 'k']:
                    if piece_loc[(r, c)[7] == 'n']:
                        moves.append(get_knight_moves(r, c))
                    else:
                        moves.append(get_king_moves(r, c))
                else:
                    pass
            elif piece_color == 'b' and not WHITES_MOVE:
                if piece_loc[(r, c)[6] == 'p']:
                    moves.append(get_pawn_moves(r, c))
                elif piece_loc[(r, c)[6] == 'b']:
                    moves.append(get_bishop_moves(r, c))
                elif piece_loc[(r, c)[6] == 'r']:
                    moves.append(get_rook_moves(r, c))
                elif piece_loc[(r, c)[6] == 'q']:
                    moves.append(get_queen_moves(r, c))
                elif piece_loc[(r, c)[6] == 'k']:
                    if piece_loc[(r, c)[7] == 'n']:
                        moves.append(get_knight_moves(r, c))
                    else:
                        moves.append(get_king_moves(r, c))
                else:
                    pass
            else:
                pass


''' Skeleton functions for piece move logic. I imagine we move this to a separate file after it's done to 
 save space. '''


def get_pawn_moves(row, col):
    pass


def get_knight_moves(row, col):
    pass


def get_bishop_moves(row, col):
    pass


def get_rook_moves(row, col):
    pass


def get_queen_moves(row, col):
    pass


def get_king_moves(row, col):
    pass


'''updates board, piece_loc, all_tles, reloads the whole board and moves pieces'''
def update_it_all(start_rank, start_file, end_rank, end_file):
    piece_loc[(end_rank, end_file)] = piece_loc[start_rank, start_file]
    piece_loc[start_rank, start_file] = ' '
    board[end_rank][end_file] = board[start_rank][start_file]
    board[start_rank][start_file] = ' '
    all_tiles = tile_generator(window)
    place_pieces(window, all_tiles)
    print_board()
    pygame.display.update()


def main():
    pygame.init()
    print_board()
    all_tiles = tile_generator(window)
    place_pieces(window, all_tiles)

    selected_tile = ()  # Tracks last click of user
    last_two_tile = []  # Tracks last two clicks of user
    move_log = []       # Tuple that stores previously executed moves

    pygame.display.update()

    while True:
        pygame.time.delay(50)

        # causes exit not to break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:  # Two clicks to move, not drag and drop.
                mouse_coords = pygame.mouse.get_pos()
                file, rank = get_tile(mouse_coords)
                if selected_tile == (file, rank):  # Double click square is undo
                    selected_tile = ()
                    last_two_tile = []
                else:
                    selected_tile = (file, rank)  # Reversed because horizontal view
                    last_two_tile.append(selected_tile)
                if len(last_two_tile) == 2:
                    start_rank = last_two_tile[0][0]
                    start_file = last_two_tile[0][1]
                    end_rank = last_two_tile[1][0]
                    end_file = last_two_tile[1][1]

                    try:
                        chosen_piece = piece_loc.get((start_rank, start_file))
                        pygame.Rect.move(chosen_piece.active_image.get_rect(),
                                         end_rank * SQUARE + 20, end_file * SQUARE + 20)
                        pygame.display.update()
                        move_log.append(last_two_tile)
                    except AttributeError:
                        print("you did not choose a piece")

                    update_it_all(start_rank, start_file, end_rank, end_file)

                    last_two_tile = []
                    selected_tile = ()

                    if len(move_log) == 1:
                        WHITES_MOVE = False
                    elif len(move_log) % 2 == 0:
                        WHITES_MOVE = True
                    elif len(move_log) % 2 == 1:
                        WHITES_MOVE = False
                    else:
                        pass

                    print("White to move? " + WHITES_MOVE)

                else:
                    pass
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:           # Z for undo (Like ctrl + z)
                    if len(move_log) != 0:            # No moves have been made
                        update_it_all(end_rank, end_file, start_rank, start_file)

                        # ^^ This function makes life easy, thanks for that. Only issue is captured piece not being
                        # returned to original square.
                    else:
                        pass
                else:
                    pass
            else:
                pass


if __name__ == "__main__":
    main()
