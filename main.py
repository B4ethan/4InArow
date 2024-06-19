import random
import numpy as np

class OneGame():
    def __init__(self):
        self.board = np.array([
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
        ])

    def turn(self, turn, col):
        # Adjust for 0-based index
        col -= 1
        
        # Check if the column is valid
        while col < 0 or col >= 7:
            col = int(input(f"You chose {col+1} which is invalid, please choose a valid column (1-7): ")) - 1

        for row in range(5, -1, -1):  # Start from the bottom row
            if self.board[row][col] == ' ':
                self.board[row][col] = turn
                return
        print(f"Column {col+1} is full. Choose another column.")

    def printBoard(self):
        print("1   2   3   4   5   6   7")
        for row in self.board:
            print(" | ".join(row))
            print("-" * 29)
        print()
    
    def livePlayerTurn(self):
        turn = int(input(f"Its your turn, pls enter the col you want to put your piece: "))
        self.turn("x", turn)

    def randomPlayerTurn(self):
        turn = random.randint(1, 7)  # Correct range to 1-7
        self.turn("O", turn)

    def playGame(self):
        isWin = WinChecker(self.board)

        for i in range(21): # Each player gets 21 turns until the board is full
            self.printBoard()
            self.livePlayerTurn()
            self.printBoard()

            if isWin.checkWin() == 1:
                print("Damn! you won!")
                return
            
            self.randomPlayerTurn()

            if isWin.checkWin() == 2:
                print("L, you lost to the Bot!")
                return
            
        self.printBoard()
        print("That was a good game! It ends with a tie!")
#add this to check something
class WinChecker():
    # 1 - live player wins
    # 2 - bot player wins
    # 0 - still no win

    def __init__(self, board):
        self.boardToCheck = board

    def checkStreakOf4(self, partOfBoard, gamePiece):
        streak = 0  # True return if the streak is 4

        for cell in partOfBoard:
            if cell == gamePiece:
                streak += 1
                if streak == 4:
                    return True
            else:
                streak = 0
        
        return False
    
    def checkWinHorizontal(self):
        for row in self.boardToCheck:
            if self.checkStreakOf4(row, 'x'):  # Correct piece representation
                return 1
            elif self.checkStreakOf4(row, 'O'):
                return 2
        return 0

    def checkWinVertical(self):
        for col in range(len(self.boardToCheck[0])):
            column = [self.boardToCheck[row][col] for row in range(len(self.boardToCheck))]
            if self.checkStreakOf4(column, 'x'):
                return 1
            elif self.checkStreakOf4(column, 'O'):
                return 2
        return 0
    
    def checkWinDiagonal(self):
        # Positive slope diagonals
        for row in range(3, len(self.boardToCheck)):
            for col in range(len(self.boardToCheck[0]) - 3):
                diagonal = [self.boardToCheck[row - i][col + i] for i in range(4)]
                if self.checkStreakOf4(diagonal, 'x'):
                    return 1
                elif self.checkStreakOf4(diagonal, 'O'):
                    return 2

        # Negative slope diagonals
        for row in range(len(self.boardToCheck) - 3):
            for col in range(len(self.boardToCheck[0]) - 3):
                diagonal = [self.boardToCheck[row + i][col + i] for i in range(4)]
                if self.checkStreakOf4(diagonal, 'x'):
                    return 1
                elif self.checkStreakOf4(diagonal, 'O'):
                    return 2
        return 0

    def checkWin(self):
        horizontalWin = self.checkWinHorizontal()
        if horizontalWin != 0:
            return horizontalWin
        
        verticalWin = self.checkWinVertical()
        if verticalWin != 0:
            return verticalWin
        
        diagonalWin = self.checkWinDiagonal()
        if diagonalWin != 0:
            return diagonalWin
        
        return 0

def main():
    game = OneGame()
    game.playGame()

if __name__ == '__main__':
    main()
