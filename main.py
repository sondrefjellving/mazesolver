from graphics import Window
from maze import Maze

win = Window(800, 600)
maze = Maze(5, 5, 10, 15, 40, 40, win)
maze.solve()
win.wait_for_close()