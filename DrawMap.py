from turtle import *
import math


def draw_hex(x, y, size):
    penup()
    goto(x, y)
    right(90)
    forward(size)
    right(120)
    pendown()

    for i in range(6):
        forward(size)
        right(60)

    right(150)
    penup()


def draw_hex_line(x, y, n, size):
    for i in range(n):
        draw_hex(x, y, size)
        x += math.sqrt(3) * size


def draw_map(map_size, size):
    speed(0)
    h_dis = math.sqrt(3) * size
    v_dis = 1.5 * size
    x = -(map_size * 2 - 1) * h_dis * 0.5
    y = 0

    for i in range(map_size):
        if i == 0:
            draw_hex_line(x, y, map_size * 2 - 1, size)
            continue

        x = x + 0.5 * h_dis
        y = y + v_dis
        n = map_size * 2 - 1 - i
        draw_hex_line(x, y, n, size)
        draw_hex_line(x, -y, n, size)
    done()
    print("done")
