def main():
    print("This program will calculate the are of a circle for you")
    radius = input("Enter the radius of a circle: ")
    radius = float(radius)
    square_radius = radius * radius
    pi = 3.14159265358979
    are = square_radius * pi
    print(f"The area of a circle with the radius of {radius} is {are}")

if __name__ == '__main__':
    main()
