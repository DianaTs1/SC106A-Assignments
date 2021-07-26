import random
from simpleimage import SimpleImage


def main():
    image = SimpleImage.blank(500, 500)

    for x in range(image.height):
        for y in range(image.width):
            random_number_blue = random.randint(0, 255)
            random_number_green = random.randint(0, 255)
            random_number_red = random.randint(0, 255)
            pixel = image.get_pixel(x, y)
            pixel.green = random_number_green
            pixel.blue = random_number_blue
            pixel.red = random_number_red
    image.show()



if __name__ == '__main__':
    main()
