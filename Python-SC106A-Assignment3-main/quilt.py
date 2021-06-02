import tkinter

CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 1000

RECTANGLE_WIDTH = 150
RECTANGLE_HEIGHT = 100

BAR_LINES = 16
EYE_LINES = 10
BOWTIE_LINES = 6


def draw_bars(canvas, x, y, width, height, num_lines):
    canvas.create_rectangle(x, y, x+width, y+height, outline='lightblue')
    x1 = x
    for i in range(num_lines):
        # since the lines are moving vertically only x coordinates, which are same, will change
        # according to how many lines we need y coordinates will remain the same
        canvas.create_line(x1, y, x1, y+height, fill='black')
        x1 += width/(num_lines-1)


def draw_eye(canvas, x, y, width, height, num_lines):
    canvas.create_rectangle(x, y, x+width, y+height, outline='lightblue')
    canvas.create_oval(x, y, x+width, y+height, outline='yellow', fill="yellow")
    x2 = x
    for i in range(num_lines):
        # here only the second x coordinate (x2) of all the lines will change,
        # the rest 3 coordinates will remain the same
        canvas.create_line(x+width/2, y+height/2, x2, y+height)
        x2 += width/(num_lines-1)


def draw_bowtie(canvas, x, y, width, height, num_lines):
    canvas.create_rectangle(x, y, x+width, y+height, outline='lightblue')
    y1 = y
    y2 = y + height
    for i in range(num_lines):
        # here x coordinates stay same and y1 and y2 coordinates change in a reverse way
        canvas.create_line(x, y1, x+width, y2)
        y1 += height/(num_lines-1)
        y2 -= height/(num_lines-1)


def draw_quilt(canvas):
    # calculate number of rectangles in one line horizontally and vertically
    n1 = CANVAS_WIDTH//RECTANGLE_WIDTH
    n2 = CANVAS_HEIGHT//RECTANGLE_HEIGHT

    y = 0
    for i in range(n1):
        x = 0  # when the loop is done with one horizontal line, x is 0 again
        for j in range(n2):  # this loop first chooses the right rectangle to draw, then changes x coordinate
            if (i + j) % 3 == 0:
                draw_bars(canvas, x, y, RECTANGLE_WIDTH, RECTANGLE_HEIGHT, BAR_LINES)
            elif (i + j) % 3 == 1:
                draw_eye(canvas, x, y, RECTANGLE_WIDTH, RECTANGLE_HEIGHT, EYE_LINES)
            else:
                draw_bowtie(canvas, x, y, RECTANGLE_WIDTH, RECTANGLE_HEIGHT, BOWTIE_LINES)
            x += RECTANGLE_WIDTH
        y += RECTANGLE_HEIGHT # when the loop is done with one horizontal line, y increases by rectangle height size


def make_canvas(width, height):
    top = tkinter.Tk()
    top.minsize(width=width + 10, height=height + 10)
    top.title('quilt')
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    canvas.xview_scroll(8, 'units')  # add this so (0, 0) works correctly
    canvas.yview_scroll(8, 'units')  # otherwise it's clipped off

    return canvas


def main():
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # draw_eye(canvas, 0, 400, RECTANGLE_WIDTH, RECTANGLE_HEIGHT, NUMBER_OF_LINES)
    draw_quilt(canvas)
    tkinter.mainloop()


if __name__ == '__main__':
    main()
