"""
File: babygraphics.py
---------------------
Add your comments here
"""

import tkinter
import babynames
import babygraphicsgui as gui


# Provided constants to load and draw the baby data
FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (float): The x coordinate of the vertical line associated
                              with the specified year.
    >>> round(get_x_coordinate(1000, 0), 1)
    20.0
    >>> round(get_x_coordinate(1000, 2), 1)
    180.0
    >>> round(get_x_coordinate(1000, 11), 1)
    900.0
    """
    quantity_of_lines = len(YEARS)
    x_coordinate = GRAPH_MARGIN_SIZE + (width - GRAPH_MARGIN_SIZE * 2) / quantity_of_lines * year_index
    return x_coordinate


def draw_fixed_lines(canvas):
    canvas.delete('all')            # delete all existing lines from the canvas
    width = canvas.winfo_width()    # get the width of the canvas
    height = canvas.winfo_height()  # get the height of the canvas

    # Draw vertical lines
    for i in range(len(YEARS)):
        x_coordinate = get_x_coordinate(width, i)
        canvas.create_line(x_coordinate, 0, x_coordinate, height)
        canvas.create_text(x_coordinate, height - GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)

    # Draw horizontal lines
    canvas.create_rectangle(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, width, height-GRAPH_MARGIN_SIZE)



def draw_names(canvas, name_data, lookup_names):
    """
    Given a dictionary of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (tkinter Canvas): The canvas on which we are drawing.
        name_data (dictionary): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot
    """
    draw_fixed_lines(canvas)
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    count = 0

    for name_index in range(len(lookup_names)):
        years_and_ratings = name_data[lookup_names[name_index]]   # dictionary with the key of year, the value or rating
        color = COLORS[count % 4]
        count += 1

        name = lookup_names[name_index]
        draw_graph_for_each_name(height, years_and_ratings, width, canvas, color, name)


def draw_graph_for_each_name(height, years_and_ratings, width, canvas, color, name):

    for year in range(1, len(YEARS)):
        # Count distance between every single Y coordinate
        distance = (height - 2 * GRAPH_MARGIN_SIZE) / MAX_RANK

        # Get the ranking of the first year and one coming after that
        ranking_of_current_year = years_and_ratings.get(YEARS[year - 1], MAX_RANK)
        ranking_of_following_year = years_and_ratings.get(YEARS[year], MAX_RANK)

        # Get Y and X coordinates
        y1 = distance * ranking_of_current_year + GRAPH_MARGIN_SIZE
        y2 = distance * ranking_of_following_year + GRAPH_MARGIN_SIZE
        x1 = get_x_coordinate(width, year - 1)
        x2 = get_x_coordinate(width, year)

        # Print "*" if the name does not have ranking
        rank_to_print = ranking_of_current_year
        if ranking_of_current_year == MAX_RANK:
            rank_to_print = "*"

        # Print lines, names and ranking on canvas, and also a cute little oval which I just like
        canvas.create_line(x1, y1, x2, y2, fill=color)
        canvas.create_oval(x1 - 2, y1 - 2, x1 + 2, y1 + 2, fill=color, outline=color)
        canvas.create_text(x1, y1, text=(name, rank_to_print), fill=color, anchor=tkinter.SW)


def main():
    import sys
    args = sys.argv[1:]
    global WINDOW_WIDTH
    global WINDOW_HEIGHT
    if len(args) == 2:
        WINDOW_WIDTH = int(args[0])
        WINDOW_HEIGHT = int(args[1])

    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Make window
    top = tkinter.Tk()
    top.wm_title('Baby Names Solution')
    canvas = gui.make_gui(top, WINDOW_WIDTH, WINDOW_HEIGHT, name_data, draw_names, babynames.search_names)

    # draw_fixed once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This needs to be called just once
    top.mainloop()


if __name__ == '__main__':
    main()
