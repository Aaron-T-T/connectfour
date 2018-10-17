from player import Player
from board import Board
class Game:
    def __init__(self,board):
        self.turn = 0
        self.players = []
        self.board = board
        
    
    def play_game(self):
        print('Welcome to Connect Four')
        print('')
        print('Player 1 what is your name')
        self.players.append(Player('*'))
        print('Player 2 what is your name')
        self.players.append(Player('/'))
        while True:
            try:
                self.board.disp_board()
                self.choice = Player.get_choice(self,self.board)
                self.board.add_piece(self.players[self.turn].piece,self.choice)
                self.board.disp_board()
                if self.board.detect_win():
                    return
                if self.board.is_full():
                    return
        
            except Exception as e:
                pass
        


if __name__ == "__main__":
    d = Game(Board(7,7))
    d.play_game()