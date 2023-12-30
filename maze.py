from graphics import Cell
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.__cells = []
        self.__create_cells()

    def __create_cells(self):
        for c in range(self.num_cols):
            col = []
            for r in range(self.num_rows):
                col.append(Cell(self.win))
            self.__cells.append(col)

            for r in range(self.num_rows):
                self.__draw_cell(c, r)

        
    def __draw_cell(self, c, r):
        x1 = self.x1 + c*self.cell_size_x
        y1 = self.y1 + r*self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self.__cells[c][r].draw(x1, y1, x2, y2)
        self.__animate()

    def __animate(self):
        self.win.redraw()
        time.sleep(0.01)



