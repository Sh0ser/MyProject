import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic-Tac-Toe")
        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        self.player_label = tk.Label(self.master, text=f"Хід гравця {self.current_player}", font='Arial 14')
        self.player_label.grid(row=1, column=0, columnspan=3, pady=(5, 10))

        self.button_frame = tk.Frame(self.master, padx=10, pady=10)
        self.button_frame.grid(row=2, column=0, columnspan=3)

        self.create_buttons()

        self.restart_button = tk.Button(self.master, text="Скинути рахунок", font='Arial 14',command=self.reset_score)
        self.restart_button.grid(row=3, column=0, columnspan=3, pady=10)
        self.x_win = 0
        self.o_win = 0
        self.xplayer_win_counter = tk.Label(self.master, text=f"X: {self.x_win}", font='Arial 14')
        self.xplayer_win_counter.grid(row=3, column=0, pady=(5, 10))

        self.oplayer_win_counter = tk.Label(self.master, text=f"O: {self.o_win}",font='Arial 14')
        self.oplayer_win_counter.grid(row=3, column=2, pady=(5, 10))

    def create_buttons(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col] = tk.Button(
                    self.button_frame,
                    text=' ',
                    font='Arial 30',
                    width=5,
                    height=2,
                    bd=1,
                    highlightthickness=0,
                    command=lambda r=row, c=col: self.on_button_click(r, c)
                )
                self.buttons[row][col].grid(row=row, column=col)

        for i in range(3):
            self.button_frame.grid_columnconfigure(i, weight=1)
            self.button_frame.grid_rowconfigure(i, weight=1)

    def on_button_click(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            winner = self.check_winner()
            if winner:
                if (winner == 'X'):
                    self.x_win += 1
                else:
                    self.o_win += 1
                self.xplayer_win_counter.config(text=f"X: {self.x_win}")
                self.oplayer_win_counter.config(text=f"0: {self.o_win}")
                messagebox.showinfo("Вітаємо!", f"Гравець {winner} виграв!")
                self.reset_game()
            elif self.is_full():
                messagebox.showinfo("Нічия!", "Гра зацінчилася нічиєю!")
                self.reset_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.player_label.config(text=f"Хід гравця {self.current_player}")

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        return None

    def is_full(self):
        return all(cell != ' ' for row in self.board for cell in row)

    def reset_game(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.player_label.config(text=f"Хід гравця {self.current_player}")
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=' ')

    def reset_score(self):
        self.x_win = 0
        self.xplayer_win_counter.config(text=f"X: {self.x_win}")
        self.o_win = 0
        self.oplayer_win_counter.config(text=f"0: {self.o_win}")


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
