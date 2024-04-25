from cell import Cell
import time
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
                 win
                 ):
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()
        self.seed = None
        if self.seed is not None:
            random.seed(self.seed)

    def _create_cells(self):
        for i in range (self.num_cols):
            current_column = []
            for y in range (self.num_rows):
                current_column.append(Cell(self._win))
            self._cells.append(current_column)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i,j)
    
    def _draw_cell(self,i,j):

        if self._win is None:
            return
        
        x1 = self._x1 + i * self._cell_size_x

        y1 = self._y1 + j * self._cell_size_y

        x2 = x1 + self._cell_size_x

        y2 = y1 + self._cell_size_y

        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()
        

    def _animate(self):
        self._win.redraw()
        time.sleep(0.01)

    def _break_entrance_and_Exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False
        self._draw_cell(self.num_cols-1,self.num_rows-1)

    def _break_walls_r(self,i,j):
        self._cells[i][j].visited = True
        while True:
           
            cell_list = []
            if i > 0 :
                if self._cells[i-1][j].visited == False:
                
                 cell_list.append((i-1,j))

            if i < self.num_cols-1 :
                if self._cells[i+1][j].visited == False:
                
                    cell_list.append((i+1,j))
            if j > 0 :
                if self._cells[i][j-1].visited == False:
                
                    cell_list.append((i,j-1))
            if j < self.num_rows-1:
                if self._cells[i][j+1].visited == False:
                
                    cell_list.append((i,j+1))
            if len(cell_list) == 0:
               self._draw_cell(i,j)
               return
            
            r_index = random.randrange(0,len(cell_list))
            index = cell_list[r_index]
            

            if index[0] == i-1:
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
                self._draw_cell(i,j)
                self._draw_cell(i-1,j)
                
            if index[0] == i+1:
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
                self._draw_cell(i,j)
                self._draw_cell(i+1,j)
                

            if index[1] == j-1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False
                self._draw_cell(i,j)
                self._draw_cell(i,j-1)
                

            if index[1] == j+1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False
                self._draw_cell(i,j)
                self._draw_cell(i,j+1)
               
            self._break_walls_r(index[0],index[1])
            
    def _reset_cells_visited(self):
        for cell_col in self._cells:
            for cell in cell_col:
                cell.visited = False
    
    def solve(self):
        return self._solve_r(0,0)
    
    def _solve_r(self,i,j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self.num_cols-1 and j == self.num_rows-1:
            return True
        
        if self._cells[i][j].has_bottom_wall == False and self._cells[i][j+1].visited == False and j<self.num_rows-1:
            
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_r(i, j+1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j+1],True)
        
        if self._cells[i][j].has_top_wall == False and self._cells[i][j-1].visited == False and j>0:
            
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_r(i, j-1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j-1],True)

        if self._cells[i][j].has_left_wall == False and self._cells[i-1][j].visited == False and i>0:
            
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve_r(i-1,j):
                return True
            self._cells[i][j].draw_move(self._cells[i-1][j],True)

        if self._cells[i][j].has_right_wall == False and self._cells[i+1][j].visited == False and i < self.num_cols-1:
            
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i+1,j):
                return True
            self._cells[i][j].draw_move(self._cells[i+1][j],True)
        return False

            




        
                

