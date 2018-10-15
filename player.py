class Player:
    def __init__(self,piece):
        self.name = self.get_name()
        self.choice = self.get_choice()
        self.piece = piece
#        self.piece = self.get_piece()
        
    
    def get_name(self):
        name = input("What is your name:  ")        
    def get_choice(self):
        pass
    
#    def get_piece(self):
#        str(input('what will your piece be:  '))
        
        
        
        



if __name__ == "__main__":
    Player('a')