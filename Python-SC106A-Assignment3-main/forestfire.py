from simpleimage import SimpleImage

INTENSITY_THRESHOLD = 1.05


def highlight_fires(filename):
    image = SimpleImage(filename)
    for pixel in image:
        average = (pixel.red + pixel.blue + pixel.green) // 3
        if pixel.red >= average * INTENSITY_THRESHOLD:
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:
            pixel.green = pixel.blue = pixel.red = average
    return image


def main():
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


if __name__ == '__main__':
    main()
