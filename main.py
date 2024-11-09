from maze import Maze
from window import Window
from point import Point
from line import Line
from cell import Cell

def main():
    screen_x = 800.0
    screen_y = 600.0
    margin = 10.0
    num_cols = 20
    num_rows = 20
    win = Window(screen_x, screen_y)

    # top_left = Point(10.0, 10.0)
    # bottom_right = Point(100.0, 100.0)

    # test_cell = Cell(x1=0.0, y1=0.0, x2=90.0, y2=90.0, win=win)
    # test_cell.draw(top_left, bottom_right)

    # test_cell2 = Cell(x1=90.0, y1=0.0, x2=180.0, y2=90.0, win=win)
    # test_cell2.draw(top_left, bottom_right)

    # test_cell3 = Cell(x1=0.0, y1=90.0, x2=90.0, y2=180.0, win=win)
    # test_cell3.draw(top_left, bottom_right)

    # test_cell.draw_move(test_cell2)
    # test_cell.draw_move(test_cell3)

    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    maze = Maze(0.0, 0.0, num_cols, num_rows, cell_size_x, cell_size_y, win)
    maze._create_cells()

    win.wait_for_close()




main()