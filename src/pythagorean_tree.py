"""Дерево Піфагора.

Фрактал, що будується з відрізка шляхом рекурсивного розгалуження під кутом 45°.
"""

from __future__ import annotations

import argparse
import math
import turtle


def go_to_point(t: turtle.Turtle, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def pythagorean_tree(
    t: turtle.Turtle,
    order: int,
    size: float,
    last_angle: float = 0,
    size_decrease_rate: float = 0.6,
) -> None:
    """Малює фрактал «дерево Піфагора» за допомогою рекурсії.

    Args:
        t: об'єкт turtle для малювання.
        order: рівень (порядок) рекурсії.
        size: довжина поточного відрізка.
        last_angle: кут попереднього рівня. За замовчуванням 0.
        size_decrease_rate: коефіцієнт зменшення довжини. За замовчуванням 0.6.
    """
    if order == 0:
        t.forward(size)
        return

    t.forward(size)
    current_point = t.position()
    # Decrease current size by some factor to avoid collisions
    next_size = size * math.cos(math.radians(45))
    # Split into several lines and draw the next order of the tree
    for angle in [45, -45]:
        t.setheading(last_angle)
        go_to_point(t, current_point[0], current_point[1])
        t.left(angle)
        pythagorean_tree(t, order - 1, next_size, last_angle + angle)


if __name__ == "__main__":
    window = turtle.Screen()
    window.bgcolor("white")

    parser = argparse.ArgumentParser()
    parser.add_argument("--order", type=int, nargs="?", const=3, default=3)
    parser.add_argument("--size", type=float, nargs="?", const=200, default=200)
    parser.add_argument("--initial-angle", type=float, nargs="?", const=90, default=90)
    parser.add_argument("--sdr", type=float, nargs="?", const=0.7, default=0.7)
    args = parser.parse_args()

    initial_angle = args.initial_angle % 360

    initial_position = turtle.Vec2D(-args.size, 0)
    initial_position = initial_position.rotate(initial_angle)

    order = args.order
    if not (0 < order < 8):
        print("Order should be more than 0 and less than 8. Setting to 5.")
        order = 5

    t = turtle.Turtle()
    t.speed(0)
    go_to_point(t, initial_position[0], initial_position[1])
    t.left(args.initial_angle)
    pythagorean_tree(t, order, args.size, initial_angle, args.sdr)
    t.hideturtle()

    window.mainloop()
