from player import Player
from board import Board
class Game:
    def __init__(self):
        self.turn = 0
        self.players = []
#        self.players.append(Player('a'))
#        self.players.append(Player('b'))
        self.board = Board(7,7)
        
    
    def play_game(self):
        print('Welcome to Connect Four')
        print('')
        print('Player 1 what is your name')
        self.players.append(Player('a'))
        print('Player 2 what is your name')
        self.players.append(Player('b'))
        self.board.displayboard()
        Player.get_choice(self,self.board)
        
        
        


if __name__ == "__main__":
    d = Game()
    d.play_game()