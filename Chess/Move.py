
class Move:
    def __init__(self, piece_nam, start_index, end_index, capture):
        self.piece_name = piece_nam
        self.start_index = start_index
        self.end_index = end_index
        self.capture = capture

    def get_name(self):
        return self.piece_name
