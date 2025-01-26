#Tal Tikhonov 
# 215275512 
# ass 7
#cell.py - Respresents each cell
class Cell:

    "Constructor"
    def __init__(self):
        #Initialize a cell with default values
        self.is_bomb = False
        self.is_revealed = False
        self.is_flagged = False
        self.neighbor_bombs = 0

    "Toggle flag - hidden, revealed, or flagged"
    def toggle_flag(self):
        #Toggle the flag status of the cell if it's not revealed
        if not self.is_revealed:
            self.is_flagged = not self.is_flagged
            return True
        return False
    
    "Reveal - reveals as long as not flagged"
    def reveal(self):
        #Reveal the cell if it's not flagged
        if not self.is_flagged:
            self.is_revealed = True
            return True
        return False