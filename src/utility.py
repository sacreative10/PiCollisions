from pyglet import shapes
from elasticCollisionSolver import Object
from math import log


def mass_factor(mass):
    print(mass)
    return abs(log(mass + 10))


def draw_object(obj: Object, colour: tuple):
    shapes.Rectangle(
        obj.position.x,
        obj.position.y,
        10 * mass_factor(obj.mass),
        10 * mass_factor(obj.mass),
        colour,
    ).draw()
