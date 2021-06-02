import tkinter

CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels

BRICK_WIDTH	= 30        # The width of each brick in pixels
BRICK_HEIGHT = 12       # The height of each brick in pixels
BRICKS_IN_BASE = 14     # The number of bricks in the base


def draw_brick(canvas, x, y, width, height):
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.create_recangle(x, y, width, height)


def draw_pyramid(canvas):
    draw_brick(canvas, 0, 0, BRICK_WIDTH, BRICK_HEIGHT)


def main():
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.create_rectangle(285, 285, 315, 300)
    # draw_pyramid(canvas)
    tkinter.mainloop()


def make_canvas(width, height):
    top = tkinter.Tk()
    top.minsize(width=width + 10, height=height + 10)
    top.title('pyramid')
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    canvas.xview_scroll(8, 'units')  # This is so (0, 0) works correctly,
    canvas.yview_scroll(8, 'units')  # otherwise it's clipped off

    # Draw blue boundary line at bottom of canvas
    canvas.create_line(0, height-1, width, height-1, width=1, fill='blue')

    return canvas


if __name__ == '__main__':
    main()
