from graphics import Window, Point, Line, Cell

win = Window(800, 600)
cell = Cell(5, 5, 55, 55, win)
cell2 = Cell(55, 5, 105, 55, win)
cell3 = Cell(105, 5, 600, 55, win)
cell.has_right_wall = False
cell2.has_left_wall = False
cell2.has_bottom_wall = False
cell.draw()
cell2.draw()
cell3.draw()

win.wait_for_close()