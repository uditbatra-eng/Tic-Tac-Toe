# 1. Piece
# PlayingPiece
# PieceO
# PieceX

from abc import ABC, abstractmethod
class Piece(ABC):
    @abstractmethod
    def Sign(self):
        pass

class PieceX(Piece):
    def __init__(self):
        pass
    def Sign(self):
        return "X"

class PieceO(Piece):
    def __init__(self):
        pass
    def Sign(self):
        return "O"

class PlayingPiece:
    def __init__(self,piece:Piece):
        self.symbol = piece
    
    def RetSign(self):        
        return self.symbol.Sign()

# 2. Board:

class Board:
    def __init__(self,board = 3):
        self.board = [[" " for i in range(board)] for i in range(board)]
    
    def Add(self,r,c,symbol):
        if self.board[r][c] == " ":
            self.board[r][c] = symbol
            return True
        return False
    
    def DisplayBoard(self):
        for i in range(len(self.board)):
            print((' | ').join(self.board[i]))
            # if i<len(self.board)-1:
            #     print('-'*5)

    def FreeCells(self):
        ans = []
        for i in range(self.board):
            for j in range(self.board):
                if self.board[i][j] == " ":
                    ans += ([i],[j])
        return ans

    def IsFull(self):
        if all(self.board[row][col] != ' ' for row in range(3) for col in range(3)):
            return True
        return False
    
# 3. Player

class Player:
    def __init__(self,name,piece:Piece) -> None:
        self.Name = name
        self.Piece = piece

    def GetName(self):
        return self.Name

    def SetName(self,name):
        self.Name = name

    def SetPlayingPiece(self):
        return self.Piece.Sign()

# Main Game

class Game:
    def __init__(self) -> None:
        # Initialize the board and players
        self.board = Board()
        self.player1 = Player("Player 1", PieceX())
        self.player2 = Player("Player 2", PieceO())
        self.current_player = self.player1  # Player 1 starts the game
    
    def switch_turns(self):
        # Alternate between player 1 and player 2
        self.current_player = self.player1 if self.current_player == self.player2 else self.player2
    
    def take_turn(self):
        # Get the current player's move
        valid_move = False
        while not valid_move:
            try:
                row, col = map(int, input(f"{self.current_player.GetName()}, enter row and column (0-2): ").split())
                if 0 <= row < 3 and 0 <= col < 3:
                    # Try to place the piece on the board
                    valid_move = self.board.Add(row, col, self.current_player.SetPlayingPiece())
                    if not valid_move:
                        print("Cell already occupied, try again.")
                else:
                    print("Invalid input. Please enter numbers between 0 and 2.")
            except ValueError:
                print("Invalid input. Please enter two integers.")
    
    def is_winner(self):
        # Check for a winner (rows, columns, diagonals)
        board = self.board.board
        for i in range(3):
            # Check rows and columns
            if board[i][0] == board[i][1] == board[i][2] != " " or board[0][i] == board[1][i] == board[2][i] != " ":
                return True
        # Check diagonals
        if board[0][0] == board[1][1] == board[2][2] != " " or board[0][2] == board[1][1] == board[2][0] != " ":
            return True
        return False

    def play(self):
        print("Starting Tic-Tac-Toe game...")
        self.board.DisplayBoard()

        while True:
            self.take_turn()
            self.board.DisplayBoard()

            if self.is_winner():
                print(f"{self.current_player.GetName()} wins!")
                break

            if self.board.IsFull():
                print("The game is a draw!")
                break

            self.switch_turns()


if __name__ == "__main__":
    game = Game()
    game.play()

        
