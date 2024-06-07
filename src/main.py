from graphics import Window, Point
from cell import Cell
        

        
def main():
    win = Window(800, 600)
    p1 = Point(20, 40)
    p2 = Point(60, 80)

    cell = Cell(p1, p2, win)
    cell.has_right_wall = False
    cell.draw()
    
    p1 = Point(740, 40)
    p2 = Point(780, 80)

    new_cell = Cell(p1, p2, win)
    new_cell.has_left_wall = False
    new_cell.draw()
    
    cell.draw_move(new_cell, True)
    
    
    
    win.wait_for_close()
    
main()
        