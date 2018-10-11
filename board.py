

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
            
        
        
        
        
        
if __name__ == "__main__":
    eyy = Board(7, 5)
    eyy.displayBoard()
    eyy.emptyBoard()
    eyy.displayBoard()