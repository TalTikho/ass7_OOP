# minesweeper.py
import tkinter as tk
from tkinter import messagebox
from board import Board

class Minesweeper:

    "Constructor"
    def __init__(self, root, size, bomb_count):
        self.root = root
        self.root.title("Minesweeper")
        self.board = Board(size, bomb_count)
        self.buttons = []
        self.first_move = True
        self._create_widgets()

    # "Creating widget"
    # def _create_widgets(self):
    #     for x in range(self.board.size):
    #         row = []
    #         for y in range(self.board.size):
    #             btn = tk.Button(
    #                 self.root, 
    #                 width=2, 
    #                 height=1, 
    #                 bg="light gray",
    #                 command=lambda x=x, y=y: self._reveal_cell(x, y)
    #             )
    #             btn.bind("<Button-3>", lambda e, x=x, y=y: self._toggle_flag(x, y))
    #             btn.grid(row=x, column=y)
    #             row.append(btn)
    #         self.buttons.append(row)
    def _create_widgets(self):
        """Create the grid of buttons for the game."""
        for x in range(self.board.size):
            row = []
            for y in range(self.board.size):
                btn = tk.Button(
                    self.root, 
                    width=2, 
                    height=1, 
                    bg="light gray",
                    command=lambda x=x, y=y: self._reveal_cell(x, y)
                )
                btn.bind("<Button-3>", lambda e, x=x, y=y: self._toggle_flag(x, y))
                btn.grid(row=x, column=y)
                row.append(btn)
            self.buttons.append(row)

    "Reaviling cell"
    def _reveal_cell(self, x, y):
        cell = self.board.cells[x][y]
        
        if cell.is_flagged:
            return

        if self.first_move:
            self.board.make_first_move(x, y)
            self.first_move = False

        if cell.reveal():
            if cell.is_bomb:
                self._game_over()
            else:
                self._reveal_recursive(x, y)
                if self._check_win():
                    self._show_win()

    "Reavilng REC"
    def _reveal_recursive(self, x, y):
        cell = self.board.cells[x][y]
        if not cell.is_revealed or cell.is_bomb:
            return

        # Update button appearance
        self.buttons[x][y].config(
            bg="white",
            state=tk.DISABLED,
            text=str(cell.neighbor_bombs) if cell.neighbor_bombs > 0 else ""
        )

        # If cell has no neighboring bombs, reveal neighbors
        if cell.neighbor_bombs == 0:
            for new_x, new_y in self.board.get_neighbor_positions(x, y):
                neighbor_cell = self.board.cells[new_x][new_y]
                if not neighbor_cell.is_revealed and not neighbor_cell.is_flagged:
                    neighbor_cell.reveal()
                    self._reveal_recursive(new_x, new_y)
    
    # "Flagging"
    # def _toggle_flag(self, x, y, event):
    #     cell = self.board.cells[x][y]
    #     if not cell.is_revealed:
    #         if cell.toggle_flag():
    #             self.buttons[x][y].config(
    #                 text="🚩" if cell.is_flagged else "",
    #                 bg="light gray"
    #             )
    def _toggle_flag(self, x, y, event=None):
        """Handle the right-click event to toggle flag."""
        cell = self.board.cells[x][y]
        if cell.toggle_flag():
            self.buttons[x][y].config(
                text="🚩" if cell.is_flagged else "",
                bg="light gray"
            )

    "Checking win case"
    def _check_win(self):
        for x in range(self.board.size):
            for y in range(self.board.size):
                cell = self.board.cells[x][y]
                if not cell.is_bomb and not cell.is_revealed:
                    return False
        return True

    "Show win"
    def _show_win(self):
        for x in range(self.board.size):
            for y in range(self.board.size):
                if self.board.cells[x][y].is_bomb:
                    self.buttons[x][y].config(text="🚩", bg="light green")
        messagebox.showinfo("Congratulations!", "You've won!")
        self.root.quit()
        
    "Game over case"
    def _game_over(self):
        for x in range(self.board.size):
            for y in range(self.board.size):
                cell = self.board.cells[x][y]
                if cell.is_bomb:
                    self.buttons[x][y].config(text="💣", bg="red")
        messagebox.showinfo("Game Over", "You hit a mine!")
        self.root.quit()
