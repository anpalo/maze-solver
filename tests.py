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

    def test_reset_cells_seen(self):
        maze = Maze(0, 0, 10, 12, 10, 10)
        for col in maze._cells[:5]:
            for cell in col:
                cell.visited = True
        maze._reset_cells_visited()
        for col in maze._cells:
            for cell in col:
                self.assertFalse(cell.visited)




if __name__ == "__main__":
    unittest.main()
