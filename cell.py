from tkinter import Toplevel
from window import Window
from point import Point
from line import Line
from typing_extensions import Self

class Cell():
    def __init__(self, 
                 x1: float, x2: float, y1: float, y2: float, 
                 win: Window=None, has_left_wall: bool = True, has_right_wall: bool = True,  # type: ignore
                 has_top_wall: bool = True, has_bottom_wall: bool = True):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        # Every center point will be offset by what the edge draw boundary is.
        center_offset = 10.0
        self.center = Point(((x1 + x2) / 2) + center_offset, ((y1 + y2) / 2) + center_offset)
        self.__win = win
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall

    
    def draw(self, top_left: Point, bottom_right: Point):
        offset = Point(self.__x1, self.__y1)
        if self.has_left_wall:
            start = top_left + offset
            end = Point(top_left.x, bottom_right.y) + offset
            left = Line(start, end)
            # print(f"Drawing left wall from {start} to {end}")
            self.__win.draw_line(left, "white")
        else:
            start = top_left + offset
            end = Point(top_left.x, bottom_right.y) + offset
            left = Line(start, end)
            self.__win.draw_line(left, "black")
        
        if self.has_right_wall:
            start = Point(bottom_right.x, top_left.y) + offset
            end = bottom_right + offset
            # print(f"Drawing right wall from {start} to {end}")
            left = Line(start, end)
            self.__win.draw_line(left, "white")
        else:
            start = Point(bottom_right.x, top_left.y) + offset
            end = bottom_right + offset
            left = Line(start, end)
            self.__win.draw_line(left, "black")

        if self.has_top_wall:
            start = top_left + offset
            end = Point(bottom_right.x, top_left.y) + offset
            # print(f"Drawing top wall from {start} to {end}")
            left = Line(start, end)
            self.__win.draw_line(left, "white")
        else:
            start = top_left + offset
            end = Point(bottom_right.x, top_left.y) + offset
            left = Line(start, end)
            self.__win.draw_line(left, "black")
        
        if self.has_bottom_wall:
            start = Point(top_left.x, bottom_right.y) + offset
            end = bottom_right + offset
            # print(f"Drawing bottom wall from {start} to {end}")
            left = Line(start, end)
            self.__win.draw_line(left, "white")
        else:
            start = Point(top_left.x, bottom_right.y) + offset
            end = bottom_right + offset
            # print(f"Drawing bottom wall from {start} to {end}")
            left = Line(start, end)
            self.__win.draw_line(left, "black")
        
    def draw_move(self, to_cell: Self, undo=False):
        colour = ""
        if undo:
            colour = "gray"
        else:
            colour = "red"
        
        # print(f"Drawing path from {self.center} to {to_cell.center}")
        # print(f"--- Self: top_left: ({self.__x1}, {self.__y1}) bottom_right: ({self.__x2}, {self.__y2})  center: {self.center}")
        # print(f"--- dest: top_left: ({to_cell.__x1}, {to_cell.__y1}) bottom_right: ({to_cell.__x2}, {to_cell.__y2})  center: {to_cell.center}")
        line = Line(self.center, to_cell.center)
        self.__win.draw_line(line, colour)
