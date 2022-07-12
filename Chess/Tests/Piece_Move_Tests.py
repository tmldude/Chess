import unittest

import Piece as Pi

from Main import piece_loc
from Main import pieces
from Main import get_possible_moves
from Main import validate_moves

class PieceMoveTests(unittest.TestCase):
    def test_start_pos_pawn_w(self):
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
                ans.sort()
                poss_moves.sort()
                self.assertEqual(poss_moves, ans)

    def test_start_pos_pawn_b(self):
        for i in range(0, 8):
            for j in range(0, 8):
                ans = []
                index = (i, j)
                poss_moves = Pi.pawn_move_black(index)
                if i == 6:
                    ans.append((i - 2, j))
                if j == 0:
                    ans.append((i - 1, j + 1))
                elif j == 7:
                    ans.append((i - 1, j - 1))
                else:
                    ans.append((i - 1, j - 1))
                    ans.append((i - 1, j + 1))
                ans.append((i - 1, j))
                if i == 0 or i == 7:
                    ans = []
                ans.sort()
                poss_moves.sort()
                self.assertEqual(poss_moves, ans)

    def test_start_bishop_pos(self):
        ans = [(2, 0), (1, 1), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7)]
        poss_moves = Pi.bishop_move((0, 2))
        ans.sort()
        poss_moves.sort()
        self.assertEqual(poss_moves, ans)

        ans = [(1, 6), (2, 7), (1, 4), (2, 3), (3, 2), (4, 1), (5, 0)]
        poss_moves = Pi.bishop_move((0, 5))
        ans.sort()
        poss_moves.sort()
        self.assertEqual(poss_moves, ans)

        ans = [(6, 1), (5, 0), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7)]
        poss_moves = Pi.bishop_move((7, 2))
        ans.sort()
        poss_moves.sort()
        self.assertEqual(poss_moves, ans)

        ans = [(6, 6), (5, 7), (6, 4), (5, 3), (4, 2), (3, 1), (2, 0)]
        poss_moves = Pi.bishop_move((7, 5))
        ans.sort()
        poss_moves.sort()
        self.assertEqual(poss_moves, ans)

    def test_start_knight_pos(self):
        ans = [(2, 0), (2, 2), (1, 3)]
        poss_moves = Pi.knight_move((0, 1))
        ans.sort()
        poss_moves.sort()
        self.assertEqual(poss_moves, ans)

        ans = [(1, 4), (2, 5), (2, 7)]
        poss_moves = Pi.knight_move((0, 6))
        ans.sort()
        poss_moves.sort()
        self.assertEqual(poss_moves, ans)

        ans = [(5, 0), (5, 2), (6, 3)]
        poss_moves = Pi.knight_move((7, 1))
        ans.sort()
        poss_moves.sort()
        self.assertEqual(poss_moves, ans)

        ans = [(6, 4), (5, 5), (5, 7)]
        poss_moves = Pi.knight_move((7, 6))
        ans.sort()
        poss_moves.sort()
        self.assertEqual(poss_moves, ans)

    def test_start_rook_pos(self):
        ans = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
               (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]
        poss_moves = Pi.rook_move((0, 0))
        poss_moves.sort()
        ans.sort()
        self.assertEqual(poss_moves, ans)

        ans = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),
               (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7)]
        poss_moves = Pi.rook_move((0, 7))
        ans.sort()
        poss_moves.sort()
        self.assertEqual(poss_moves, ans)

        ans = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0),
               (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7)]
        poss_moves = Pi.rook_move((7, 0))
        ans.sort()
        poss_moves.sort()
        self.assertEqual(poss_moves, ans)

        ans = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7),
               (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6)]
        poss_moves = Pi.rook_move((7, 7))
        ans.sort()
        poss_moves.sort()
        self.assertEqual(poss_moves, ans)

    def test_queen_start_pos(self):
        ans = [(0, 0), (0, 1), (0, 2), (0, 4), (0, 5), (0, 6), (0, 7),
               (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3),
               (1, 2), (2, 1), (3, 0), (1, 4), (2, 5), (3, 6), (4, 7)]
        poss_moves = Pi.queen_move((0, 3))
        poss_moves.sort()
        ans.sort()
        self.assertEqual(poss_moves, ans)

        ans = [(7, 0), (7, 1), (7, 2), (7, 4), (7, 5), (7, 6), (7, 7),
               (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3),
               (6, 2), (5, 1), (4, 0), (6, 4), (5, 5), (4, 6), (3, 7)]
        poss_moves = Pi.queen_move((7, 3))
        ans.sort()
        poss_moves.sort()
        self.assertEqual(poss_moves, ans)

    def test_king_start_pos(self):
        ans = [(0, 3), (0, 5), (1, 3), (1, 4), (1, 5)]
        poss_moves = Pi.king_move((0, 4))
        poss_moves.sort()
        ans.sort()
        self.assertEqual(poss_moves, ans)

        ans = [(7, 3), (7, 5), (6, 3), (6, 4), (6, 5)]
        poss_moves = Pi.king_move((7, 4))
        poss_moves.sort()
        ans.sort()
        self.assertEqual(poss_moves, ans)

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
                elif piece_loc[location].name == "black_knight" or piece_loc[location].name == "white_knight":
                    if location == (0, 1):
                        self.assertEqual(val_ans.sort(), [(2, 0), (2, 2)].sort())
                    elif location == (0, 6):
                        self.assertEqual(val_ans.sort(), [(1, 4), (2, 5)].sort())

                    elif location == (7, 1):
                        self.assertEqual(val_ans.sort(), [(5, 0), (5, 2)].sort())
                    else:
                        self.assertEqual(val_ans.sort(), [(6, 4), (5, 5)].sort())
                else:
                    #self.assertEqual(val_ans, [])
                    pass


if __name__ == '__main__':
    unittest.main()
