from graphics import Window
from maze import Maze        

        
def main():
    win = Window(800, 600)
    maze = Maze(40, 40, 10, 10, 40, 40, win)
    maze._create_cells()
    
    
    
    
    win.wait_for_close()
    
main()
        