import time
from cell import Cell
from constants import *
from point import Point
from window import Window

class Maze():
    def __init__(
        self,
        x1: float,
        y1: float,
        num_rows: int,
        num_cols: int,
        cell_size_x: float,
        cell_size_y: float,
        win: Window,
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win

    def _create_cells(self):
        self.__cells = []

        for x in range(self.__num_cols):
            self.__cells.append([])
            for y in range(self.__num_rows):
                c = Cell(x1=(x * self.__cell_size_x) + EDGE_OFFSET, 
                         y1=(y * self.__cell_size_y) + EDGE_OFFSET, 
                         x2=(x * self.__cell_size_x) + self.__cell_size_x,
                         y2=(y * self.__cell_size_y) + self.__cell_size_y,
                         win=self.__win)
                self.__cells[x].append(c)
        
        for x in range(self.__num_cols):
            for y in range(self.__num_rows):
                self._draw_cell(self.__cells[x][y])
    
    def _draw_cell(self, cell: Cell):
        cell.draw(Point(0.0, 0.0), Point(self.__cell_size_x, self.__cell_size_y))
    

    def _animate(self):
        while True:
            self.__win.redraw()
            time.sleep(0.05)