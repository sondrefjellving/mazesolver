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
    
    def test_maze_create_cells3(self):
        num_cols = 3
        num_rows = 2
        m3 = Maze(0, 0, num_rows, num_cols, 30, 30)
        self.assertEqual(len(m3._Maze__cells), num_cols)
        self.assertEqual(len(m3._Maze__cells[0]), num_rows)

    def test_maze_create_entrance_and_exit(self):
        m4 = Maze(0, 0, 10, 15, 10, 10)
        self.assertFalse(m4._Maze__cells[0][0].has_top_wall)
        self.assertFalse(m4._Maze__cells[14][9].has_bottom_wall)

    def test_maze_reset_cells_visted(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for col in m1._Maze__cells:
            for cell in col:
                self.assertEqual(
                    cell.visited,
                    False,
                )


if __name__ == "__main__":
    unittest.main()


