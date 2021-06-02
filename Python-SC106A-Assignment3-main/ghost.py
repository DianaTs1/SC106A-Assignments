import os
import sys
from simpleimage import SimpleImage
import math


def get_pixel_dist(pixel, red, green, blue):
    # Returns the square of the color distance between pixel and mean RGB value
    red_difference = pixel.red - red
    green_difference = pixel.green - green
    blue_difference = pixel.blue - blue
    square_distance = (red_difference ** 2 + green_difference ** 2 + blue_difference ** 2)
    return square_distance


def get_best_pixel(pixel1, pixel2, pixel3):
    average_red = (pixel1.red + pixel2.red + pixel3.red) / 3
    average_green = (pixel1.green + pixel2.green + pixel3.green) / 3
    average_blue = (pixel1.blue + pixel2.blue + pixel3.blue) / 3

    # Calculate distance between average and image1 pixel
    image1_distance = get_pixel_dist(pixel1, average_red, average_green, average_blue)
    image2_distance = get_pixel_dist(pixel2, average_red, average_green, average_blue)
    image3_distance = get_pixel_dist(pixel3, average_red, average_green, average_blue)

    min_distance = min(image1_distance, image2_distance, image3_distance)

    # choosing the best pixel
    if min_distance == image1_distance:
        return pixel1
    elif min_distance == image2_distance:
        return pixel2
    return pixel3


def create_ghost(image1, image2, image3):
    # for each pixel get the best value and assign it to the pixels of new blank image
    new_image = SimpleImage.blank(image1.width, image1.height)
    for x in range(image1.width):
        for y in range(image1.height):
            pixel1 = image1.get_pixel(x, y)
            pixel2 = image2.get_pixel(x, y)
            pixel3 = image3.get_pixel(x, y)
            best_pixel = get_best_pixel(pixel1, pixel2, pixel3)
            new_image.set_pixel(x, y, best_pixel)
    return new_image




######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########


def jpgs_in_dir(directory):
    """
    DO NOT MODIFY
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(directory):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(directory, filename))
    return filenames


def load_images(directory):
    """
    DO NOT MODIFY
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints to terminal the names of the files it loads.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(directory)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # DO NOT MODIFY
    args = sys.argv[1:]

    if len(args) != 1:
        print('Please specify directory of images on command line')
        return

    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    result = create_ghost(images[0], images[1], images[2])
    if result:
        print("Displaying image!")
        result.show()
    else:
        print("No image to display!")

if __name__ == '__main__':
    main()
