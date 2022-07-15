import unittest

import Piece as Pi
import Move as Mo

from Main import piece_loc
from Main import empty_piece_loc
from Main import pieces
from Main import get_possible_moves
from Main import check_if_mate
from Main import empty_board

class AdvancedPieceTests(unittest.TestCase):
    def test_pawn_in_center_with_pawn_in_front(self):
        new_piece_loc = empty_piece_loc.copy()
        new_piece_loc[(3, 2)] = pieces['white_pawn']
        new_piece_loc[(4, 2)] = pieces['black_pawn']
        pos_moves_white = Pi.pawn_move_white((3, 2), new_piece_loc)
        pos_moves_black = Pi.pawn_move_black((4, 2), new_piece_loc)
        self.assertEqual(pos_moves_white, [])
        self.assertEqual(pos_moves_black, [])

        new_piece_loc[(3, 3)] = pieces['white_pawn']
        new_piece_loc[(4, 3)] = pieces['black_pawn']
        pos_moves_white = Pi.pawn_move_white((3, 2), new_piece_loc)
        pos_moves_black = Pi.pawn_move_black((4, 2), new_piece_loc)
        self.assertEqual(pos_moves_white, [(4, 3)])
        self.assertEqual(pos_moves_black, [(3, 3)])

        new_piece_loc[(3, 1)] = pieces['white_pawn']
        new_piece_loc[(4, 1)] = pieces['black_pawn']
        pos_moves_white = (Pi.pawn_move_white((3, 2), new_piece_loc))
        pos_moves_black = (Pi.pawn_move_black((4, 2), new_piece_loc))
        pos_moves_white.sort()
        pos_moves_black.sort()
        w_ans = [(4, 3), (4, 1)]
        b_ans = [(3, 3), (3, 1)]
        w_ans.sort()
        b_ans.sort()
        self.assertEqual(pos_moves_white, w_ans)
        self.assertEqual(pos_moves_black, b_ans)

        # En Passant test
        new_piece_loc[(4, 1)] = new_piece_loc[(3, 2)]
        new_piece_loc[(3, 2)] = ' '
        new_piece_loc[(4, 0)] = pieces['black_pawn']
        pos_moves_white = Pi.pawn_move_white((4, 1), new_piece_loc, Mo.Move('black_pawn', (6, 0), (4, 0), False))
        w_ans = [(5, 1), (5, 0)]
        self.assertEqual(pos_moves_white, w_ans)

    def test_rook_movement(self):
        new_piece_loc = empty_piece_loc.copy()
        new_piece_loc[(3, 2)] = pieces['white_rook']
        new_piece_loc[(3, 1)] = pieces['white_pawn']
        new_piece_loc[(3, 3)] = pieces['white_pawn']
        new_piece_loc[(2, 2)] = pieces['white_pawn']
        new_piece_loc[(4, 2)] = pieces['white_pawn']
        pos_moves = Pi.rook_move((3, 2), new_piece_loc, True)
        self.assertEqual(pos_moves, [])

        new_piece_loc[(2, 2)] = ' '
        pos_moves = Pi.rook_move((3, 2), new_piece_loc, True)
        pos_moves.sort()
        ans = [(2, 2), (1, 2), (0, 2)]
        ans.sort()
        self.assertEqual(pos_moves, ans)

        new_piece_loc[(3, 3)] = ' '
        pos_moves = Pi.rook_move((3, 2), new_piece_loc, True)
        pos_moves.sort()
        ans = [(2, 2), (1, 2), (0, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7)]
        ans.sort()
        self.assertEqual(pos_moves, ans)

        new_piece_loc[(3, 1)] = ' '
        pos_moves = Pi.rook_move((3, 2), new_piece_loc, True)
        pos_moves.sort()
        ans = [(2, 2), (1, 2), (0, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 1), (3, 0)]
        ans.sort()
        self.assertEqual(pos_moves, ans)

        new_piece_loc[(4, 2)] = ' '
        pos_moves = Pi.rook_move((3, 2), new_piece_loc, True)
        pos_moves.sort()
        ans = [(2, 2), (1, 2), (0, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 1), (3, 0), (4, 2),
               (5, 2), (6, 2), (7, 2)]
        ans.sort()
        self.assertEqual(pos_moves, ans)

        new_piece_loc[(3, 1)] = pieces['black_pawn']
        new_piece_loc[(3, 3)] = pieces['black_pawn']
        new_piece_loc[(2, 2)] = pieces['black_pawn']
        new_piece_loc[(4, 2)] = pieces['black_pawn']
        pos_moves = Pi.rook_move((3, 2), new_piece_loc, True)
        pos_moves.sort()
        ans = [(2, 2), (3, 3), (3, 1), (4, 2)]
        ans.sort()
        self.assertEqual(pos_moves, ans)

        new_piece_loc[(3, 1)] = ' '
        new_piece_loc[(3, 0)] = pieces['black_pawn']
        pos_moves = Pi.rook_move((3, 2), new_piece_loc, True)
        pos_moves.sort()
        ans = [(2, 2), (3, 3), (3, 1), (3, 0), (4, 2)]
        ans.sort()
        self.assertEqual(pos_moves, ans)

    def test_bishop_movement(self):
        new_piece_loc = empty_piece_loc.copy()
        new_piece_loc[(3, 2)] = pieces['white_bishop']
        new_piece_loc[(2, 3)] = pieces['white_pawn']
        new_piece_loc[(4, 3)] = pieces['white_pawn']
        new_piece_loc[(2, 1)] = pieces['white_pawn']
        new_piece_loc[(4, 1)] = pieces['white_pawn']
        pos_moves = Pi.bishop_move((3, 2), new_piece_loc, True)
        self.assertEqual(pos_moves, [])

        new_piece_loc[(2, 3)] = ' '
        pos_moves = Pi.bishop_move((3, 2), new_piece_loc, True)
        pos_moves.sort()
        ans = [(2, 3), (1, 4), (0, 5)]
        ans.sort()
        self.assertEqual(pos_moves, ans)

        new_piece_loc[(4, 3)] = ' '
        pos_moves = Pi.bishop_move((3, 2), new_piece_loc, True)
        pos_moves.sort()
        ans = [(2, 3), (1, 4), (0, 5), (4, 3), (5, 4), (6, 5), (7, 6)]
        ans.sort()
        self.assertEqual(pos_moves, ans)

        new_piece_loc[(2, 1)] = ' '
        pos_moves = Pi.bishop_move((3, 2), new_piece_loc, True)
        pos_moves.sort()
        ans = [(2, 3), (1, 4), (0, 5), (4, 3), (5, 4), (6, 5), (7, 6), (2, 1), (1, 0)]
        ans.sort()
        self.assertEqual(pos_moves, ans)

        new_piece_loc[(4, 1)] = ' '
        pos_moves = Pi.bishop_move((3, 2), new_piece_loc, True)
        pos_moves.sort()
        ans = [(2, 3), (1, 4), (0, 5), (4, 3), (5, 4), (6, 5), (7, 6), (2, 1), (1, 0), (4, 1), (5, 0)]
        ans.sort()
        self.assertEqual(pos_moves, ans)

        new_piece_loc[(2, 3)] = pieces['black_pawn']
        new_piece_loc[(4, 3)] = pieces['black_pawn']
        new_piece_loc[(2, 1)] = pieces['black_pawn']
        new_piece_loc[(4, 1)] = pieces['black_pawn']
        pos_moves = Pi.bishop_move((3, 2), new_piece_loc, True)
        pos_moves.sort()
        ans = [(2, 3), (4, 3), (2, 1), (4, 1)]
        ans.sort()
        self.assertEqual(pos_moves, ans)

        new_piece_loc[(4, 1)] = ' '
        new_piece_loc[(5, 0)] = pieces['black_pawn']
        pos_moves = Pi.bishop_move((3, 2), new_piece_loc, True)
        pos_moves.sort()
        ans = [(2, 3), (4, 3), (2, 1), (4, 1), (5, 0)]
        ans.sort()
        self.assertEqual(pos_moves, ans)

    def test_king_movement(self):
        new_piece_loc = empty_piece_loc.copy()
        new_piece_loc[(0, 0)] = pieces['white_king']
        new_piece_loc[(0, 7)] = pieces['black_rook']
        new_piece_loc[(7, 0)] = pieces['black_rook']

        pos_moves = get_possible_moves((0, 0), True, (0, 0), custom_piece_loc=new_piece_loc)
        self.assertEqual(pos_moves, [(1, 1)])

    def test_board_check_pos_1(self):
        test_board = piece_loc.copy()
        test_board[(3, 4)] = test_board[(1, 4)]
        test_board[(1, 4)] = ' '
        test_board[(4, 4)] = test_board[(6, 4)]
        test_board[(6, 4)] = ' '
        test_board[(4, 1)] = test_board[(0, 5)]
        test_board[(0, 5)] = ' '

        pos_moves = get_possible_moves((6, 3), False, (7, 4), custom_piece_loc=test_board)
        self.assertEqual(pos_moves, [])

        test_board[(6, 3)] = ' '
        for pi in test_board:
            if test_board[pi] != ' ':
                if test_board[pi].color == 'b':
                    if 'knight' in test_board[pi].name and pi == (7, 1):
                        pos_moves = get_possible_moves((7, 1), False, (7, 4), custom_piece_loc=test_board)
                        ans = [(5, 2), (6, 3)]
                    elif 'bishop' in test_board[pi].name and pi == (7, 2):
                        pos_moves = get_possible_moves((7, 2), False, (7, 4), custom_piece_loc=test_board)
                        ans = [(6, 3)]
                    elif 'queen' in test_board[pi].name and pi == (7, 3):
                        pos_moves = get_possible_moves((7, 3), False, (7, 4), custom_piece_loc=test_board)
                        ans = [(6, 3)]
                    elif 'king' in test_board[pi].name and pi == (7, 4):
                        pos_moves = get_possible_moves((7, 4), False, (7, 4), custom_piece_loc=test_board)
                        ans = [(6, 4)]
                    elif 'pawn' in test_board[pi].name and pi == (6, 2):
                        pos_moves = get_possible_moves((6, 2), False, (7, 4), custom_piece_loc=test_board)
                        ans = [(5, 2)]
                    else:
                        pos_moves = get_possible_moves(pi, False, (7, 4), custom_piece_loc=test_board)
                        ans = []
                    pos_moves.sort()
                    ans.sort()
                    self.assertEqual(pos_moves, ans)

    def test_check_mate(self):
        test_board = piece_loc.copy()
        test_board[(5, 6)] = test_board[(0, 3)]
        test_board[(0, 3)] = ' '
        test_board[(3, 2)] = test_board[(0, 5)]
        test_board[(0, 5)] = ' '
        self.assertTrue(check_if_mate((7, 4), True))
        self.assertFalse(check_if_mate((0, 4), True))


if __name__ == '__main__':
    unittest.main()
