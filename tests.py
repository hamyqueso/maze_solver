import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells2(self):
        num_cols = 9
        num_rows = 8
        m1 = Maze(30, 40, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells3(self):
        num_cols = 18
        num_rows = 15
        m1 = Maze(10, 70, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def check_maze_entrance_and_exit(self):
        num_cols = 18
        num_rows = 15
        m1 = Maze(10, 70, num_rows, num_cols, 10, 10)
        self.assertFalse(
            m1._cells[0][0].has_left_wall
        )
        self.assertFalse(
            m1._cells[num_cols-1][num_rows-1].has_right_wall
        )

if __name__ == "__main__":
    unittest.main()