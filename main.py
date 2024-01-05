from graphics import Window
from maze import Maze

win = Window(800, 600)
maze = Maze(5, 5, 5, 5, 20, 20, win, 4)
win.wait_for_close()