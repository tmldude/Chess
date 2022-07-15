
class Move:
    """
    Move:
    :param piece_name: name of the piece that was moved
    :param start_index: the starting index of the moved piece
    :param end_index: the ending index and current location of the moved piece
    :param capture: bool stating whether a capture took place during this move
    """
    def __init__(self, piece_name, start_index, end_index, capture, en_passant=False, castling=False):
        self.piece_name = piece_name
        self.start_index = start_index
        self.end_index = end_index
        self.capture = capture
        self.en_passant = en_passant
        self.castling = castling

    def get_name(self):
        return self.piece_name
