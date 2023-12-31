from graphics import Window
from maze import Maze

win = Window(800, 600)
maze = Maze(5, 5, 8, 10, 80, 80, win, 4)
win.wait_for_close()