from graphics import Window, Point, Line

win = Window(800, 600)
start_point = Point(50, 50)
end_point = Point(200, 200)
line = Line(start_point, end_point)

win.draw_line(line, "red")
win.wait_for_close()