from cell import Cell
from time import sleep
import random

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.seed = seed
        if seed != None:
            random.seed(seed)
        
        self._create_cells()
    
    def _create_cells(self):
        self._cells = []
        for i in range(self.num_cols):
            self._cells.append([])
            for j in range(self.num_rows):
                self._cells[i].append(Cell(self.win))
        for i, col in enumerate(self._cells):
            for j, _ in enumerate(col):
                self._draw_cell(i, j)
        return
    
    def _draw_cell(self, i, j):
        if self.win is None:
            return
        
        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_x
        
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()
        
    def _animate(self):
        self.win.redraw()
        sleep(0.05)
        
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_left_wall = False
        self._draw_cell(0, 0)
        self._cells[len(self._cells) - 1][len(self._cells[0]) - 1].has_right_wall = False
        self._draw_cell(len(self._cells) - 1, len(self._cells[0]) - 1)
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        
        while(True):
            to_visit = []
            
            if i > 0 and not self._cells[i - 1][j].visited:
                to_visit.append("left")
            if i < self.num_cols - 1 and not self._cells[i + 1][j].visited:
                to_visit.append("right")
                
            if j > 0 and not self._cells[i][j - 1].visited:
                to_visit.append("up")
            if j < self.num_rows - 1 and not self._cells[i][j + 1].visited:
                to_visit.append("down")
                
            if len(to_visit) == 0:
                return
            else:
                direction = random.randrange(len(to_visit))
                match to_visit[direction]:
                    case "left":
                        self._cells[i][j].has_left_wall = False
                        self._cells[i - 1][j].has_right_wall = False
                        self._draw_cell(i , j)
                        self._draw_cell(i - 1, j)
                        self._break_walls_r(i - 1, j)
                    case "right":
                        self._cells[i][j].has_right_wall = False
                        self._cells[i + 1][j].has_left_wall = False
                        self._draw_cell(i , j)
                        self._draw_cell(i + 1, j)
                        self._break_walls_r(i + 1, j)
                    case "up":
                        self._cells[i][j].has_top_wall = False
                        self._cells[i][j - 1].has_bottom_wall = False
                        self._draw_cell(i , j)
                        self._draw_cell(i, j - 1)
                        self._break_walls_r(i, j - 1)
                    case "down":
                        self._cells[i][j].has_bottom_wall = False
                        self._cells[i][j + 1].has_top_wall = False
                        self._draw_cell(i , j)
                        self._draw_cell(i, j + 1)
                        self._break_walls_r(i, j + 1)
    
    def _reset_cells_visited(self):
        for i, col in enumerate(self._cells):
            for j, _ in enumerate(col):
                self._cells[i][j].visited = False

    def solve(self):
        return self.solve_r(0, 0)

    def solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True

        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        # check left
        if i > 0 and not self._cells[i][j].has_left_wall and not self._cells[i - 1][j].visited:
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            attempt = self.solve_r(i - 1, j)
            if attempt:
                return True
            self._cells[i - 1][j].draw_move(self._cells[i][j], True)

        # check right
        if i < self.num_cols - 1 and not self._cells[i][j].has_right_wall and not self._cells[i + 1][j].visited:
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            attempt = self.solve_r(i + 1, j)
            if attempt:
                return True
            self._cells[i + 1][j].draw_move(self._cells[i][j], True)

        # check up
        if j > 0 and not self._cells[i][j].has_top_wall and not self._cells[i][j - 1].visited:
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            attempt = self.solve_r(i, j - 1)
            if attempt:
                return True
            self._cells[i][j - 1].draw_move(self._cells[i][j], True)

        # check down
        if j < self.num_rows - 1 and not self._cells[i][j].has_bottom_wall and not self._cells[i][j + 1].visited:
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            attempt = self.solve_r(i, j + 1)
            if attempt:
                return True
            self._cells[i][j + 1].draw_move(self._cells[i][j], True)

        return False
            
            
        

        
        
            
