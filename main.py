from cell import Cell
from graphics import Window
        
def main():
    win = Window(800, 600)
    # line1 = Line(Point(20, 30), Point(40, 50))
    # line2 = Line(Point(100, 30), Point(100, 160))
    # line3 = Line(Point(20, 550), Point(780, 550))
    # win.draw_line(line1, "black")
    # win.draw_line(line2, "red")
    # win.draw_line(line3, 'blue')

    # cell = Cell(window=win)
    # cell.draw(x1= 100, y1= 100, x2 = 200, y2=200)

    # cell = Cell(window=win)
    # cell.has_bottom_wall = False
    # cell.has_right_wall = False
    # cell.draw(x1= 300, y1= 100, x2 = 400, y2=200)

    # cell = Cell(window=win)
    # cell.has_top_wall = False
    # cell.draw(x1= 300, y1= 400, x2 = 400, y2=500)

    # cell = Cell(window=win)
    # cell.has_top_wall = False
    # cell.has_left_wall = False
    # cell.draw(x1= 500, y1= 300, x2 = 600, y2=400)

    cell_1 = Cell(window=win)
    cell_2 = Cell(window=win)
    cell_3 = Cell(window=win)

    cell_1.draw(x1= 100, y1= 100, x2 = 200, y2=200)
    cell_2.draw(x1= 300, y1= 400, x2 = 400, y2=500)
    cell_3.draw(x1= 500, y1= 300, x2 = 600, y2=400)

    cell_1.draw_move(cell_2)
    cell_2.draw_move(cell_3, True)


    win.wait_for_close()

if __name__ == "__main__":
    main()