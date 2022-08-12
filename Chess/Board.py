from Piece import Pieces

board = [['  ' for i in range(8)] for j in range(8)]

pieces = {}  # Dictionary to assign piece names to their piece objects
''' To access piece images call from dictionary pieces. Ex: pieces['white_king'] '''

piece_names = ['white_king', 'white_queen', 'white_rook', 'white_bishop', 'white_knight', 'white_pawn',
               'black_king', 'black_queen', 'black_rook', 'black_bishop', 'black_knight', 'black_pawn']

for p in piece_names:
    new_piece = Pieces(p, p[0], "piece_images" + "/" + p + ".png")
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
