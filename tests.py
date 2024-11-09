import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0.0, 0.0, num_rows, num_cols, 10.0, 10.0) # type: ignore
        # print(m1.get_cells())
        self.assertEqual(
            len(m1.get_cells()),
            num_cols,
        )
        self.assertEqual(
            len(m1.get_cells()[0]),
            num_rows,
        )

    def test_maze_create_cells2(self):
        num_cols = 20
        num_rows = 36
        m1 = Maze(0.0, 0.0, num_rows, num_cols, 10.0, 10.0) # type: ignore
        # print(m1.get_cells())
        self.assertEqual(
            len(m1.get_cells()),
            num_cols,
        )
        self.assertEqual(
            len(m1.get_cells()[0]),
            num_rows,
        )
    
    def test_maze_create_cells3(self):
        num_cols = 100
        num_rows = 300
        m1 = Maze(0.0, 0.0, num_rows, num_cols, 10.0, 10.0) # type: ignore
        # print(m1.get_cells())
        self.assertEqual(
            len(m1.get_cells()),
            num_cols,
        )
        self.assertEqual(
            len(m1.get_cells()[0]),
            num_rows,
        )


if __name__ == "__main__":
    unittest.main()