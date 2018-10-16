class Player:
    def __init__(self,piece):
        self.name = self.get_name()
        self.piece = piece

        
    
    def get_name(self):
        self = input("What is your name:  ")
        return self
    def get_choice(self,Board):
        choice = int(input(f"{self.players[self.turn].name} pick a column: "))
        if choice <= 0:
            print('The value can not be less than or equal to 0')
            get_choice()
        elif choice > self.board.width:
            print('That is a value bigger than the board itself')
            get_choice()
        
        
    
        
        
        
        



if __name__ == "__main__":
    Player('a')