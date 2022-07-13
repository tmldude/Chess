import unittest

import Piece as Pi

from Main import piece_loc
from Main import empty_piece_loc
from Main import pieces
from Main import get_possible_moves
from Main import validate_moves
from Main import empty_board

class AdvancedPieceTests(unittest.TestCase):
    def test_pawn_in_center_with_pawn_in_front(self):
        new_piece_loc = empty_piece_loc
        white_pawn = pieces['white_pawn']
        black_pawn = pieces['black_pawn']
        index = (3, 2)
        new_piece_loc[index] = white_pawn
        new_piece_loc[(4, 2)] = black_pawn
        poss_moves = Pi.pawn_move_white(index, new_piece_loc)
        ans = []
        self.assertEqual(poss_moves, ans)
        empty_board(new_piece_loc)


if __name__ == '__main__':
    unittest.main()
