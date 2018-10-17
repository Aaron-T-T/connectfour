

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.bd = [[" "] * width for i in range(height)]
        
    def disp_board(self):
        print()
        topString  = ""
        countString = ""
        for i in range(len(self.bd[0])):
            topString += "- "
        print(topString)
        topString = ""
        for row in self.bd:
            for element in row:
                print(str(element),end=' ')
            print()
        for i in range(1,len(self.bd[0])+1):
            topString += "- "
        print(topString)
        for i in range(1,len(self.bd[0])+1):
            countString += str(i) + " "
        print(countString)
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
            if self.bd[i][column-1] == " ":
                self.bd[i][column-1] = str(piece_string)
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
                if self.bd[i][j] == previousPiece and self.bd[i][j] != " ":
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
                if self.bd[j][i] == previousPiece and self.bd[j][i] != " ":
                    samePieceCount += 1
                else:
                    samePieceCount = 1
                    previousPiece = str(self.bd[j][i])
                if samePieceCount == 4:
                    return True
            samePieceCount = 0
            previousPiece = ""
        #Detect win diagonally left-right
        for i in range(len(self.bd)-1, len(self.bd)-4, -1):
            for j in range(3):
                if self.bd[i][j] == previousPiece and self.bd[i][j] != " ":
                    samePieceCount += 1
                else:
                    samePieceCount = 1
                    previousPiece = str(self.bd[i][j])
                if samePieceCount == 4:
                    return True
            samePieceCount = 0
            previousPiece = ""
        #Detect win diagonally right-left
        for i in range(3):
            for j in range(len(self.bd[0])-1, len(self.bd[0])-4, -1):
                if self.bd[i][j] == previousPiece and self.bd[i][j] != " ":
                    samePieceCount += 1
                else:
                    samePieceCount = 1
                    previousPiece = str(self.bd[i][j])
                if samePieceCount == 4:
                    return True
            samePieceCount = 0
            previousPiece = ""
        return False #Dummy Boi
                    
        
        

if __name__ == "__main__":
    eyy = Board(7, 6)
    eyy.disp_board()
    eyy.add_piece("*",1)
    eyy.disp_board()
    print(eyy.detect_win())