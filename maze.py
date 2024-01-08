from cell import Cell
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        if seed:
            random.seed(seed)
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
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()

        
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
        time.sleep(0.1)

    def __break_entrance_and_exit(self):
        entrance = self.__cells[0][0]
        exit = self.__cells[self.__num_cols-1][self.__num_rows-1]
        entrance.has_top_wall = False
        exit.has_bottom_wall = False
        entrance.draw(entrance._Cell__x1, entrance._Cell__y1, entrance._Cell__x2, entrance._Cell__y2)
        exit.draw(exit._Cell__x1, exit._Cell__y1, exit._Cell__x2, exit._Cell__y2)

    def __break_walls_r(self, c, r):
        
        self.__cells[c][r].visited = True
        while True:
            unvisited = []
            has_t_adjacent = True
            has_r_adjacent = True
            has_b_adjacent = True
            has_l_adjacent = True
            if c == 0:
                has_l_adjacent = False
            if r == 0:
                has_t_adjacent = False
            if c+1 >= self.__num_cols:
                has_r_adjacent = False
            if r+1 >= self.__num_rows:
                has_b_adjacent = False
            
            if has_t_adjacent and self.__cells[c][r-1].visited == False:
                unvisited.append((c, r-1))
            if has_r_adjacent and self.__cells[c+1][r].visited == False:
                unvisited.append((c+1, r))
            if has_b_adjacent and self.__cells[c][r+1].visited == False:
                unvisited.append((c, r+1))
            if has_l_adjacent and self.__cells[c-1][r].visited == False:
                unvisited.append((c-1, r))
            
            if len(unvisited) == 0:
                self.__draw_cell(c, r)
                return
            
            direction_index = random.randrange(len(unvisited))
            choice = unvisited[direction_index]
            
            if choice[0] == c and choice[1] < r: # top
                self.__cells[c][r].has_top_wall = False
                self.__cells[c][r-1].has_bottom_wall = False
            elif choice[0] == c and choice[1] > r: # bottom
                self.__cells[c][r].has_bottom_wall = False
                self.__cells[c][r+1].has_top_wall = False
            elif choice[1] == r and choice[0] < c: # left
                self.__cells[c][r].has_left_wall = False
                self.__cells[c-1][r].has_right_wall = False
            elif choice[1] == r and choice[0] > c: # right
                self.__cells[c][r].has_right_wall = False
                self.__cells[c+1][r].has_left_wall = False
            
            self.__break_walls_r(choice[0], choice[1])

    def __reset_cells_visited(self):
        for col in self.__cells:
            for row in col:
                row.visited = False

    def solve(self):
        return self.__solve_r(0,0)
    
    def __solve_r(self, c, r):
        self.__animate()
        self.__cells[c][r].visited = True
        if self.__num_cols-1 == c and self.__num_rows-1 == r:
            return True
        
        has_t_adjacent = True
        has_r_adjacent = True
        has_b_adjacent = True
        has_l_adjacent = True

        if c == 0:
            has_l_adjacent = False
        if r == 0:
            has_t_adjacent = False
        if c+1 >= self.__num_cols:
            has_r_adjacent = False
        if r+1 >= self.__num_rows:
            has_b_adjacent = False
        
        if has_t_adjacent and not self.__cells[c][r-1].visited and not self.__cells[c][r].has_top_wall:
            self.__cells[c][r].draw_move(self.__cells[c][r-1])
            if self.__solve_r(c, r-1):
                return True
            else:
                self.__cells[c][r].draw_move(self.__cells[c][r-1], True)
        if has_r_adjacent and not self.__cells[c+1][r].visited and not self.__cells[c][r].has_right_wall:
            self.__cells[c][r].draw_move(self.__cells[c+1][r])
            if self.__solve_r(c+1, r):
                return True
            else:
                self.__cells[c][r].draw_move(self.__cells[c+1][r], True)
        if has_b_adjacent and not self.__cells[c][r+1].visited and not self.__cells[c][r].has_bottom_wall:
            self.__cells[c][r].draw_move(self.__cells[c][r+1])
            if self.__solve_r(c, r+1):
                return True
            else:
                self.__cells[c][r].draw_move(self.__cells[c][r+1], True)
        if has_l_adjacent and not self.__cells[c-1][r].visited and not self.__cells[c][r].has_left_wall:
            self.__cells[c][r].draw_move(self.__cells[c-1][r])
            if self.__solve_r(c-1, r):
                return True
            else:
                self.__cells[c][r].draw_move(self.__cells[c-1][r], True)
        return False
        

