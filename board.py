

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.bd = [["O"] * width for i in range(height)]
        
    def displayBoard(self):
        for row in self.bd:
            for element in row:
                print(str(element),end=' ')
            print()
            
    def emptyBoard(self):
        for i in range(self.height):
            for j in range(len(self.bd[0])):
                self.bd[i][j] = "*"
                
    def is_full(self):
        for row in self.bd:
            for element in row:
                if element == "O":
                    return False
        return True
    
    def add_piece(self, piece_string, column):
        if type(column) != int or int(column) > self.width or int(column) <= 0:
            raise ValueError("Invalid Column")
        column = int(column)
        for i in range(self.height):
            if self.bd[i][column] != "O":
                self.bd[i-1][column] = str(piece_string)
                self.displayBoard()
                return True
        raise ValueError("Column Is Full")
        return False
        
    
        
    
    
                
    
            
        
        
        
        
        
if __name__ == "__main__":
    eyy = Board(7, 5)
    eyy.displayBoard()
    eyy.add_piece("*", 3)
    eyy.add_piece("*", 3)