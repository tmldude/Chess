import unittest

import Piece as Pi

from Main import piece_loc
from Main import pieces
from Main import get_possible_moves
from Main import validate_moves

class PieceMoveTests(unittest.TestCase):
    def test_star_pos_pawn_w(self):
        for i in range(0, 8):
            for j in range(0, 8):
                ans = []
                index = (i, j)
                poss_moves = Pi.pawn_move_white(index)
                if i == 1:
                    ans.append((i + 2, j))
                if j == 0:
                    ans.append((i + 1, j + 1))
                elif j == 7:
                    ans.append((i + 1, j - 1))
                else:
                    ans.append((i + 1, j - 1))
                    ans.append((i + 1, j + 1))
                ans.append((i + 1, j))
                if i == 0 or i == 7:
                    ans = []
                self.assertEqual(poss_moves.sort(), ans.sort())

    def test_start_pos_of_board(self):
        for location in piece_loc:
            x, y = location
            if piece_loc[location] != ' ':
                ans = get_possible_moves(location)
                val_ans = validate_moves(ans, location, True)
                if piece_loc[location].name == "white_pawn":
                    self.assertEqual(val_ans.sort(), [(x + 1, y), (x + 2, y)].sort())
                elif piece_loc[location].name == "black_pawn":
                    self.assertEqual(val_ans.sort(), [(x - 1, y), (x - 2, y)].sort())
                else:
                    self.assertEqual(val_ans, [])


if __name__ == '__main__':
    unittest.main()
