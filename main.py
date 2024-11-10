import time
from maze import Maze
from window import Window

def main():
    screen_x = 800.0
    screen_y = 600.0
    margin = 10.0
    num_cols = 20
    num_rows = 20
    win = Window(screen_x, screen_y)

    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    print(f"Creating maze with size: {num_cols}x{num_rows}")
    maze = Maze(0.0, 0.0, num_cols, num_rows, cell_size_x, cell_size_y, win)

    print("Maze created.")
    timer_start = time.time()
    can_solve = maze.solve()
    timer_end = time.time()
    time_to_solve = timer_end - timer_start
    if not can_solve:
        print("Maze not able to be solved.")
    else:
        print(f"Maze was succesfully solved in {time_to_solve:.2f} seconds!")

    win.wait_for_close()




main()