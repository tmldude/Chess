import pygame
import sys

from pygame import MOUSEBUTTONDOWN

from Piece import Pieces
import Piece as Pi

import Move as Mo

WIDTH = HEIGHT = 800
DIMENSIONS = 8
SQUARE = WIDTH // DIMENSIONS

WHITE = (255, 255, 255)
GREY = (128, 128, 128)
YELLOW = (204, 204, 0)
BLUE = (50, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
LIGHT_BLUE = (195, 216, 228)
DARK_BLUE = (78, 109, 128)

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

board = [['  ' for i in range(8)] for j in range(8)]

pieces = {}  # Dictionary to assign piece names to their piece objects
''' To access piece images call from dictionary pieces. Ex: pieces['white_king'] '''

piece_names = ['white_king', 'white_queen', 'white_rook', 'white_bishop', 'white_knight', 'white_pawn',
               'black_king', 'black_queen', 'black_rook', 'black_bishop', 'black_knight', 'black_pawn']

for p in piece_names:
    new_piece = Pieces(p, p[0], "piece_images/" + p + ".png")
    pieces[p] = new_piece

# assigned indexes to pieces using the pieces dictionary
piece_loc = {(0, 0): pieces["white_rook"], (0, 1): pieces["white_knight"],
             (0, 2): pieces["white_bishop"], (0, 3): pieces["white_queen"], (0, 4): pieces["white_king"],
             (0, 5): pieces["white_bishop"], (0, 6): pieces["white_knight"], (0, 7): pieces["white_rook"],
             (1, 0): pieces["white_pawn"], (1, 1): pieces["white_pawn"], (1, 2): pieces["white_pawn"],
             (1, 3): pieces["white_pawn"], (1, 4): pieces["white_pawn"], (1, 5): pieces["white_pawn"],
             (1, 6): pieces["white_pawn"], (1, 7): pieces["white_pawn"],
             (2, 0): " ", (2, 1): " ", (2, 2): " ", (2, 3): " ", (2, 4): " ", (2, 5): " ", (2, 6): " ", (2, 7): " ",
             (3, 0): " ", (3, 1): " ", (3, 2): " ", (3, 3): " ", (3, 4): " ", (3, 5): " ", (3, 6): " ", (3, 7): " ",
             (4, 0): " ", (4, 1): " ", (4, 2): " ", (4, 3): " ", (4, 4): " ", (4, 5): " ", (4, 6): " ", (4, 7): " ",
             (5, 0): " ", (5, 1): " ", (5, 2): " ", (5, 3): " ", (5, 4): " ", (5, 5): " ", (5, 6): " ", (5, 7): " ",
             (6, 0): pieces["black_pawn"], (6, 1): pieces["black_pawn"], (6, 2): pieces["black_pawn"],
             (6, 3): pieces["black_pawn"],
             (6, 4): pieces["black_pawn"], (6, 5): pieces["black_pawn"], (6, 6): pieces["black_pawn"],
             (6, 7): pieces["black_pawn"], (7, 0): pieces["black_rook"], (7, 1): pieces["black_knight"],
             (7, 2): pieces["black_bishop"], (7, 3): pieces["black_queen"], (7, 4): pieces["black_king"],
             (7, 5): pieces["black_bishop"], (7, 6): pieces["black_knight"], (7, 7): pieces["black_rook"]}

# for testing
empty_piece_loc = \
    {(0, 0): " ", (0, 1): " ", (0, 2): " ", (0, 3): " ", (0, 4): " ", (0, 5): " ", (0, 6): " ", (0, 7): " ",
     (1, 0): " ", (1, 1): " ", (1, 2): " ", (1, 3): " ", (1, 4): " ", (1, 5): " ", (1, 6): " ", (1, 7): " ",
     (2, 0): " ", (2, 1): " ", (2, 2): " ", (2, 3): " ", (2, 4): " ", (2, 5): " ", (2, 6): " ", (2, 7): " ",
     (3, 0): " ", (3, 1): " ", (3, 2): " ", (3, 3): " ", (3, 4): " ", (3, 5): " ", (3, 6): " ", (3, 7): " ",
     (4, 0): " ", (4, 1): " ", (4, 2): " ", (4, 3): " ", (4, 4): " ", (4, 5): " ", (4, 6): " ", (4, 7): " ",
     (5, 0): " ", (5, 1): " ", (5, 2): " ", (5, 3): " ", (5, 4): " ", (5, 5): " ", (5, 6): " ", (5, 7): " ",
     (6, 0): " ", (6, 1): " ", (6, 2): " ", (6, 3): " ", (6, 4): " ", (6, 5): " ", (6, 6): " ", (6, 7): " ",
     (7, 0): " ", (7, 1): " ", (7, 2): " ", (7, 3): " ", (7, 4): " ", (7, 5): " ", (7, 6): " ", (7, 7): " "}


def empty_board(piece_dict):
    for key in piece_dict:
        piece_dict[key] = " "


# places the pieces on the board given the index
for key_coord in piece_loc:
    x_c, y_c = key_coord
    try:
        board[x_c][y_c] = piece_loc.get(key_coord).name
    except AttributeError:
        board[x_c][y_c] = piece_loc.get(key_coord)


# prints the board function
def print_board():
    for i in range(8):
        print(board[i])


def get_possible_moves(selected_index: (int, int), white_move: bool, king_index: (int, int),
                       last_move: Mo.Move = None) -> list[(int, int)]:
    """
    get_possible_moves(selected_index, white_move, king_index, last_move)
    :param selected_index: index of the user chosen piece
    :param white_move: bool saying if black or white's move
    :param king_index: index of the king of the color either black's or white's king
    :param last_move: the last move made on the board to test En Passant
    - Checks all moves whether they are legal or not. Creating checks/blocking checks
    - Covers castling
    :return: list[(int, int)] of all legal moves for the piece at selected index
    """

    r, c = selected_index
    selected_piece = piece_loc[r, c]
    piece_name = selected_piece.name

    # gets the possible moves from the individual piece functions in Piece
    if piece_name == 'white_pawn':
        moves = Pi.pawn_move_white(selected_index, piece_loc, last_move)
    elif piece_name == 'black_pawn':
        moves = Pi.pawn_move_black(selected_index, piece_loc, last_move)
    elif 'rook' in piece_name:
        moves = Pi.rook_move(selected_index, piece_loc, white_move)
    elif 'bishop' in piece_name:
        moves = Pi.bishop_move(selected_index, piece_loc, white_move)
    elif 'knight' in piece_name:
        moves = Pi.knight_move(selected_index, piece_loc, white_move)
    elif 'queen' in piece_name:
        moves = Pi.queen_move(selected_index, piece_loc, white_move)
    else:
        moves = Pi.king_move(selected_index, piece_loc, white_move)

    # checks each move to see if it creates or can stop checks
    # adds them if they do not create checks and if the can block a check
    checked = []
    for move in moves:
        copy = piece_loc.copy()
        temp = copy[selected_index]
        copy[move] = temp
        copy[selected_index] = ' '
        if 'king' in piece_name:
            checks = Pi.check_king_attacked(copy, move, white_move)
        else:
            checks = Pi.check_king_attacked(copy, king_index, white_move)
        if not checks:
            checked.append(move)

    # the special castling condition
    if 'king' in piece_name and not selected_piece.has_moved and \
            not Pi.check_king_attacked(piece_loc, selected_index, white_move):
        checked += attempt_castle(white_move)

    return checked


def attempt_castle(white_move: bool) -> list[(int, int)]:
    """
    attempt_white_castle(white_move)
    :param white_move: bool for whose turn it is: True = white, False = black
    - Depending on the bool white_move the criteria switch for checking the white or black castling
    - The testing is extensive because the king movement in castling cannot be done through a check
        but the rook can be attacked or move through check. Additionally, there cannot be pieces inbetween them
    - The function output is processed in main where specific movement criteria must be met
    :return: list[(int, int)] outputs a list of 4 possible castle moves: white king side, white queen side
        maximum size of outputted list is 2, king side/queen side castle for each color
    """
    pos_castles = []
    x = 7
    test_name = 'black_rook'
    if white_move:
        x = 0
        test_name = 'white_rook'
    if piece_loc[(x, 0)] != ' ':
        if piece_loc[(x, 0)].name == test_name and not piece_loc[(x, 0)].has_moved and \
                piece_loc[(x, 1)] == ' ' and piece_loc[(x, 2)] == ' ' and piece_loc[(x, 3)] == ' ':
            seven_two = Pi.check_king_attacked(piece_loc, (x, 2), white_move)
            seven_three = Pi.check_king_attacked(piece_loc, (x, 3), white_move)
            if not seven_two and not seven_three:
                pos_castles.append((x, 0))
    if piece_loc[(x, 7)] != ' ':
        if piece_loc[(x, 7)].name == test_name and not piece_loc[(x, 7)].has_moved and \
                piece_loc[(x, 5)] == ' ' and piece_loc[(x, 6)]:
            seven_five = Pi.check_king_attacked(piece_loc, (x, 5), white_move)
            seven_six = Pi.check_king_attacked(piece_loc, (x, 6), white_move)
            if not seven_five and not seven_six:
                pos_castles.append((x, 7))
    return pos_castles


def check_if_mate(king_index: (int, int), is_white: bool, last_move: Mo.Move) -> bool:
    """
    check_if_mate(king_index, is_white, last_move)
    :param king_index: index of the selected king
    :param is_white: True when white king, False when black king
    :param last_move: last move a user inputted and was played for En Passant
    - checks every piece of a certain color to see if they can move at all. This is regular movement, blocking mate,
         king moving out of mate etc.
    - If there are no possible moves then it is checkmate
    :return:
            False = not checkmate
            True = checkmate
    """
    color = 'b'
    if is_white:
        color = 'w'

    pos_moves = []
    for key in piece_loc:
        temp = piece_loc[key]
        if temp != ' ':
            if temp.color == color:
                moves = get_possible_moves(key, is_white, king_index, last_move)
                pos_moves += moves
                if pos_moves:
                    return False
    return True


class Tile:
    """
    Tile: The board tile
    :param index: the x, y coordinate of the tile on a (0,0)->(7,7) 8x8 grid
    :param chess_id: the chess board ID of a given tile. Example: (0,0) = A1
    :param color: the color of the tile when it is drawn
    """

    def __init__(self, index: (int, int), chess_id, color):
        self.index = index
        self.chess_id = chess_id
        self.color = color

    def draw(self, win):
        x, y = self.index
        scale = WIDTH / DIMENSIONS
        pygame.draw.rect(win, self.color, (x * scale, y * scale, scale, scale))

    def get_center(self):
        x, y = self.index
        scale = WIDTH / DIMENSIONS
        return x * scale + (scale / 2), y * scale + (scale / 2)


def tile_generator(win, king_index_list, pos_moves=None):
    """
    tile_generator(win, in_check, pos_moves)
    :param win: the PyGames window
    :param king_index_list: It is a list of king coordinates to be used to see uf that king is in check. Used
        when deciding if a tile needs to be the color RED to indicate a king in check
    :param pos_moves: the moves to be highlighted. None if returning the board back to default ie un-highlighting
    - Generates all tiles and defines the colors/specifications uses the draw function in tile
    - Placed the tiles on the newly generated board
    - Draws a grid (if enabled, causes lag)
    - Updates the PyGames display
    """

    if pos_moves is None:
        pos_moves = []
    font = pygame.font.Font(None, 25)

    for i in range(DIMENSIONS):
        for j in range(DIMENSIONS):
            chosen_tile_color = DARK_BLUE
            opposite_color = WHITE
            if (i + j) % 2 == 0:
                chosen_tile_color = WHITE
                opposite_color = BLACK

            # generates tiles given color choices above
            temp_tile = Tile((i, j), str(chr(j + 65)) + str(i + 1), chosen_tile_color)
            # checks to see if tile needs to be highlighted
            tile_color = opposite_color
            if temp_tile.index in pos_moves:
                temp_tile.color = LIGHT_BLUE
                tile_color = YELLOW

            # checks if the king tile needs to be red
            if Pi.check_king_attacked(piece_loc, king_index_list[0], True):
                in_check = king_index_list[0]
            elif Pi.check_king_attacked(piece_loc, king_index_list[1], False):
                in_check = king_index_list[1]
            else:
                in_check = (-1, -1)
            if temp_tile.index == in_check:
                temp_tile.color = RED

            temp_tile.draw(win)

            # generates tile chess coordinate
            # text = font.render(temp_tile.chess_id, True, opposite_color)
            if i == 0 or j == 0:
                text = font.render(temp_tile.chess_id, True, tile_color)
                text_rect = text.get_rect(
                    center=(i * SQUARE + SQUARE - (SQUARE / 7), j * SQUARE + SQUARE - (SQUARE / 10)))
                window.blit(text, text_rect)

    # draw_grid(window, WIDTH, WIDTH)  # adds a lot of lag
    place_pieces(window)
    pygame.display.update()


# Draws a grid to outline the tiles
def draw_grid(win, rows, width):
    gap = width // 8
    for i in range(rows):
        pygame.draw.line(win, BLACK, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, BLACK, (j * gap, 0), (j * gap, width))


# Places pieces and their images on starting tiles.
def place_pieces(win):
    for key in piece_loc:
        x_co, y_co = key
        try:
            piece_loc[key].active_image = pygame.image.load(piece_loc[key].image)
            piece_loc[key].active_image.convert()
            win.blit(piece_loc[key].active_image, pygame.Rect(x_co * SQUARE + SQUARE / 5,
                                                              y_co * SQUARE + SQUARE / 5, SQUARE, SQUARE))
        except AttributeError:
            pass


# Takes in mouse position and outputs the rank and file of the tile to be used for identification
def get_tile(mouse_pos):
    x, y = mouse_pos
    rank = x // SQUARE
    file = y // SQUARE
    return rank, file

# sets the coordinate of in_check to turn the tile red
def in_check_finder(king_index_list):
    if Pi.check_king_attacked(piece_loc, king_index_list[0], True):
        return king_index_list[0]
    elif Pi.check_king_attacked(piece_loc, king_index_list[1], False):
        return king_index_list[1]
    else:
        return -1, -1

def promotion_func(mouse_coords, is_white: bool):
    """
    promotion_func(mouse_coords, is_white):
    :param mouse_coords: the coordinates of the cursor
    :param is_white: bool for whose turn it is: True = white, False = black
    :return:
    """
    scale = WIDTH / DIMENSIONS
    color_depends = WHITE
    queen = pieces['black_queen']
    bishop = pieces['black_bishop']
    knight = pieces['black_knight']
    rook = pieces['black_rook']
    if is_white:
        color_depends = BLACK
        queen = pieces['white_queen']
        bishop = pieces['white_bishop']
        knight = pieces['white_knight']
        rook = pieces['white_rook']

    pygame.draw.rect(window, color_depends, pygame.Rect(scale * 2, scale * 2, scale * 4, scale))

    queen_index = (2, 2)
    bishop_index = (3, 2)
    knight_index = (4, 2)
    rook_index = (5, 2)
    possible_choices = {queen_index: queen, bishop_index: bishop,
                        knight_index: knight, rook_index: rook}

    queen_img = pygame.image.load(queen.image)
    bishop_img = pygame.image.load(bishop.image)
    knight_img = pygame.image.load(knight.image)
    rook_img = pygame.image.load(rook.image)

    queen_img.convert()
    bishop_img.convert()
    knight_img.convert()
    rook_img.convert()

    image_list = [queen_img, bishop_img, knight_img, rook_img]
    i = 0
    for image in image_list:
        window.blit(image, pygame.Rect(WIDTH / 4 + (i * 100) + 20, HEIGHT / 4 + (scale / 4) - 15, scale, scale))
        i += 1

    pygame.display.update()
    selected_piece = get_tile(mouse_coords)

    for choices in possible_choices:
        if selected_piece == choices:
            return possible_choices[choices]
    return ' '


def return_pgn_file(move_history: list[Mo.Move]) -> str:
    """
    return_pgn_file(move_history):
    :param move_history: list of Move class objects storing the history of move
    - Takes in the move list and uses the data to craft a string so the game can be easily retraced
    :return: Outputs a crafted string of the games move history
        Example:
        Black | White
        1 d4 | d5
        2 knf3 | bd3
        etc
    """
    raise NameError("Unimplemented")


def main():
    pygame.init()

    pos_moves = []
    last_two_tile = []  # Tracks last two clicks of user
    last_move = Mo.Move(None, None, None, None)
    move_log = []  # Tuple that stores previously executed moves
    king_index = [(0, 4), (7, 4)]
    white_move = True
    white_promotion = False
    black_promotion = False

    print_board()
    tile_generator(window, king_index)

    while True:
        pygame.time.delay(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:  # Two clicks to move, not drag and drop.
                mouse_coords = pygame.mouse.get_pos()
                selected_tile = get_tile(mouse_coords)

                if white_promotion:
                    chosen = promotion_func(mouse_coords, True)
                    if chosen != ' ':
                        piece_loc[last_move.end_index] = chosen
                        board[last_move.end_index[0]][last_move.end_index[1]] = chosen.name
                        white_promotion = False
                        tile_generator(window, king_index)
                elif black_promotion:
                    chosen = promotion_func(mouse_coords, False)
                    if chosen != ' ':
                        piece_loc[last_move.end_index] = chosen
                        board[last_move.end_index[0]][last_move.end_index[1]] = chosen.name
                        black_promotion = False
                        tile_generator(window, king_index)

                elif check_if_mate(king_index[0], True, last_move):
                    print("Black Wins!")

                elif check_if_mate(king_index[1], False, last_move):
                    print("White Wins!")

                # if there are no tiles in last_two_tile, appends the current tile to last_two_tiles
                # also gets the possible moves, validates them, and highlights them on the board
                elif len(last_two_tile) == 0:
                    # catches an attribute error if the selected tile has no piece
                    try:
                        if white_move and piece_loc[selected_tile].color == 'w':
                            pos_moves = get_possible_moves(selected_tile, white_move, king_index[0], last_move)
                            tile_generator(window, king_index, pos_moves)
                            last_two_tile.append(selected_tile)
                        if not white_move and piece_loc[selected_tile].color == 'b':
                            pos_moves = get_possible_moves(selected_tile, white_move, king_index[1], last_move)
                            tile_generator(window, king_index, pos_moves)
                            last_two_tile.append(selected_tile)
                    except AttributeError:
                        print("No piece selected or wrong turn")

                # if the length of last_two_tiles is 1 and the selected tile is in it
                # this if statement reverts the board back
                elif selected_tile in last_two_tile and len(last_two_tile) == 1:  # Double click square is undo
                    last_two_tile.clear()  # clears last 2 tuple
                    pos_moves = []  # clears possible moves
                    tile_generator(window, king_index)  # un highlights

                # once there are two tiles in last_two_tile, the board works to move the piece
                else:
                    last_two_tile.append(selected_tile)
                    start_pos = last_two_tile[0]
                    start_rank = last_two_tile[0][0]
                    start_file = last_two_tile[0][1]
                    end_pos = last_two_tile[1]
                    end_rank = last_two_tile[1][0]
                    end_file = last_two_tile[1][1]
                    last_two_tile.clear()
                    chosen_piece = piece_loc.get(start_pos)

                    if (end_rank, end_file) in pos_moves:
                        # castling possibility, alters the data so the function outputs correctly. The castling tests
                        # are done above and then added to pos_moves
                        # this still checks to see if the king has not moved before checking the individual rook
                        # coordinates and updating them
                        # specifically, this has to update the end coordinates of the king and
                        # move the rook which normally would be passed over if not selected
                        if 'king' in chosen_piece.name and not chosen_piece.has_moved:
                            new_rook_x = -1
                            new_rook_y = -1
                            rook_from = (-1, -1)
                            if end_pos == (0, 0):
                                end_file = 2
                                new_rook_x = 0
                                new_rook_y = 3
                                rook_from = (0, 0)
                            if end_pos == (7, 0):
                                end_file = 2
                                new_rook_x = 7
                                new_rook_y = 3
                                rook_from = (7, 0)
                            if end_pos == (0, 7):
                                end_file = 6
                                new_rook_x = 0
                                new_rook_y = 5
                                rook_from = (0, 7)
                            if end_pos == (7, 7):
                                end_file = 6
                                new_rook_x = 7
                                new_rook_y = 5
                                rook_from = (7, 7)
                            if new_rook_x != -1 and new_rook_y != -1:
                                end_pos = (end_rank, end_file)
                                pygame.Rect.move(piece_loc[rook_from].active_image.get_rect(),
                                                 new_rook_x * SQUARE + SQUARE / 5, new_rook_y * SQUARE + SQUARE / 5)
                                piece_loc[(new_rook_x, new_rook_y)] = piece_loc[rook_from]
                                piece_loc[rook_from] = ' '
                                board[new_rook_x][new_rook_y] = board[rook_from[0]][rook_from[1]]
                                board[rook_from[0]][rook_from[1]] = ' '

                        # en passant checks
                        if chosen_piece.name == 'black_pawn' and last_move.piece_name == 'white_pawn':
                            if piece_loc[end_pos] == ' ' and (end_file == start_file + 1 or end_file == start_file - 1):
                                piece_loc[last_move.end_index] = ' '
                                board[last_move.end_index[0]][last_move.end_index[1]] = ' '
                        if chosen_piece.name == 'white_pawn' and last_move.piece_name == 'black_pawn':
                            if piece_loc[end_pos] == ' ' and (end_file == start_file + 1 or end_file == start_file - 1):
                                piece_loc[last_move.end_index] = ' '
                                board[last_move.end_index[0]][last_move.end_index[1]] = ' '

                        # updates the board
                        pygame.Rect.move(chosen_piece.active_image.get_rect(),
                                         end_rank * SQUARE + SQUARE / 5, end_file * SQUARE + SQUARE / 5)

                        # updates the coordinates of the kings if they are moved
                        if 'king' in piece_loc[start_pos].name:
                            if chosen_piece.color == 'w':
                                king_index[0] = end_pos
                            else:
                                king_index[1] = end_pos

                        # tracks the current move and adds it to move_log
                        current_move = Mo.Move(chosen_piece.name, start_pos, end_pos, piece_loc[end_pos] != ' ')
                        move_log.append(current_move)
                        last_move = current_move

                        # updates piece_loc and board
                        piece_loc[end_pos] = piece_loc[start_pos]
                        piece_loc[start_pos] = ' '
                        board[end_rank][end_file] = board[start_rank][start_file]
                        board[start_rank][start_file] = ' '

                        # updates the tile, places pieces, and updates display
                        tile_generator(window, king_index)

                        piece_loc[end_pos].has_moved = True
                        print_board()

                        # promotion covering
                        if 'pawn' in last_move.piece_name:
                            if last_move.end_index[0] == 7 and piece_loc[last_move.end_index].color == 'w':
                                white_promotion = True
                            if last_move.end_index[0] == 0 and piece_loc[last_move.end_index].color == 'b':
                                black_promotion = True

                        # updates white move
                        if piece_loc[end_pos].color == 'w':
                            white_move = False
                        if piece_loc[end_pos].color == 'b':
                            white_move = True
                    else:
                        tile_generator(window, king_index)  # un highlights if selected no tile
                        print("impossible move")

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:  # Z for undo (Like ctrl + z)
                    if len(move_log) != 0:  # No moves have been made
                        # update_it_all(end_rank, end_file, start_rank, start_file)
                        pass
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
