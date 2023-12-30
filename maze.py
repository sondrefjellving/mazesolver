from cell import Cell
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        self.__create_cells()

    def __create_cells(self):
        for c in range(self.__num_cols):
            col = []
            for r in range(self.__num_rows):
                col.append(Cell(self.__win))
            self.__cells.append(col)

            for r in range(self.__num_rows):
                self.__draw_cell(c, r)
        self.__break_entrance_and_exit()

        
    def __draw_cell(self, c, r):
        x1 = self.__x1 + c*self.__cell_size_x
        y1 = self.__y1 + r*self.__cell_size_y
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y
        self.__cells[c][r].draw(x1, y1, x2, y2)
        self.__animate()

    def __animate(self):
        if self.__win == None:
            return
        self.__win.redraw()
        time.sleep(0.01)

    def __break_entrance_and_exit(self):
        entrance = self.__cells[0][0]
        exit = self.__cells[self.__num_cols-1][self.__num_rows-1]
        entrance.has_top_wall = False
        exit.has_bottom_wall = False
        entrance.draw(entrance._Cell__x1, entrance._Cell__y1, entrance._Cell__x2, entrance._Cell__y2)
        exit.draw(exit._Cell__x1, exit._Cell__y1, exit._Cell__x2, exit._Cell__y2)




