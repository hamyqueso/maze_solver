from cell import Cell
import time

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):

        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._cells = []

        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        for i in range(self._num_cols):
            col = []
            for j in range(self._num_rows):
                col.append(Cell(self._win))
            self._cells.append(col)
        
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cell(i, j)
        
    def _draw_cell(self, i, j):
        if self._win == None:
            return
        
        x_offset = self._x1
        y_offset = self._y1
        x1 = i * self._cell_size_x + x_offset
        x2 = i * self._cell_size_x + self._cell_size_x + x_offset
        y1 = j * self._cell_size_y + y_offset
        y2 = j * self._cell_size_y + self._cell_size_y + y_offset
        
        self._cells[i][j].draw(x1, x2, y1, y2)
        self._animate()

    def _animate(self):
        if self._win == None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_left_wall = False
        self._draw_cell(0, 0)
        
        last_col = self._num_cols - 1
        last_row = self._num_rows - 1
        self._cells[last_col][last_row].has_right_wall = False
        self._draw_cell(last_col, last_row)

        



