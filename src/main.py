from graphics import Window
from maze import Maze        

        
def main():
    win = Window(800, 600)
    maze = Maze(40, 40, 10, 10, 40, 40, win, 10)
    maze._create_cells()
    maze._break_entrance_and_exit()
    maze._break_walls_r(0, 0)
    maze._reset_cells_visited()
    solved = maze.solve()
    print(solved)
    win.wait_for_close()
    
main()
        