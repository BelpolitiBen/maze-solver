from tkinter import Tk, BOTH, Canvas

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Line:
    def __init__(self, a: Point, b: Point):
        self.a = a
        self.b = b
    
    def draw(self, canvas: Canvas, fill_color):
        x1, y1 = self.a.x, self.a.y
        x2, y2 = self.b.x, self.b.y
        canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title = "New Window"
        self.canvas = Canvas(width=self.width, height=self.height)
        self.canvas.pack()
        self.window_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.window_running = True
        while self.window_running:
            self.redraw()
            
    def draw_line(self, line: Line, fill_color):
        line.draw(self.canvas, fill_color)
    
    def close(self):
        self.window_running = False