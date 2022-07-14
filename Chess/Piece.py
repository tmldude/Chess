class Pieces:
    def __init__(self, name, color, image, is_king=False):
        self.name = name
        self.color = color
        self.image = image
        self.is_king = is_king
        self.has_moved = False

    ''' I looked into it and overloaded contractors are not a thing in Python
    def __init__(self, piece):  # Copy constructor
        self.name = piece.name
        self.color = piece.color
        self.image = piece.image
        self.is_king = piece.is_king

    def __init__(self):  # Default constructor
        self.name = None
        self.color = None
        self.image = None
        self.is_king = None
        self.active_image = None
    '''


'''The individual piece functions output ALL possible moves on a 8x8 chess board for the piece at the 
given index. This is a list:[(int,int)] or a list of move indexes. After, the are_moves_valid() function
should be ran to remove all illegal moves that may jump over pieces of go past them.'''

# Pawn move function: for white pieces takes in index of selected pawn outputs possible pawn moves'''
def pawn_move_white(index: (int, int), piece_loc: dict[(int, int), Pieces]) -> list[(int, int)]:
    pos_moves = []
    x, y = index
    if x == 7 or x == 0:
        return []
    if piece_loc[(x + 1, y)] == ' ':
        pos_moves.append((x + 1, y))
    if x == 1:
        if piece_loc[(x + 1, y)] == ' ' and piece_loc[(x + 2, y)] == ' ':
            pos_moves.append((x + 2, y))
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

# Pawn move function: for black pieces takes in index of selected pawn outputs possible pawn moves
def pawn_move_black(index: (int, int), piece_loc: dict[(int, int), Pieces]) -> list[(int, int)]:
    pos_moves = []
    x, y = index
    if x == 7 or x == 0:
        return []
    if piece_loc[(x - 1, y)] == ' ':
        pos_moves.append((x - 1, y))
    if x == 6:
        if piece_loc[(x - 1, y)] == ' ' and piece_loc[(x - 2, y)] == ' ':
            pos_moves.append((x - 2, y))
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

# Knight move function: takes in index of selected knight and outputs possible knight moves
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

# Bishop move function: takes in index of selected bishop and outputs possible bishop moves
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

# Rook move function: takes in index of selected rook and outputs possible rook moves
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

# Queen move function: takes in index of selected queen and outputs possible queen moves
def queen_move(index: (int, int), piece_loc: dict[(int, int), Pieces], white_move: bool) -> list[(int, int)]:
    moves = rook_move(index, piece_loc, white_move)
    moves += bishop_move(index, piece_loc, white_move)
    return moves


# King move function: takes in index of selected king and outputs possible king moves
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


# This function may handle checks? Note sure yet
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
