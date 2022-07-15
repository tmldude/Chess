import Move as Mo


class Pieces:
    def __init__(self, name, color, image, is_king=False):
        self.name = name
        self.color = color
        self.image = image
        self.is_king = is_king
        self.has_moved = False


'''The individual piece functions output possible moves on a 8x8 chess board for the piece at the 
given index. The function sort through a majority of piece issues including: attacking pieces of the same color,
piece moving to a normal square, and making sure the moves are on the chess grid (0,0)->(7,7)
The get_possible_moves function in Main.py removes the rest of the illegal moves and covers castling.'''


# pawn_move_white(index, piece_loc, white_move, last_move)
# index = chosen white pawn location to search for moves at
# piece_loc = piece location dictionary
# white_move = bool for whose turn it is: True = white, False = black
# last_move = the last user inputted move played on the board. Used for En Passant testing
# Finds all moves for the pawn, given if the pawn is attacking, moving forward, or blocked on the (0,0) -> (7,7) grid
# Covers En Passant
# Does not remove all illegal moves
def pawn_move_white(index: (int, int), piece_loc: dict[(int, int), Pieces], last_move: Mo.Move = None) \
        -> list[(int, int)]:
    pos_moves = []
    x, y = index
    if x == 7 or x == 0:
        return []
    if piece_loc[(x + 1, y)] == ' ':
        pos_moves.append((x + 1, y))
    if x == 1:
        if piece_loc[(x + 1, y)] == ' ' and piece_loc[(x + 2, y)] == ' ':
            pos_moves.append((x + 2, y))
    if x == 4:
        if last_move:
            if last_move.piece_name == 'black_pawn':
                if last_move.start_index[0] == 6 and last_move.end_index[0] == 4 \
                        and (last_move.end_index[1] == y + 1 or last_move.end_index[1] == y - 1):
                    pos_moves.append((last_move.start_index[0] - 1, last_move.start_index[1]))
    if y == 0:
        if piece_loc[(x + 1, y + 1)] != ' ':
            if piece_loc[(x + 1, y + 1)].color == 'b':
                pos_moves.append((x + 1, y + 1))
    elif y == 7:
        if piece_loc[(x + 1, y - 1)] != ' ':
            if piece_loc[(x + 1, y - 1)].color == 'b':
                pos_moves.append((x + 1, y - 1))
    else:
        if piece_loc[(x + 1, y + 1)] != ' ':
            if piece_loc[(x + 1, y + 1)].color == 'b':
                pos_moves.append((x + 1, y + 1))
        if piece_loc[(x + 1, y - 1)] != ' ':
            if piece_loc[(x + 1, y - 1)].color == 'b':
                pos_moves.append((x + 1, y - 1))
    return pos_moves


# pawn_move_black(index, piece_loc, white_move, last_move)
# index = chosen black pawn location to search for moves at
# piece_loc = piece location dictionary
# white_move = bool for whose turn it is: True = white, False = black
# last_move = the last user inputted move played on the board. Used for En Passant testing
# Finds all moves for the pawn, given if the pawn is attacking, moving forward, or blocked on the (0,0) -> (7,7) grid
# Covers En Passant
# Does not remove all illegal moves
def pawn_move_black(index: (int, int), piece_loc: dict[(int, int), Pieces], last_move: Mo.Move = None) \
        -> list[(int, int)]:
    pos_moves = []
    x, y = index
    if x == 7 or x == 0:
        return []
    if piece_loc[(x - 1, y)] == ' ':
        pos_moves.append((x - 1, y))
    if x == 6:
        if piece_loc[(x - 1, y)] == ' ' and piece_loc[(x - 2, y)] == ' ':
            pos_moves.append((x - 2, y))
    if x == 3:
        if last_move:
            if last_move.piece_name == 'white_pawn':
                if last_move.start_index[0] == 1 and last_move.end_index[0] == 3 \
                        and (last_move.end_index[1] == y + 1 or last_move.end_index[1] == y - 1):
                    pos_moves.append((last_move.start_index[0] + 1, last_move.start_index[1]))
    if y == 0:
        if piece_loc[(x - 1, y + 1)] != ' ':
            if piece_loc[(x - 1, y + 1)].color == 'w':
                pos_moves.append((x - 1, y + 1))
    elif y == 7:
        if piece_loc[(x - 1, y - 1)] != ' ':
            if piece_loc[(x - 1, y - 1)].color == 'w':
                pos_moves.append((x - 1, y - 1))
    else:
        if piece_loc[(x - 1, y + 1)] != ' ':
            if piece_loc[(x - 1, y + 1)].color == 'w':
                pos_moves.append((x - 1, y + 1))
        if piece_loc[(x - 1, y - 1)] != ' ':
            if piece_loc[(x - 1, y - 1)].color == 'w':
                pos_moves.append((x - 1, y - 1))
    return pos_moves


# knight_move(index, piece_loc, white_move)
# index = chosen knight location to search for moves at
# piece_loc = piece location dictionary
# white_move = bool for whose turn it is: True = white, False = black
# Finds all moves for the knight within the (0,0) -> (7,7) grid.
# Then removes pieces of the same color from the move list
# Does not remove all illegal moves
def knight_move(index: (int, int), piece_loc: dict[(int, int), Pieces], white_move: bool) -> list[(int, int)]:
    x, y = index
    moves = []
    if x + 2 < 8:
        if y - 1 >= 0:
            moves.append((x + 2, y - 1))
        if y + 1 < 8:
            moves.append((x + 2, y + 1))
    if x - 2 >= 0:
        if y - 1 >= 0:
            moves.append((x - 2, y - 1))
        if y + 1 < 8:
            moves.append((x - 2, y + 1))
    if y + 2 < 8:
        if x - 1 >= 0:
            moves.append((x - 1, y + 2))
        if x + 1 < 8:
            moves.append((x + 1, y + 2))
    if y - 2 >= 0:
        if x - 1 >= 0:
            moves.append((x - 1, y - 2))
        if x + 1 < 8:
            moves.append((x + 1, y - 2))

    verified = []
    for move in moves:
        if piece_loc[move] != ' ':
            if white_move:
                if piece_loc[move].color == 'b':
                    verified.append(move)
            else:
                if piece_loc[move].color == 'w':
                    verified.append(move)
        else:
            verified.append(move)
    return verified


# bishop_move(index, piece_loc, white_move)
# index = chosen bishop location to search for moves at
# piece_loc = piece location dictionary
# white_move = bool for whose turn it is: True = white, False = black
# Finds all moves for the bishop, stops at pieces of the same color and first piece of the opposite color
# Does not remove all illegal moves
def bishop_move(index: (int, int), piece_loc: dict[(int, int), Pieces], white_move: bool) -> list[(int, int)]:
    x, y = index
    moves = []
    found_up_up = False
    found_down_down = False
    found_up_down = False
    found_down_up = False

    for i in range(8):
        if x + i < 8 and y + i < 8 and not found_up_up:
            move = (x + i, y + i)
            if move not in moves and move != index:
                if piece_loc[move] == ' ':
                    moves.append(move)
                else:
                    found_up_up = True
                    if white_move:
                        if piece_loc[move].color == 'b':
                            moves.append(move)
                    else:
                        if piece_loc[move].color == 'w':
                            moves.append(move)
        if x - i >= 0 and y + i < 8 and not found_down_up:
            move = (x - i, y + i)
            if move not in moves and move != index:
                if piece_loc[move] == ' ':
                    moves.append(move)
                else:
                    found_down_up = True
                    if white_move:
                        if piece_loc[move].color == 'b':
                            moves.append(move)
                    else:
                        if piece_loc[move].color == 'w':
                            moves.append(move)
        if x + i < 8 and y - i >= 0 and not found_up_down:
            move = (x + i, y - i)
            if move not in moves and move != index:
                if piece_loc[move] == ' ':
                    moves.append(move)
                else:
                    found_up_down = True
                    if white_move:
                        if piece_loc[move].color == 'b':
                            moves.append(move)
                    else:
                        if piece_loc[move].color == 'w':
                            moves.append(move)
        if x - i >= 0 and y - i >= 0 and not found_down_down:
            move = (x - i, y - i)
            if move not in moves and move != index:
                if piece_loc[move] == ' ':
                    moves.append(move)
                else:
                    found_down_down = True
                    if white_move:
                        if piece_loc[move].color == 'b':
                            moves.append(move)
                    else:
                        if piece_loc[move].color == 'w':
                            moves.append(move)
    return moves


# rook_move(index, piece_loc, white_move)
# index = chosen rook location to search for moves at
# piece_loc = piece location dictionary
# white_move = bool for whose turn it is: True = white, False = black
# Finds all moves for the rook that do not go beyond the first piece of the opposite color or pieces of its own color
# Does not remove all illegal moves
def rook_move(index: (int, int), piece_loc: dict[(int, int), Pieces], white_move: bool) -> list[(int, int)]:
    x, y = index
    dist_x_0 = x - 0
    dist_x_7 = 7 - x
    dist_y_0 = y - 0
    dist_y_7 = 7 - y
    moves = []

    not_found = True
    if x - 1 >= 0:
        for i in range(dist_x_0):
            if not_found:
                if piece_loc[(dist_x_0 - i - 1, y)] == ' ':
                    moves.append((dist_x_0 - i - 1, y))
                else:
                    not_found = False
                    if white_move:
                        if piece_loc[(dist_x_0 - i - 1, y)].color == 'b':
                            moves.append((dist_x_0 - i - 1, y))
                    else:
                        if piece_loc[(dist_x_0 - i - 1, y)].color == 'w':
                            moves.append((dist_x_0 - i - 1, y))

    not_found = True
    if x + 1 <= 7:
        for i in range(dist_x_7):
            if not_found:
                if piece_loc[(x + i + 1, y)] == ' ':
                    moves.append((x + i + 1, y))
                else:
                    not_found = False
                    if white_move:
                        if piece_loc[(x + i + 1, y)].color == 'b':
                            moves.append((x + i + 1, y))
                    else:
                        if piece_loc[(x + i + 1, y)].color == 'w':
                            moves.append((x + i + 1, y))

    not_found = True
    if y - 1 >= 0:
        for i in range(dist_y_0):
            if not_found:
                if piece_loc[(x, dist_y_0 - i - 1)] == ' ':
                    moves.append((x, dist_y_0 - i - 1))
                else:
                    not_found = False
                    if white_move:
                        if piece_loc[(x, dist_y_0 - i - 1)].color == 'b':
                            moves.append((x, dist_y_0 - i - 1))
                    else:
                        if piece_loc[(x, dist_y_0 - i - 1)].color == 'w':
                            moves.append((x, dist_y_0 - i - 1))

    not_found = True
    if y + 1 <= 7:
        for i in range(dist_y_7):
            if not_found:
                if piece_loc[(x, y + i + 1)] == ' ':
                    moves.append((x, y + i + 1))
                else:
                    not_found = False
                    if white_move:
                        if piece_loc[(x, y + i + 1)].color == 'b':
                            moves.append((x, y + i + 1))
                    else:
                        if piece_loc[(x, y + i + 1)].color == 'w':
                            moves.append((x, y + i + 1))

    return moves


# queen_move(index, piece_loc, white_move)
# index = chosen queen location to search for moves at
# piece_loc = piece location dictionary
# white_move = bool for whose turn it is: True = white, False = black
# Finds all moves for the queen, using the rook move and bishop move algorithms
# Does not remove all illegal moves
def queen_move(index: (int, int), piece_loc: dict[(int, int), Pieces], white_move: bool) -> list[(int, int)]:
    moves = rook_move(index, piece_loc, white_move)
    moves += bishop_move(index, piece_loc, white_move)
    return moves


# king_move(index, piece_loc, white_move)
# index = chosen king location to search for moves at
# piece_loc = piece location dictionary
# white_move = bool for whose turn it is: True = white, False = black
# Finds all moves for the king, then removes moves outside of the (0,0) -> (7,7) grid
# Also removes pieces of the same color in the radius
# Does not remove all illegal moves
def king_move(index: (int, int), piece_loc: dict[(int, int), Pieces], white_move: bool) -> list[(int, int)]:
    x, y = index
    moves = [(x + 1, y + 1), (x + 1, y - 1), (x - 1, y + 1), (x - 1, y - 1), (x + 1, y), (x - 1, y), (x, y + 1),
             (x, y - 1)]

    test_moves = []
    for move in moves:
        new_x, new_y = move
        if 7 >= new_x >= 0 and 7 >= new_y >= 0:
            if piece_loc[move] == ' ':
                test_moves.append(move)
            else:
                if white_move:
                    if piece_loc[move].color == 'b':
                        test_moves.append(move)
                else:
                    if piece_loc[move].color == 'w':
                        test_moves.append(move)
    return test_moves


# check_king_attacked(piece_loc, index_king, is_white)
# piece_loc = piece location dictionary
# index_king = location of the king in question, either black or white
# is white = bool for whose turn it is: True = white, False = black
# Checks the king's safety by calculating piece move functions from the king's location.
# Example: The white king finds all black piece's attacking it by running it through the white piece
# move functions that output black pieces and empty squares. Then it filters out the empty squares.
# if there are remaining pieces, they have to be attacking the king
# Returns: list of all attackers on the king
def check_king_attacked(piece_loc: dict[(int, int), Pieces], index_king: (int, int), is_white: bool) \
        -> list[(int, int)]:
    knight_possibles = knight_move(index_king, piece_loc, is_white)
    rook_possibilities = rook_move(index_king, piece_loc, is_white)
    bishop_possibles = bishop_move(index_king, piece_loc, is_white)
    king_possibles = king_move(index_king, piece_loc, is_white)

    attackers = []
    for move in knight_possibles:
        if piece_loc[move] != ' ':
            if 'knight' in piece_loc[move].name:
                attackers.append(move)
    for move in rook_possibilities:
        if piece_loc[move] != ' ':
            if 'rook' in piece_loc[move].name or 'queen' in piece_loc[move].name:
                attackers.append(move)
    for move in bishop_possibles:
        if piece_loc[move] != ' ':
            if 'bishop' in piece_loc[move].name or 'queen' in piece_loc[move].name:
                attackers.append(move)
            if 'pawn' in piece_loc[move].name:
                if not is_white:
                    pawn_pos = pawn_move_white(move, piece_loc)
                else:
                    pawn_pos = pawn_move_black(move, piece_loc)
                if index_king in pawn_pos:
                    attackers.append(move)
    for move in king_possibles:
        if piece_loc[move] != ' ':
            if 'king' in piece_loc[move].name:
                attackers.append(move)

    return attackers
