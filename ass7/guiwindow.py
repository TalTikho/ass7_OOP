#window.py
import tkinter as tk
from tkinter import ttk, messagebox

class GuiWindow:

    "Constructor"
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Minesweeper Configuration")
        self.size = None
        self.bombs = None
        self._create_widgets()
        self.root.mainloop()

    "Creating window"
    def _create_widgets(self):
        #Setting variables
        #Create and pack a frame for better organization
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Size configuration
        ttk.Label(frame, text="Board Size (5-20):").grid(row=0, column=0, padx=5, pady=5)
        self.size_var = tk.StringVar(value="10")
        self.size_entry = ttk.Entry(frame, textvariable=self.size_var)
        self.size_entry.grid(row=0, column=1, padx=5, pady=5)

        # Bombs configuration
        ttk.Label(frame, text="Number of Bombs:").grid(row=1, column=0, padx=5, pady=5)
        self.bombs_var = tk.StringVar(value="10")
        self.bombs_entry = ttk.Entry(frame, textvariable=self.bombs_var)
        self.bombs_entry.grid(row=1, column=1, padx=5, pady=5)

        # Start button
        ttk.Button(frame, text="Start Game", command=self._validate_and_start).grid(row=2, column=0, columnspan=2, pady=10)

    "Validating and starting"
    def _validate_and_start(self):
        #try&catch in case there is an invalid input
        try:
            size = int(self.size_var.get())
            bombs = int(self.bombs_var.get())

            if not (5 <= size <= 20):
                messagebox.showerror("Error", "Board size must be between 5 and 20!")
                return

            if bombs >= size * size:
                messagebox.showerror("Error", "Too many bombs! Must be less than total cells.")
                return

            if bombs < 1:
                messagebox.showerror("Error", "Must have at least 1 bomb!")
                return

            self.size = size
            self.bombs = bombs
            self.root.quit()
            self.root.destroy()
        #Invalid input
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers!")
