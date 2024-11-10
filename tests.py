import unittest
from maze import Maze
import globals

class Tests(unittest.TestCase):
    # def test_maze_create_cells(self):
    #     num_cols = 12
    #     num_rows = 10
    #     m1 = Maze(0.0, 0.0, num_rows, num_cols, 10.0, 10.0) # type: ignore
    #     # print(m1.get_cells())
    #     self.assertEqual(
    #         len(m1.get_cells()),
    #         num_cols,
    #     )
    #     self.assertEqual(
    #         len(m1.get_cells()[0]),
    #         num_rows,
    #     )

    # def test_maze_create_cells2(self):
    #     num_cols = 20
    #     num_rows = 36
    #     m1 = Maze(0.0, 0.0, num_rows, num_cols, 10.0, 10.0) # type: ignore
    #     # print(m1.get_cells())
    #     self.assertEqual(
    #         len(m1.get_cells()),
    #         num_cols,
    #     )
    #     self.assertEqual(
    #         len(m1.get_cells()[0]),
    #         num_rows,
    #     )
    
    # def test_maze_create_cells3(self):
    #     num_cols = 100
    #     num_rows = 300
    #     m1 = Maze(0.0, 0.0, num_rows, num_cols, 10.0, 10.0) # type: ignore
    #     # print(m1.get_cells())
    #     self.assertEqual(
    #         len(m1.get_cells()),
    #         num_cols,
    #     )
    #     self.assertEqual(
    #         len(m1.get_cells()[0]),
    #         num_rows,
    #     )

    def test_maze_reset_cells_visited(self):
        globals.DEBUG_MODE = True
        num_cols = 20
        num_rows = 20
        m1 = Maze(0.0, 0.0, num_rows, num_cols, 10.0, 10.0, seed=10) # type: ignore

        cells = m1.get_cells()

        for x in range(m1.get_num_cols()):
            for y in range(m1.get_num_rows()):
                self.assertEqual(cells[x][y].visited, False, "A cell was found to be incorrectly flagged as True.")
        
        globals.DEBUG_MODE = False


if __name__ == "__main__":
    unittest.main()