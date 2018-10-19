

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[" "] * width for i in range(height)]
        
    def disp_board(self):
        topString  = ""
        countString = ""
        for i in range(len(self.board[0])*2):
            topString += "-"
        print(topString)
        topString = ""
        for row in self.board:
            for element in row:
                print(str(element),end=' ')
            print()
        for i in range(1,(((len(self.board[0])+1)*2)-1)):
            topString += "-"
        print(topString)
        for i in range(1,len(self.board[0])+1):
            countString += str(i) + " "
        print(countString)
            
    def emptyBoard(self):
        for i in range(self.height):
            for j in range(len(self.board[0])):
                self.board[i][j] = " "
                
    def is_full(self):
        for row in self.board:
            for element in row:
                if element == " ":
                    return False
        return True
    
    def add_piece(self, column, piece_string):
        counter = 0
        if type(column) != int or int(column) > self.width or int(column) <= 0:
            raise ValueError("Invalid Column")
        column = int(column)
        for i in range((len(self.board)-1),-1,-1):
            if self.board[i][column-1] == " ":
                self.board[i][column-1] = str(piece_string)
                break
            else:
                counter += 1
        if counter == len(self.board):
            raise ValueError("Column Full")
        
    def check_win(self):
        #Detect win horizontally
        samePieceCount = 0
        previousPiece = ""
        for i in range(len(self.board)-1, -1, -1):
            for j in range(len(self.board[0])):
                if self.board[i][j] == previousPiece and self.board[i][j] != " ":
                    samePieceCount += 1
                else:
                    samePieceCount = 1
                    previousPiece = str(self.board[i][j])
                if samePieceCount == 4:
                    return True
            samePieceCount = 0
            previousPiece = ""
        #Detect win vertically
        for i in range(len(self.board[0])):
            for j in range(len(self.board)-1, -1, -1):
                if self.board[j][i] == previousPiece and self.board[j][i] != " ":
                    samePieceCount += 1
                else:
                    samePieceCount = 1
                    previousPiece = str(self.board[j][i])
                if samePieceCount == 4:
                    return True
            samePieceCount = 0
            previousPiece = ""
        #Detect win diagonally left-right
        for i in range(3, self.height):
            for j in range(self.width-3):
                if self.board[i][j] == self.board[i-1][j+1] and self.board[i-1][j+1] and self.board[i-2][j+2] and self.board[i-2][j+2] == self.board[i-3][j+3] and self.board[i][j] != " ":
                    return True
        #Detect win diagonally right-left
        for i in range(self.width-3):
            for j in range(self.height-3):
                if self.board[i][j] == self.board[i+1][j-1] and self.board[i+1][j-1] and self.board[i+2][j-2] and self.board[i+2][j-2] == self.board[i+3][j-3] and self.board[i][j] != " ":
                    return True
        return False #Dummy Boi
                    
        
        

if __name__ == "__main__":
    new_board = Board(6,7)