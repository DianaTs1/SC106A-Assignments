from simpleimage import SimpleImage
import random

# ჩემი კოდი შვება შემდეგ რამეს:
# 1-ხატავს 100x100-ზე რრენდომ მწვანე ფერის კვადრატს, ოღონდ ამ კვადრატში
# პიქსელები ჭადრაკისებურადაა განასილებული
# 2 რამხელა ზომასაც მივუთითებთ ფოტოს, მთლიანი ფოტოს ზომას
# (თუ 100-ის ჯერადია) აფერადებს რენდომ წერის ამ მწვანე კვადრატებით.


def get_green_squares(image, green, newx, newy):
    for x in range(100):
        for y in range (100):
            pixel = image.get_pixel(x+newx, y+newy)
            if y % 2 == 1 and x % 2 == 1:
                pixel.red = 0
                pixel.blue = 0
                pixel.green = green


def main():
    img = SimpleImage.blank(1100, 1200)
    number_of_iteration = int(img.width/100 * img.height/100)
    new_location_x = 0
    new_location_y=0
    for i in range(number_of_iteration):
        green_number = random.randint(0, 255)
        get_green_squares(img, green_number, new_location_x, new_location_y)
        new_location_x +=100
        if new_location_x > img.width - 100:
            new_location_x = 0
            new_location_y += 100
    img.show()


if __name__ == '__main__':
    main()
