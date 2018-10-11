

class Board:
    def __init__(self, width, height):
        self.bd = [["*"] * width for i in range(height)]
        
    def displayBoard(self):
        for row in self.bd:
            for element in row:
                print(element,end=' ')
        print()
            
        
        
        
        
        
if __name == "__main__":
    pass