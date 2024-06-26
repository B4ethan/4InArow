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

        self.arr_with_boards = []

    def turn(self, turn, col):
        # Adjust for 0-based index
        col -= 1
        
        # Check if the column is valid
        if col < 0 or col >= 7:
            return False

        for row in range(5, -1, -1):  # Start from the bottom row
            if self.board[row][col] == ' ':
                self.board[row][col] = turn
                return True
        
        return False

    def printBoard(self):
        print("1   2   3   4   5   6   7")
        for row in self.board:
            print(" | ".join(row))
            print("-" * 29)
        print()
    
    def livePlayerTurn(self):
        turn = int(input(f"Its your turn, pls enter the col you want to put your piece: "))
        isValid = self.turn("X", turn)

        while not isValid:
            turn = int(input(f"column is full or invaild, Pls choose another column: "))
            isValid = self.turn("X", turn)
        
    def randomPlayerTurn(self, gamePeice):
        turn = random.randint(1, 7)  # Correct range to 1-7
        isValid = self.turn(gamePeice, turn)

        while not isValid:
            turn = random.randint(1, 7)
            isValid = self.turn(gamePeice, turn)


    def playGameLiveVSrandom(self):
        isWin = WinChecker(self.board)

        for i in range(21): # Each player gets 21 turns until the board is full
            self.printBoard()
            self.livePlayerTurn()
            self.printBoard()

            if isWin.checkWin() == 1:
                print("Damn! you won!")
                return
            
            self.randomPlayerTurn('O')

            if isWin.checkWin() == 2:
                print("L, you lost to the Bot!")
                return
            
        self.printBoard()
        print("That was a good game! It ends with a tie!")

    def playGameRandVSrand(self):
        isWin = WinChecker(self.board)

        for i in range(21): 
            self.printBoard()
            self.randomPlayerTurn('X')
            self.printBoard()

            if isWin.checkWin() == 1:
                print("Player 1 won!")
                return 1
            
            self.randomPlayerTurn('O')
            
            if isWin.checkWin() == 2:
                self.printBoard()
                print("Player 2 won!")
                return 2
            
        self.printBoard()
        print("Tie!")
        return 0

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
            if self.checkStreakOf4(row, 'X'):  # Correct piece representation
                return 1
            elif self.checkStreakOf4(row, 'O'):
                return 2
        return 0

    def checkWinVertical(self):
        for col in range(len(self.boardToCheck[0])):
            column = [self.boardToCheck[row][col] for row in range(len(self.boardToCheck))]
            if self.checkStreakOf4(column, 'X'):
                return 1
            elif self.checkStreakOf4(column, 'O'):
                return 2
        return 0
    
    def checkWinDiagonal(self):
        # Positive slope diagonals
        for row in range(3, len(self.boardToCheck)):
            for col in range(len(self.boardToCheck[0]) - 3):
                diagonal = [self.boardToCheck[row - i][col + i] for i in range(4)]
                if self.checkStreakOf4(diagonal, 'X'):
                    return 1
                elif self.checkStreakOf4(diagonal, 'O'):
                    return 2

        # Negative slope diagonals
        for row in range(len(self.boardToCheck) - 3):
            for col in range(len(self.boardToCheck[0]) - 3):
                diagonal = [self.boardToCheck[row + i][col + i] for i in range(4)]
                if self.checkStreakOf4(diagonal, 'X'):
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
    game.playGameRandVSrand()

if __name__ == '__main__':
    main()
