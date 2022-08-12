import Move as Mo

def index_to_SAN(index: tuple[int, int]):
    """
    index_to_SAN(index)
    :param index: Integer tuple as recorded in pos_list
    :return: chess algebraic notation of a tile. Ex: (4, 4) -> e4
    """
    r, f = index
    san = str(chr(f + 97)) + str(r + 1)
    return san

def return_pgn_file(move_history: list[Mo.Move]) -> str:
    """
    return_pgn_file(move_history):
    :param move_history: list of Move class objects storing the history of move

    - Takes in the move list and uses the data to craft a string so the game can be easily retraced
    :return: Outputs a crafted string of the games move history
        Example:
        1. e4 e5 2. Nf3 Ne6 3. Bb5

    TODO: Checks, checkmate, and might be issue with generating PGN if white is last to move
    """
    pgn = ""
    if len(move_history) == 0:
        pgn = "no game"
    else:
        turns = len(move_history) // 2
        for i in range(1, turns+1):
            piece = ''
            capture = ''
            check = ''
            pgn += (str(i) + '. ')

            ''' White's move '''

            if move_history[(2*i)-2].piece_name[6] == 'p':
                piece = ''
            elif move_history[(2*i)-2].piece_name[6] == 'k':
                if move_history[(2*i)-2].piece_name[7] == 'n':
                    piece = 'N'
                else:
                    piece = 'K'
            else:
                piece = move_history[(2*i)-2].piece_name[6].capitalize()

            if not move_history[(2 * i) - 2].capture:
                capture = ''
            else:
                if move_history[(2 * i) - 2].piece_name[6] == 'p':
                    piece = index_to_SAN(move_history[(2 * i) - 1].start_index)[0]
                else:
                    pass
                capture = 'x'

            pgn += piece + capture + index_to_SAN(move_history[(2*i)-2].end_index) + move_history[(2*i)-2].gamestate \
                   + ' '

            ''' Black's move' '''

            if move_history[(2*i)-1].piece_name[6] == 'p':
                piece = ''
            elif move_history[(2*i)-1].piece_name[6] == 'k':
                if move_history[(2*i)-1].piece_name[7] == 'n':
                    piece = 'N'
                else:
                    piece = 'K'
            else:
                piece = move_history[(2*i)-1].piece_name[6].capitalize()

            if not move_history[(2 * i) - 1].capture:
                capture = ''
            else:
                if move_history[(2*i)-1].piece_name[6] == 'p':
                    piece = index_to_SAN(move_history[(2*i)-1].start_index)[0]
                else:
                    pass
                capture = 'x'

            pgn += piece + capture + index_to_SAN(move_history[(2*i)-1].end_index) + move_history[(2*i)-1].gamestate \
                   + ' '

    return pgn