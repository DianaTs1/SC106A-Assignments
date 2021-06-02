import tkinter

CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels

BRICK_WIDTH	= 30        # The width of each brick in pixels
BRICK_HEIGHT = 12       # The height of each brick in pixels
BRICKS_IN_BASE = 14     # The number of bricks in the base


def draw_brick(canvas, x1, y1, x2, y2):
    canvas.create_rectangle(x1, y1, x2, y2)


# Draw first bottom line of a pyramid
def draw_line(canvas, x, y, width, height, base):
    for i in range(base):
        draw_brick(canvas, x, y, x+width, y-height)
        x += width


def draw_pyramid(canvas, start_point_x, y, width, height, base):
    for i in range(base, 0, -1):
        x = start_point_x
        draw_line(canvas, x, y, width, height, i)
        start_point_x += width / 2
        y -= height


def main():
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    x1 = (CANVAS_WIDTH - BRICKS_IN_BASE * BRICK_WIDTH) / 2
    y = CANVAS_HEIGHT
    draw_pyramid(canvas, x1, y, BRICK_WIDTH, BRICK_HEIGHT, BRICKS_IN_BASE)
    # draw_row(canvas, x1, y1, x2, y2, BRICK_WIDTH, BRICKS_IN_BASE)
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
    # canvas.create_line(0, height, width, height, width=1, fill='blue')
    # Subtracting 1 from height so the blue line is visible
    canvas.create_line(0, height-1, width, height-1, width=1, fill='blue')

    return canvas


if __name__ == '__main__':
    main()


# def draw_brick(canvas, x, y, width, height):
#     canvas.create_rectangle(x, y, width, height)

#
# def draw_row(canvas, x1, y1, x2, y2, width, base):
#     for i in range(base):
#         draw_brick(canvas, x1, y1, x2, y2)
#         x1 += width
#         x2 += width
#
#
# def draw_pyramid(canvas, x1, y1, x2, y2, width, height, base):
#     for i in range(base):
#         draw_row(canvas, x1, y1, x2, y2, width, base)
#         y1 -= height
#         y2 -= height
#         base -= 1
#         x1 += width/2
#         x2 += width/2
#
#
# def make_canvas(width, height):
#     top = tkinter.Tk()
#     top.minsize(width=width + 10, height=height + 10)
#     top.title('pyramid')
#     canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
#     canvas.pack()
#     canvas.xview_scroll(8, 'units')  # This is so (0, 0) works correctly,
#     canvas.yview_scroll(8, 'units')  # otherwise it's clipped off
#
#     # Draw blue boundary line at bottom of canvas
#     # canvas.create_line(0, height, width, height, width=1, fill='blue')
#     # Subtracting 1 from height so the blue line is visible
#     canvas.create_line(0, height-1, width, height-1, width=1, fill='blue')
#
#     return canvas
#
#
# def main():
#     canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
#     x1 = (CANVAS_WIDTH - BRICKS_IN_BASE * BRICK_WIDTH) / 2
#     y1 = CANVAS_HEIGHT - BRICK_HEIGHT
#     x2 = x1 + BRICK_WIDTH
#     y2 = CANVAS_HEIGHT
#     draw_pyramid(canvas, x1, y1, x2, y2, BRICK_WIDTH, BRICK_HEIGHT, BRICKS_IN_BASE)
#     draw_row(canvas, x1, y1, x2, y2, BRICK_WIDTH, BRICKS_IN_BASE)
#     tkinter.mainloop()