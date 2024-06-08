from graphics import Point, Line, Window

class Cell:
    def __init__(self, window: Window):
        self._window = window
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
    
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        
        left_wall = Line(Point(x1, y2), Point(x1, y1))
        right_wall = Line(Point(x2, y1), Point(x2, y2))
        top_wall = Line(Point(x1, y1), Point(x2, y1))
        bot_wall = Line(Point(x1, y2), Point(x2, y2))
        
        if self.has_left_wall:
            self._window.draw_line(left_wall, "black")
        else:
            self._window.draw_line(left_wall, "white")
            
        if self.has_right_wall:
            self._window.draw_line(right_wall, "black")
        else:
            self._window.draw_line(right_wall, "white")
            
        if self.has_top_wall:
            self._window.draw_line(top_wall, "black")
        else:
            self._window.draw_line(top_wall, "white")
            
        if self.has_bottom_wall:
            self._window.draw_line(bot_wall, "black")
        else:
            self._window.draw_line(bot_wall, "white")
            
    
    def draw_move(self, to_cell, undo=False):
        center = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
        to_cell_center = Point((to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2)
        line = Line(center, to_cell_center)
        color = "gray" if undo else "red"
        self._window.draw_line(line, color)