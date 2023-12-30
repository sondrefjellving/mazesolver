import unittest
from maze import Maze
from graphics import Window

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._Maze__cells), num_cols)
        self.assertEqual(len(m1._Maze__cells[0]), num_rows)
        self.assertIsNone(m1._Maze__animate())
    
    def test_maze_create_cells2(self):
        num_cols = 5
        num_rows = 10
        m2 = Maze(0, 0, num_rows, num_cols, 20, 20)
        self.assertEqual(len(m2._Maze__cells), num_cols)
        self.assertEqual(len(m2._Maze__cells[0]), num_rows)
        self.assertIsNone(m2._Maze__animate())
    
    def test_maze_create_cells_valid(self):
        num_cols = 3
        num_rows = 2
        m3 = Maze(0, 0, num_rows, num_cols, 30, 30)
        self.assertEqual(len(m3._Maze__cells), num_cols)
        self.assertEqual(len(m3._Maze__cells[0]), num_rows)


if __name__ == "__main__":
    unittest.main()


