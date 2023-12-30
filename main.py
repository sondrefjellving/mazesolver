from graphics import Window, Point, Line, Cell
from maze import Maze

win = Window(800, 600)
maze = Maze(5, 5, 6, 9, 80, 80, win)
win.wait_for_close()