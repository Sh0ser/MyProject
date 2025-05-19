import unittest
import sys
import os
from unittest.mock import Mock, patch

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.main import TicTacToe

class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        """Set up a new game before each test."""
        self.mock_master = Mock()
        with patch('tkinter.Label'), patch('tkinter.Button'), patch('tkinter.Frame'):
            self.game = TicTacToe(self.mock_master)
    
    def test_initial_state(self):
        """Test the initial state of the game."""
        self.assertEqual(self.game.current_player, 'X')
        self.assertEqual(self.game.board, [[' ' for _ in range(3)] for _ in range(3)])
        
    def test_check_winner_rows(self):
        """Test horizontal win condition."""
        self.game.board[0] = ['X', 'X', 'X']
        self.assertEqual(self.game.check_winner(), 'X')
        
        self.game.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.game.board[1] = ['O', 'O', 'O']
        self.assertEqual(self.game.check_winner(), 'O')

        self.game.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.game.board[2] = ['X', 'X', 'X']
        self.assertEqual(self.game.check_winner(), 'X')
    
    def test_check_winner_columns(self):
        """Test vertical win condition."""
        for i in range(3):
            self.game.board[i][0] = 'X'
        self.assertEqual(self.game.check_winner(), 'X')

        self.game.board = [[' ' for _ in range(3)] for _ in range(3)]
        for i in range(3):
            self.game.board[i][1] = 'O'
        self.assertEqual(self.game.check_winner(), 'O')

        self.game.board = [[' ' for _ in range(3)] for _ in range(3)]
        for i in range(3):
            self.game.board[i][2] = 'X'
        self.assertEqual(self.game.check_winner(), 'X')
    
    def test_check_winner_diagonals(self):
        """Test diagonal win conditions."""
        for i in range(3):
            self.game.board[i][i] = 'X'
        self.assertEqual(self.game.check_winner(), 'X')

        self.game.board = [[' ' for _ in range(3)] for _ in range(3)]
        for i in range(3):
            self.game.board[i][2-i] = 'O'
        self.assertEqual(self.game.check_winner(), 'O')
    
    def test_check_winner_no_winner(self):
        """Test when there is no winner."""
        self.game.board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', 'O']
        ]
        self.assertIsNone(self.game.check_winner())
    
    def test_is_full_empty_board(self):
        """Test is_full with an empty board."""
        self.assertFalse(self.game.is_full())
    
    def test_is_full_partially_filled(self):
        """Test is_full with a partially filled board."""
        self.game.board = [
            ['X', 'O', 'X'],
            ['O', ' ', 'O'],
            ['O', 'X', 'O']
        ]
        self.assertFalse(self.game.is_full())
    
    def test_is_full_completely_filled(self):
        """Test is_full with a completely filled board."""
        self.game.board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', 'O']
        ]
        self.assertTrue(self.game.is_full())
    
    def test_reset_game(self):
        """Test that the reset_game method clears the board and resets the player."""
        self.game.board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', 'O']
        ]
        self.game.current_player = 'O'
        
        self.game.reset_game()

        self.assertEqual(self.game.board, [[' ' for _ in range(3)] for _ in range(3)])
        self.assertEqual(self.game.current_player, 'X')
    
    def test_on_button_click_empty_cell(self):
        """Test clicking on an empty cell."""
        with patch.object(self.game, 'check_winner', return_value=None), \
             patch.object(self.game, 'is_full', return_value=False), \
             patch('tkinter.messagebox.showinfo'):
            
            self.game.on_button_click(0, 0)

            self.assertEqual(self.game.board[0][0], 'X')
            self.assertEqual(self.game.current_player, 'O')
    
    def test_on_button_click_win(self):
        """Test clicking that results in a win."""
        with patch.object(self.game, 'check_winner', return_value='X'), \
             patch.object(self.game, 'reset_game') as mock_reset, \
             patch('tkinter.messagebox.showinfo') as mock_showinfo:
            
            self.game.on_button_click(0, 0)

            mock_showinfo.assert_called_once()
            mock_reset.assert_called_once()
    
    def test_on_button_click_draw(self):
        """Test clicking that results in a draw."""
        with patch.object(self.game, 'check_winner', return_value=None), \
             patch.object(self.game, 'is_full', return_value=True), \
             patch.object(self.game, 'reset_game') as mock_reset, \
             patch('tkinter.messagebox.showinfo') as mock_showinfo:
            
            self.game.on_button_click(0, 0)

            mock_showinfo.assert_called_once()
            mock_reset.assert_called_once()
    
    def test_on_button_click_occupied_cell(self):
        """Test clicking on an already occupied cell."""
        with patch.object(self.game, 'check_winner', return_value=None), \
             patch.object(self.game, 'is_full', return_value=False):
            self.game.on_button_click(0, 0)

        first_player = self.game.current_player

        with patch.object(self.game, 'check_winner', return_value=None), \
             patch.object(self.game, 'is_full', return_value=False):
            self.game.on_button_click(0, 0)

        self.assertEqual(self.game.current_player, first_player)

    def test_reset_score(self):
        """Test that the reset_score method resets both scores to zero."""
        self.game.x_win = 5
        self.game.o_win = 3
        
        self.game.reset_score()
        
        self.assertEqual(self.game.x_win, 0)
        self.assertEqual(self.game.o_win, 0)
    
    def test_score_update_x_win(self):
        """Test score updating when X wins."""
        initial_x_wins = self.game.x_win
        
        with patch.object(self.game, 'check_winner', return_value='X'), \
             patch.object(self.game, 'reset_game'), \
             patch('tkinter.messagebox.showinfo'):
            
            self.game.on_button_click(0, 0)
            
            self.assertEqual(self.game.x_win, initial_x_wins + 1)
            self.assertEqual(self.game.o_win, 0)
    
    def test_score_update_o_win(self):
        """Test score updating when O wins."""
        initial_o_wins = self.game.o_win
        self.game.current_player = 'O'
        
        with patch.object(self.game, 'check_winner', return_value='O'), \
             patch.object(self.game, 'reset_game'), \
             patch('tkinter.messagebox.showinfo'):
            
            self.game.on_button_click(0, 0)
            
            self.assertEqual(self.game.o_win, initial_o_wins + 1)
            self.assertEqual(self.game.x_win, 0)

if __name__ == '__main__':
    unittest.main()
