import random
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
        win: Window = None, # type: ignore
        seed = None
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win

        if seed:
            random.seed(seed)

        self.__cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def get_cells(self):
        return self.__cells

    def get_num_cols(self):
        return self.__num_cols

    def get_num_rows(self):
        return self.__num_rows

    def _create_cells(self):
        for x in range(self.__num_cols):
            self.__cells.append([])
            for y in range(self.__num_rows):
                c = Cell(x1=(x * self.__cell_size_x) + EDGE_OFFSET, 
                         y1=(y * self.__cell_size_y) + EDGE_OFFSET, 
                         x2=(x * self.__cell_size_x) + self.__cell_size_x,
                         y2=(y * self.__cell_size_y) + self.__cell_size_y,
                         win=self.__win)
                self.__cells[x].append(c)
        
        if self.__win:
            for x in range(self.__num_cols):
                for y in range(self.__num_rows):
                    self._draw_cell(self.__cells[x][y])
    
    def _draw_cell(self, cell: Cell):
        cell.draw(Point(0.0, 0.0), Point(self.__cell_size_x, self.__cell_size_y))
    

    def _animate(self):
        self.__win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        start: Cell = self.__cells[0][0]
        end: Cell = self.__cells[-1][-1]
        start.has_left_wall = False
        self._draw_cell(start)
        end.has_right_wall = False
        self._draw_cell(end)

    def _break_walls_r(self, i, j):
        current = self.__cells[i][j]
        current.visited = True

        while True:
            indices = []

            # Find cells to affect
            # left
            if i > 0 and not self.__cells[i - 1][j].visited:
                indices.append((i - 1, j))
            # right
            if i < self.__num_cols - 1 and not self.__cells[i + 1][j].visited:
                indices.append((i + 1, j))
            # up
            if j > 0 and not self.__cells[i][j - 1].visited:
                indices.append((i, j - 1))
            # down
            if j < self.__num_rows - 1 and not self.__cells[i][j + 1].visited:
                indices.append((i, j + 1))

            if len(indices) == 0:
                self._draw_cell(self.__cells[i][j])
                return

            # Randomly choose the next direction
            direction_index = random.randrange(len(indices))            
            next_index = indices[direction_index]
            # print(next_index)

            # Destroy walls between this cell and the next cell
            # right
            if next_index[0] == i + 1:
                self.__cells[i][j].has_right_wall = False
                self.__cells[i + 1][j].has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self.__cells[i][j].has_left_wall = False
                self.__cells[i - 1][j].has_right_wall = False
            # down
            if next_index[1] == j + 1:
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[i][j + 1].has_top_wall = False
            # up
            if next_index[1] == j - 1:
                self.__cells[i][j].has_top_wall = False
                self.__cells[i][j - 1].has_bottom_wall = False

            # Go visit the next cell
            self._break_walls_r(next_index[0], next_index[1])


    def _reset_cells_visited(self):
        for x in range(self.__num_cols):
            for y in range(self.__num_rows):
                self.__cells[x][y].visited = False

    def solve(self) -> bool:
        return self._solve_r(0, 0)
    
    def _solve_r(self, i: int, j: int) -> bool:
        self._animate()
        self.__cells[i][j].visited = True

        if i == self.__num_cols - 1 and j == self.__num_rows - 1:
            return True
        
        # Try left
        if (i > 0 and not self.__cells[i][j].has_left_wall
            and not self.__cells[i - 1][j].visited):
            self.__cells[i][j].draw_move(self.__cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i - 1][j], True)

        # Try right
        if (
            i < self.__num_cols - 1
            and not self.__cells[i][j].has_right_wall
            and not self.__cells[i + 1][j].visited
        ):
            self.__cells[i][j].draw_move(self.__cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i + 1][j], True)

        # Try up
        if (
            j > 0
            and not self.__cells[i][j].has_top_wall
            and not self.__cells[i][j - 1].visited
        ):
            self.__cells[i][j].draw_move(self.__cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i][j - 1], True)

        # Try down
        if (
            j < self.__num_rows - 1
            and not self.__cells[i][j].has_bottom_wall
            and not self.__cells[i][j + 1].visited
        ):
            self.__cells[i][j].draw_move(self.__cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i][j + 1], True)

        # This path has failed.
        return False

