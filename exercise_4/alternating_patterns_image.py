from simpleimage import SimpleImage


def main():
    img = SimpleImage.blank(200,200)

    for x in range(img.height):
        for y in range(img.width):
            pixel = img.get_pixel(x,y)
            if x % 2 == 0:
                pixel.blue = 0
                pixel.green = 0
            else:
                pixel.blue = 0
                pixel.green = 0
                pixel.red = 0

    img.show()


if __name__ == '__main__':
    main()
