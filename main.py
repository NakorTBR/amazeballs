from window import Window
from point import Point
from line import Line

def main():
    win = Window(800, 600)

    p1 = Point(0, 0)
    p2 = Point(800, 600)
    l1 = Line(p1, p2)
    win.draw_line(l1, "pink")
    p3 = Point(0, 600)
    p4 = Point(800, 0)
    l2 = Line(p3, p4)
    win.draw_line(l2, "red")

    win.wait_for_close()




main()