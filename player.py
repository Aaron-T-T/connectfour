class Player:
    def __init__(self,piece):
        self.name = self.get_name()
        self.piece = piece

        
    
    def get_name(self):
        self = input("What is your name:  ")
        return self
    def get_choice(self,Board):
        choice = int(input(f"{self.players[self.turn].name}, pick a column: "))
        return int(choice)
        
        
    
        
        
        
        



if __name__ == "__main__":
    Player('a')