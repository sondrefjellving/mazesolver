from graphics import Window
from maze import Maze

win = Window(800, 600)
maze = Maze(5, 5, 6, 9, 80, 80, win)
maze._Maze__break_entrance_and_exit()
win.wait_for_close()