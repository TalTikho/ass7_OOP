# main.py
import tkinter as tk
from minesweeper import Minesweeper
from guiwindow import GuiWindow

if __name__ == "__main__":
    #First show configuration window
    config = GuiWindow()
    
    #If user closed the config window without starting
    if config.size is None or config.bombs is None:
        exit()
    
    #Create main game window
    root = tk.Tk()
    game = Minesweeper(root, size=config.size, bomb_count=config.bombs)
    root.mainloop()
