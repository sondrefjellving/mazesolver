from graphics import Line, Point

class Cell:
    def __init__(self, win=None):
        self.__x1 = None
        self.__y1 = None
        self.__x2 = None
        self.__y2 = None
        self.__win = win
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.has_left_wall = True

    def draw(self, x1, y1, x2, y2):
        if self.__win == None:
            return
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

        color = "black" if self.has_top_wall else "white"
        wall = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
        self.__win.draw_line(wall, color)

        color = "black" if self.has_right_wall else "white"
        wall = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
        self.__win.draw_line(wall, color)

        color = "black" if self.has_bottom_wall else "white"
        wall = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
        self.__win.draw_line(wall, color)

        color = "black" if self.has_left_wall else "white"
        wall = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
        self.__win.draw_line(wall, color)

    def draw_move(self, to_cell, undo=False):
        from_cell_center_x = self.__x1 + (self.__x2-self.__x1)/2
        from_cell_center_y = self.__y1 + (self.__y2-self.__y1)/2
        to_cell_center_x = to_cell.__x1 + (to_cell.__x2-to_cell.__x1)/2
        to_cell_center_y = to_cell.__y1 + (to_cell.__y2-to_cell.__y1)/2

        move = Line(Point(from_cell_center_x, from_cell_center_y), Point(to_cell_center_x, to_cell_center_y))
        move_color = "gray" if undo else "red"

        self.__win.draw_line(move, move_color)