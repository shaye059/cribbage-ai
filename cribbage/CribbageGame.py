import sys
import numpy as np

sys.path.append('..')
from Game import Game

class CribbageGame(Game):
    """
    Cribbage Game class implementing the alpha-zero-general Game interface.
    """

    def __init__(self, height=None, width=None, win_length=None, np_pieces=None):
        Game.__init__(self)

    def getInitBoard(self):
        return

    def getBoardSize(self):
        return
    def getActionSize(self):
        return

    def getNextState(self, board, player, action):
        """Returns a copy of the board with updated move, original board is unmodified."""
        return

    def getValidMoves(self, board, player):
        "Any zero value in top row in a valid move"
        return

    def getGameEnded(self, board, player):
        return

    def getCanonicalForm(self, board, player):
        # Flip player from 1 to -1
        return board * player

    def getSymmetries(self, board, pi):
        """Board is left/right board symmetric"""
        return [(board, pi), (board[:, ::-1], pi[::-1])]

    def stringRepresentation(self, board):
        return board.tostring()

    @staticmethod
    def display(board):
        print(" -----------------------")
        print(' '.join(map(str, range(len(board[0])))))
        print(board)
        print(" -----------------------")
