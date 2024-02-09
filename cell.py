from graphics import Line, Point


class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        if self._win is not None:
            self._x1 = x1
            self._x2 = x2
            self._y1 = y1
            self._y2 = y2
            if self.has_left_wall:
                line = Line(Point(x1, y1), Point(x1, y2))
                # print("drawing left wall")
                self._win.draw_line(line)
            else:
                line = Line(Point(x1, y1), Point(x1, y2))
                self._win.draw_line(line, fill_color="white")
            if self.has_top_wall:
                line = Line(Point(x1, y1), Point(x2, y1))
                # print("drawing top wall")
                self._win.draw_line(line)
            else:
                line = Line(Point(x1, y1), Point(x2, y1))
                self._win.draw_line(line, fill_color="white")
            if self.has_right_wall:
                line = Line(Point(x2, y1), Point(x2, y2))
                # print("drawing right wall")
                self._win.draw_line(line)
            else:
                line = Line(Point(x2, y1), Point(x2, y2))
                self._win.draw_line(line, fill_color="white")
            if self.has_bottom_wall:
                line = Line(Point(x1, y2), Point(x2, y2))
                # print("drawing bottom wall")
                self._win.draw_line(line)
            else:
                line = Line(Point(x1, y2), Point(x2, y2))
                self._win.draw_line(line, fill_color="white")

    def draw_move(self, to_cell, undo=False):
        fill_color = "red"
        if undo:
            fill_color = "gray"
        x_mid = (self._x1 + self._x2) / 2
        y_mid = (self._y1 + self._y2) / 2
        to_cell_x_mid = (to_cell._x1 + to_cell._x2) / 2
        to_cell_y_mid = (to_cell._y1 + to_cell._y2) / 2

        # moving left
        if self._x1 > to_cell._x1:
            line = Line(Point(self._x1, y_mid), Point(x_mid, y_mid))
            self._win.draw_line(line, fill_color=fill_color)
            line = Line(Point(to_cell_x_mid, to_cell_y_mid), Point(to_cell._x2, to_cell_y_mid))
            print("drawing now")
            self._win.draw_line(line, fill_color=fill_color)
        # moving right
        elif self._x1 < to_cell._x1:
            print("drawing now")

            line = Line(Point(self._x2, y_mid), Point(x_mid, y_mid))
            self._win.draw_line(line, fill_color=fill_color)
            line = Line(Point(to_cell_x_mid, to_cell_y_mid), Point(to_cell._x1, to_cell_y_mid))
            self._win.draw_line(line, fill_color=fill_color)
        # moving up
        elif self._y1 > to_cell._y1:
            print("drawing now")

            line = Line(Point(x_mid, self._y1), Point(x_mid, y_mid))
            self._win.draw_line(line, fill_color=fill_color)
            line = Line(Point(to_cell_x_mid, to_cell_y_mid), Point(to_cell_x_mid, to_cell._y2))
            self._win.draw_line(line, fill_color=fill_color)

        # moving down
        elif self._y1 < to_cell._y1:
            print("drawing now")

            line = Line(Point(x_mid, self._y2), Point(x_mid, y_mid))
            self._win.draw_line(line, fill_color=fill_color)
            line = Line(Point(to_cell_x_mid, to_cell_y_mid), Point(to_cell_x_mid, to_cell._y1))
            self._win.draw_line(line, fill_color=fill_color)

