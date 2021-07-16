from karel.stanfordkarel import *


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def put_one_beeper():
    move()
    turn_left()
    move()
    turn_right()
    put_beeper()


def main():
    put_beeper()
    while front_is_clear():
        put_one_beeper()


if __name__ == "__main__":
    run_karel_program()
