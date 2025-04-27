from cell import Cell
from graphics import Window
from maze import Maze
        
def main():
    win = Window(800, 600)
    
    maze = Maze(20, 20, 10, 15, 50, 50, win)
    maze.solve()
    win.wait_for_close()

if __name__ == "__main__":
    main()