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
                
                if self.board.check_win():
                    self.board.disp_board()
                    print(f'{self.players[self.turn].name} wins')
                    return
                if self.board.is_full():
                    self.board.disp_board()
                    print('The board is full game over')
                    return
                self.turn = (self.turn+1)%2
            except Exception as e:
                pass
        


if __name__ == "__main__":
    d = Game(Board(7,7))
    d.play_game()