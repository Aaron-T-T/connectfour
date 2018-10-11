

class Board:
    def __init__(self, width, height):
        self.bd = [["*"] * width for i in range(height)]
        