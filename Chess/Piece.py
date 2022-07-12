class Pieces:
    def __init__(self, name, color, image, is_king=False):
        self.name = name
        self.color = color
        self.image = image
        self.is_king = is_king

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
def pawn_move_white(index: (int, int)) -> list[(int, int)]:
    pos_moves = []
    x, y = index
    if x == 7 or x == 0:
        return []
    pos_moves.append((x + 1, y))
    if x == 1:
        pos_moves.append((x + 2, y))
    if y == 0:
        pos_moves.append((x + 1, y + 1))
    elif y == 7:
        pos_moves.append((x + 1, y - 1))
    else:
        pos_moves.append((x + 1, y + 1))
        pos_moves.append((x + 1, y - 1))
    return pos_moves

# Pawn move function: for black pieces takes in index of selected pawn outputs possible pawn moves
def pawn_move_black(index: (int, int)) -> list[(int, int)]:
    pos_moves = []
    x, y = index
    if x == 7 or x == 0:
        return []
    pos_moves.append((x - 1, y))
    if x == 6:
        pos_moves.append((x - 2, y))
    if y == 0:
        pos_moves.append((x - 1, y + 1))
    elif y == 7:
        pos_moves.append((x - 1, y - 1))
    else:
        pos_moves.append((x - 1, y + 1))
        pos_moves.append((x - 1, y - 1))
    return pos_moves

# Knight move function: takes in index of selected knight and outputs possible knight moves
def knight_move(index: (int, int)) -> list[(int, int)]:
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

    return moves

# Bishop move function: takes in index of selected bishop and outputs possible bishop moves
def bishop_move(index: (int, int)) -> list[(int, int)]:
    x, y = index
    moves = []
    for i in range(8):
        if x + i < 8 and y + i < 8:
            if (x + i, y + i) not in moves and (x + i, y + i) != index:
                moves.append((x + i, y + i))
        if x - i >= 0 and y + i < 8:
            if (x - i, y + i) not in moves and (x - i, y + i) != index:
                moves.append((x - i, y + i))
        if x + i < 8 and y - i >= 0:
            if (x + i, y - i) not in moves and (x + i, y - i) != index:
                moves.append((x + i, y - i))
        if x - i >= 0 and y - i >= 0:
            if (x - i, y - i) not in moves and (x - i, y - i) != index:
                moves.append((x - i, y - i))
    return moves

# Rook move function: takes in index of selected rook and outputs possible rook moves
def rook_move(index: (int, int)) -> list[(int, int)]:
    x, y = index
    moves = []
    for i in range(8):
        if (i, y) != index:
            moves.append((i, y))
        if (x, i) != index:
            moves.append((x, i))
    return moves

# Queen move function: takes in index of selected queen and outputs possible queen moves
def queen_move(index: (int, int)) -> list[(int, int)]:
    moves = rook_move(index)
    moves += bishop_move(index)
    return moves


# King move function: takes in index of selected king and outputs possible king moves
def king_move(index: (int, int)) -> list[(int, int)]:
    x, y = index
    moves = [(x + 1, y + 1), (x + 1, y - 1), (x - 1, y + 1), (x - 1, y - 1), (x + 1, y), (x - 1, y), (x, y + 1),
             (x, y - 1)]

    test_moves = []
    for move in moves:
        new_x, new_y = move
        if 7 >= new_x >= 0 and 7 >= new_y >= 0:
            test_moves.append(move)

    return test_moves
