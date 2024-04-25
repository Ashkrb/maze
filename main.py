
from window import Window
from line import Line,Point
from cell import Cell
from maze import Maze

def main():

    num_rows = 6
    num_cols = 9
    margin = 50
    screen_x = 1280
    screen_y = 960
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    maze._break_entrance_and_Exit()
    maze._break_walls_r(0,0)
    maze._reset_cells_visited()
    if maze.solve():
        print("solved")
    win.wait_for_close()

main()