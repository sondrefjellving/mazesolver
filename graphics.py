from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, w, h):
        self.__root = Tk()
        self.__root.title("Maze solver")
        self.__root.geometry(f"{w}x{h}")
        self.__canvas = Canvas(self.__root, height=h, width=w)
        self.__canvas.pack()
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)
    
        
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
class Line:
    def __init__(self, start_p, end_p):
        self.start = start_p
        self.end = end_p
    
    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color, width=2
            )
        canvas.pack()

class Cell:
    def __init__(self, x1, y1, x2, y2, win):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__win = win
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.has_left_wall = True

    def draw(self):
        if self.has_top_wall:
            wall = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            self.__win.draw_line(wall, "black")

        if self.has_right_wall:
            wall = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
            self.__win.draw_line(wall, "black")

        if self.has_bottom_wall:
            wall = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            self.__win.draw_line(wall, "black")

        if self.has_left_wall:
            wall = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            self.__win.draw_line(wall, "black")

