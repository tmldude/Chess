import unittest

import Piece as Pi

class PawnMoveTest(unittest.TestCase):
    def test_star_pos_pawn_w(self):
        for i in range(1, 7):
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
                self.assertEqual(poss_moves.sort(), ans.sort())

    def test_star_pos_pawn_b(self):
        raise NameError("Unimplemented")


# def test_anywhere_pawn_w_1(self):
# self.assertEqual(poss_moves, [(3, 1)])
if __name__ == '__main__':
    unittest.main()
