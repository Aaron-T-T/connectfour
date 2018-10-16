

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.bd = [["O"] * width for i in range(height)]
        
    def displayBoard(self):
        print()
        print()
        for row in self.bd:
            for element in row:
                print(str(element),end=' ')
            print()
        print()
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
            print("Invalid Column")
            return False
        column = int(column)
        for i in range((len(self.bd)-1),-1,-1):
            if self.bd[i][column] == "O":
                self.bd[i][column] = str(piece_string)
                self.displayBoard()
                return True
        else:
            print("Column is Full")
            return False
        
    def detect_win(self):
        #Detect win horizontally
        samePieceCount = 0
        previousPiece = ""
        for i in range(len(self.bd)-1, -1, -1):
            for j in range(len(self.bd[0])):
                if self.bd[i][j] == previousPiece and self.bd[i][j] != "O":
                    samePieceCount += 1
                else:
                    samePieceCount = 1
                    previousPiece = str(self.bd[i][j])
                if samePieceCount == 4:
                    return True
            samePieceCount = 0
            previousPiece = ""
        #Detect win vertically
        for i in range(len(self.bd[0])):
            for j in range(len(self.bd)-1, -1, -1):
                if self.bd[j][i] == previousPiece and self.bd[j][i] != "O":
                    samePieceCount += 1
                else:
                    samePieceCount = 1
                    previousPiece = str(self.bd[j][i])
                if samePieceCount == 4:
                    return True
            samePieceCount = 0
            previousPiece = ""
        #Detect win diagonally
        return False #Dummy Boi
                    
        
        

if __name__ == "__main__":
    eyy = Board(7, 6)
    eyy.displayBoard()
    eyy.add_piece("*", 1)
    eyy.add_piece("*", 1)
    eyy.add_piece("*", 1)
    eyy.add_piece("*", 2)
    eyy.add_piece("*",1)
    print(eyy.detect_win())