from graphics import Point, Line, Window

class Cell:
    def __init__(self, top_left: Point, bot_right: Point, window: Window):
        self._window = window
        self._x1 = top_left.x
        self._y1 = top_left.y
        self._x2 = bot_right.x
        self._y2 = bot_right.y
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
    
    def draw(self):
        if self.has_left_wall:
            top_left_point = Point(self._x1, self._y2)
            bot_left_point = Point(self._x1, self._y1)
            left_wall = Line(top_left_point, bot_left_point)
            self._window.draw_line(left_wall, "black")
        if self.has_right_wall:
            top_right_point = Point(self._x2, self._y1)
            bot_right_point = Point(self._x2, self._y2)
            right_wall = Line(top_right_point, bot_right_point)
            self._window.draw_line(right_wall, "black")
        if self.has_top_wall:
            top_left_point = Point(self._x1, self._y1)
            top_right_point = Point(self._x2, self._y1)
            top_wall = Line(top_left_point, top_right_point)
            self._window.draw_line(top_wall, "black")
        if self.has_bottom_wall:
            bot_left_point = Point(self._x1, self._y2)
            bot_right_point = Point(self._x2, self._y2)
            bot_wall = Line(bot_left_point, bot_right_point)
            self._window.draw_line(bot_wall, "black")
    
    def draw_move(self, to_cell, undo=False):
        center = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
        to_cell_center = Point((to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2)
        line = Line(center, to_cell_center)
        color = "red" if undo else "gray"
        self._window.draw_line(line, color)