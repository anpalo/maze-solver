from cell import Cell
import time
import random
import logging

class Maze:
    def __init__(self,
                 x1,
                 y1,
                 num_rows,
                 num_cols,
                 cell_size_x,
                 cell_size_y,
                 win=None,
                 seed = None):
        self.x1 = x1
        self.y1 = y1
        self._cells = []
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        if seed is not None:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self.visited = False
        self._break_walls_r(0, 0)
        self._reset_cells_visited()


    def _create_cells(self):
        for i in range(self.num_cols):
            col = []
            for j in range(self.num_rows):
                col.append(Cell(self._win))
            self._cells.append(col)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        x1 = self.x1 + (i * self.cell_size_x)
        y1 = self.y1 + (j * self.cell_size_y)
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is not None:
            self._win.redraw()
            time.sleep(0.05)

    def _break_entrance_and_exit(self):
        entrance = self._cells[0][0]
        exit = self._cells[self.num_cols - 1][self.num_rows-1]
        entrance.has_top_wall = False
        self._draw_cell(0, 0)
        exit.has_right_wall = False
        self._draw_cell(self.num_cols-1, self.num_rows-1)

    def _break_walls_r(self, i, j):

        # mark current cell as visited
        current_cell = self._cells[i][j]
        current_cell.visited = True
        while True:
            possible_directions = []
            # moving left
            if i > 0:
                left = self._cells[i - 1][j]
                if not left.visited:
                    possible_directions.append("left")
            # moving right
            if i < (self.num_cols -1):
                right = self._cells[i + 1][j]
                if not right.visited:
                    possible_directions.append("right")
            # moving up
            if j > 0:
                up = self._cells[i][j - 1]
                if not up.visited:
                    possible_directions.append("up")
            # moving down
            if j < (self.num_rows - 1):
                down = self._cells[i][j + 1]
                if not down.visited:
                    possible_directions.append("down")

            if len(possible_directions) == 0:
                self._draw_cell(i,j)
                return

            random_direction = random.choice(possible_directions)

            if random_direction == "left":
                current_cell.has_left_wall = False
                self._draw_cell(i, j)
                left.has_right_wall = False
                self._draw_cell(i - 1, j)
                self._break_walls_r(i - 1, j)
            elif random_direction == "right":
                current_cell.has_right_wall = False
                self._draw_cell(i, j)
                right.has_left_wall = False
                self._draw_cell(i + 1, j)
                self._break_walls_r(i + 1, j)
            elif random_direction == "up":
                current_cell.has_top_wall = False
                self._draw_cell(i, j)
                up.has_bottom_wall = False
                self._draw_cell(i, j - 1)
                self._break_walls_r(i, j - 1)
            elif random_direction == "down":
                current_cell.has_bottom_wall = False
                self._draw_cell(i, j)
                down.has_top_wall = False
                self._draw_cell(i, j + 1)
                self._break_walls_r(i, j + 1)

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        logging.debug(f'Entered _solve_r with i={i} and j={j}')
        current_cell = self._cells[i][j]
        self._animate()
        current_cell.visited = True
        if current_cell == self._cells[self.num_cols -1][self.num_rows - 1]:  # last cell
            return True
        # check left
        if i > 0 and not current_cell.has_left_wall:
            left = self._cells[i - 1][j]
            print(f"Left cell visited: {left.visited}")
            if not left.visited:
                current_cell.draw_move(left)
                solve_next = self._solve_r(i - 1, j)
                if solve_next:
                    return True
                else:
                    current_cell.draw_move(left, undo=True)

        # check right
        if i < (self.num_cols - 1) and not current_cell.has_right_wall:
            right = self._cells[i + 1][j]
            current_cell.draw_move(right)  # Move this line outside of `if not...` check
            print(f"Right cell visited: {right.visited}")
            if not right.visited:
                current_cell.draw_move(right)
                solve_next = self._solve_r(i+1, j)
                if solve_next:
                    return True
                else:
                    current_cell.draw_move(right, undo=True)
        # check up
        if j > 0 and not current_cell.has_top_wall:
            up = self._cells[i][j - 1]
            print(f"Up cell visited: {up.visited}")

            if not up.visited:
                current_cell.draw_move(up)
                solve_next = self._solve_r(i, j - 1)
                if solve_next:
                    return True
                else:
                    current_cell.draw_move(up, undo=True)

        # check down
        if j < (self.num_rows - 1) and not current_cell.has_bottom_wall:
            down = self._cells[i][j + 1]
            print(f"Down cell visited: {down.visited}")

            if not down.visited:
                current_cell.draw_move(down)
                solve_next = self._solve_r(i, j + 1)
                if solve_next:
                    return True
                else:
                    current_cell.draw_move(down, undo=True)

        return False






