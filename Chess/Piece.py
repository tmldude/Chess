
class Pieces:
    def __int__(self, name, color, image, is_king = False):
        self.name = name
        self.color = color
        self.image = image
        self.is_king = is_king


    '''The individual piece functions output ALL possible moves on a 8x8 chess board for the piece at the 
    given index. This is a list:[(int,int)] or a list of move indexes. After, the are_moves_valid() function
    should be ran to remove all illegal moves that may jump over pieces of go past them.'''


    '''Pawn move function: takes in index of selected pawn outputs possible pawn moves'''
    def pawn_move(self, index: (int, int)) -> list[(int, int)]:
        raise NameError("Unimplemented")

    '''Knight move function: takes in index of selected knight and outputs possible knight moves'''
    def knight_move(self, index: (int, int)) -> list[(int, int)]:
        raise NameError("Unimplemented")

    '''Bishop move function: takes in index of selected bishop and outputs possible bishop moves'''
    def bishop_move(self, index: (int, int)) -> list[(int, int)]:
        raise NameError("Unimplemented")

    '''Rook move function: takes in index of selected rook and outputs possible rook moves'''
    def rook_move(self, index: (int, int)) -> list[(int, int)]:
        raise NameError("Unimplemented")

    '''Queen move function: takes in index of selected queen and outputs possible queen moves'''
    def queen_move(self, index: (int, int)) -> list[(int, int)]:
        raise NameError("Unimplemented")

    '''King move function: takes in index of selected king and outputs possible king moves'''
    def king_move(self, index: (int, int)) -> list[(int, int)]:
        raise NameError("Unimplemented")

    '''is_valid(index,moves,board): Takes in the index of the piece to be moved, the possible moves
     list[(int,int)] for a piece and tests the board to see if the possible_moves are valid. 
     This function eliminates moves that intersect with other pieces of the same color and the 
     squares after that intersection. Additionally, it stops at the first piece of the opposing color and
     eliminates the moves beyond this point'''
    def are_moves_valid(self, moves: list[(int, int)], board) -> list[(int,int)]:
        raise NameError("Unimplemented")



