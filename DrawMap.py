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


def draw_circle(r, c):
    speed(0)
    penup()
    right(90)
    forward(r)
    left(90)
    pendown()
    color(c)
    circle(r)
    penup()
    left(90)
    forward(r)
    right(90)


def goto_vertex(vertex, length, size):
    x = vertex[0]
    y = vertex[1]
    n = vertex[2]
    x_coordinate = (x - size + 1 + 0.5 * abs(y)) * (length * math.sqrt(3))
    y_coordinate = length * y * 1.5

    speed(0)
    penup()
    goto(x_coordinate, y_coordinate)
    if n == 0:
        left(90)
        forward(length)
        right(90)
    elif n == 1:
        left(30)
        forward(length)
        right(30)
    elif n == 2:
        right(30)
        forward(length)
        left(30)
    elif n == 3:
        right(90)
        forward(length)
        left(90)
    elif n == 4:
        right(150)
        forward(length)
        left(150)
    elif n == 5:
        left(150)
        forward(length)
        right(150)
    return pos()


def draw_vertex(vertex, length, size):
    goto_vertex(vertex, length, size)
    draw_circle(0.1 * length, "green")


def draw_edge(edge, length, size):
    v1 = edge[0]
    v2 = edge[1]
    pos1 = goto_vertex(v1, length, size)
    pos2 = goto_vertex(v2, length, size)
    penup()
    goto(pos1)
    pendown()
    color("red")
    goto(pos2)
    penup()


def detail_map(game_map, length):
    speed(0)
    vertices = game_map.top_vertices
    edges = game_map.edges
    size = game_map.size
    for sign in vertices:
        draw_vertex(sign, length, size)
    for edge in edges:
        draw_edge(edge, length, size)

