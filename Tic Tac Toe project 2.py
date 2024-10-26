import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.board = [''] * 9
        self.player = 'X'
        self.buttons = []
        self.create_board()

    def create_board(self):
        for i in range(9):
            button = tk.Button(self.root, text="", font=("Arial", 20), width=10, height=4,
                               command=lambda i=i: self.click_button(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)
    
    def click_button(self, index):
        if self.buttons[index]['text'] == "" and self.check_winner() is False:
            self.buttons[index]['text'] = self.player
            self.board[index] = self.player
            if not self.check_winner():
                self.player = 'O' if self.player == 'X' else 'X'
        
    def check_winner(self):
        for row in range(0, 9, 3):
            if self.board[row] == self.board[row+1] == self.board[row+2] != '':
                self.win(row)
                return True

        for col in range(3):
            if self.board[col] == self.board[col+3] == self.board[col+6] != '':
                self.win(col)
                return True

        if self.board[0] == self.board[4] == self.board[8] != '' or self.board[2] == self.board[4] == self.board[6] != '':
            self.win(0 if self.board[0] != '' else 2)
            return True

        if all(self.board):
            self.tie()
            return True

        return False

    def win(self, index):
        messagebox.showinfo("Game Over", f"Player {self.board[index]} wins!")
        self.reset_board()
        
    def tie(self):
        messagebox.showinfo("Game Over", "It's a tie!")
        self.reset_board()
        
    def reset_board(self):
        self.board = [''] * 9
        for button in self.buttons:
            button['text'] = ""
        self.player = 'X'

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
