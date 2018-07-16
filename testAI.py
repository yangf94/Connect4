import unittest
from gameai import *
from board import Board

class TestAI(unittest.TestCase):
    def test_getPossibleMoves(self):
        AI = Level1AI()

        humanPiece = Board.BLACK_PIECE
        aiPiece = Board.RED_PIECE

        # Test case 1
        # Create board state
        # - - - O - - -
        # - - - X - - -
        # - - - O - - -
        # - - - X - - -
        # - - - O - - -
        # - - - X - - -
        board = Board(0, 0)
        board.insertIntoColumn(3, humanPiece)
        board.insertIntoColumn(3, aiPiece)
        board.insertIntoColumn(3, humanPiece)
        board.insertIntoColumn(3, aiPiece)
        board.insertIntoColumn(3, humanPiece)
        board.insertIntoColumn(3, aiPiece)

        self.assertTrue(AI.getPossibleMoves(board) == [0, 1, 2, 4, 5, 6],
                        "Invalid list of possible moves for test case 1")

        # Test case 2
        # Create board state
        # - - X O - - -
        # - - O X X - -
        # - - X O O - -
        # - - O X X - -
        # - - X O O - -
        # - - O X X - -
        board = Board(0, 0)
        board.insertIntoColumn(3, humanPiece)
        board.insertIntoColumn(3, aiPiece)
        board.insertIntoColumn(3, humanPiece)
        board.insertIntoColumn(3, aiPiece)
        board.insertIntoColumn(3, humanPiece)
        board.insertIntoColumn(3, aiPiece)
        board.insertIntoColumn(4, humanPiece)
        board.insertIntoColumn(2, aiPiece)
        board.insertIntoColumn(2, humanPiece)
        board.insertIntoColumn(2, aiPiece)
        board.insertIntoColumn(2, humanPiece)
        board.insertIntoColumn(2, aiPiece)
        board.insertIntoColumn(2, humanPiece)
        board.insertIntoColumn(4, aiPiece)
        board.insertIntoColumn(4, humanPiece)
        board.insertIntoColumn(4, aiPiece)
        board.insertIntoColumn(4, humanPiece)

        self.assertTrue(AI.getPossibleMoves(board) == [0, 1, 4, 5, 6],
                        "Invalid list of possible moves for test case 2")

        # Test case 3
        # Create board state
        # - - - - - - -
        # - - - - - - -
        # - - - - - - -
        # - - - - - - -
        # - - - - - - -
        # - - - - - - -
        board = Board(0, 0)

        self.assertTrue(AI.getPossibleMoves(board) == [0, 1, 2, 3, 4, 5, 6],
                        "Invalid list of possible moves for test case 3")

        # Test case 4
        # Create board state
        # O O O O O O O
        # X X X X X X X
        # O O O O O O O
        # X X X X X X X
        # O O O O O O O
        # X X X X X X X
        board = Board(0, 0)
        board.insertIntoColumn(0, humanPiece)
        board.insertIntoColumn(0, aiPiece)
        board.insertIntoColumn(0, humanPiece)
        board.insertIntoColumn(0, aiPiece)
        board.insertIntoColumn(0, humanPiece)
        board.insertIntoColumn(0, aiPiece)
        board.insertIntoColumn(1, humanPiece)
        board.insertIntoColumn(1, aiPiece)
        board.insertIntoColumn(1, humanPiece)
        board.insertIntoColumn(1, aiPiece)
        board.insertIntoColumn(1, humanPiece)
        board.insertIntoColumn(1, aiPiece)
        board.insertIntoColumn(2, humanPiece)
        board.insertIntoColumn(2, aiPiece)
        board.insertIntoColumn(2, humanPiece)
        board.insertIntoColumn(2, aiPiece)
        board.insertIntoColumn(2, humanPiece)
        board.insertIntoColumn(2, aiPiece)
        board.insertIntoColumn(3, humanPiece)
        board.insertIntoColumn(3, aiPiece)
        board.insertIntoColumn(3, humanPiece)
        board.insertIntoColumn(3, aiPiece)
        board.insertIntoColumn(3, humanPiece)
        board.insertIntoColumn(3, aiPiece)
        board.insertIntoColumn(4, humanPiece)
        board.insertIntoColumn(4, aiPiece)
        board.insertIntoColumn(4, humanPiece)
        board.insertIntoColumn(4, aiPiece)
        board.insertIntoColumn(4, humanPiece)
        board.insertIntoColumn(4, aiPiece)
        board.insertIntoColumn(5, humanPiece)
        board.insertIntoColumn(5, aiPiece)
        board.insertIntoColumn(5, humanPiece)
        board.insertIntoColumn(5, aiPiece)
        board.insertIntoColumn(5, humanPiece)
        board.insertIntoColumn(5, aiPiece)
        board.insertIntoColumn(6, humanPiece)
        board.insertIntoColumn(6, aiPiece)
        board.insertIntoColumn(6, humanPiece)
        board.insertIntoColumn(6, aiPiece)
        board.insertIntoColumn(6, humanPiece)
        board.insertIntoColumn(6, aiPiece)

        self.assertTrue(AI.getPossibleMoves(board) == [],
                        "Invalid list of possible moves for test case 4")

if(__name__=="__main__"):
    unittest.main()