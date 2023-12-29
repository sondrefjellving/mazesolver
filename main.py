from graphics import Window, Point, Line, Cell
from maze import Maze

win = Window(800, 600)
maze = Maze(5, 5, 10, 15, 50, 50, win)

win.wait_for_close()