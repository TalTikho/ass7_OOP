# board.py
import random
from cell import Cell

class Board:
    
    "Constructor"
    def __init__(self, size, bomb_count):
        #Initialize the game board with given size and number of bombs
        #Validating the inputs
        if not isinstance(size, int) or not isinstance(bomb_count, int):
            raise ValueError("Size and bomb count must be integers")
        
        if size < 5 or size > 20:
            raise ValueError("Board size must be between 5 and 20")
            
        if bomb_count < 1:
            raise ValueError("Must have at least one bomb")
            
        if bomb_count >= size * size:
            raise ValueError("Too many bombs for the board size")

        self.size = size
        self.bomb_count = bomb_count
        self.cells = [[Cell() for _ in range(size)] for _ in range(size)]
        #Wating for the first move and not placing the bombs
        self.first_move_made = False
    
    "Making the first move"
    def make_first_move(self, first_x, first_y):
        #Place bombs after the first move to ensure first click is safe
        if not self.first_move_made:
            self._place_bombs(first_x, first_y)
            self._calculate_neighbor_bombs()
            self.first_move_made = True

    "Placing the bombs"
    def _place_bombs(self, safe_x, safe_y):
        #Randomly place bombs on the board, ensuring the first clicked position and its immediate neighbors are safe.
        #Getting safe positions (first click and its neighbors)
        safe_positions = {(safe_x, safe_y)}
        for dx, dy in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
            new_x, new_y = safe_x + dx, safe_y + dy
            if self.is_valid_position(new_x, new_y):
                safe_positions.add((new_x, new_y))

        #Creating list of all possible positions excluding safe positions
        all_positions = [(x, y) for x in range(self.size) 
                        for y in range(self.size) 
                        if (x, y) not in safe_positions]
        #Randomly selecting positions for bombs
        bomb_positions = random.sample(all_positions, min(self.bomb_count, len(all_positions)))
        
        #Placing the bombs
        for x, y in bomb_positions:
            self.cells[x][y].is_bomb = True

    "Calculating NBombs"
    def _calculate_neighbor_bombs(self):
        #Calculate the number of neighboring bombs for each cell
        for x in range(self.size):
            for y in range(self.size):
                if not self.cells[x][y].is_bomb:
                    count = sum(1 for new_x, new_y in self.get_neighbor_positions(x, y)
                              if self.cells[new_x][new_y].is_bomb)
                    self.cells[x][y].neighbor_bombs = count

    "Validating position"
    def is_valid_position(self, x, y):
        #Check if the given position is valid on the board
        return 0 <= x < self.size and 0 <= y < self.size
    
    "Getting all the valid positions"
    def get_neighbor_positions(self, x, y):
        #Get all valid neighboring positions for a given cell
        return [(x + dx, y + dy) for dx, dy in 
                [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
                if self.is_valid_position(x + dx, y + dy)]
