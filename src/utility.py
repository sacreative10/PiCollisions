from pyglet import shapes
from elasticCollisionSolver import Object
from math import log


def mass_factor(mass):
    return abs(log(mass + 10))


def updateObject(dt: float, obj: Object):
    delta_x = obj.velocity * dt
    obj.position.x += delta_x


def draw_object(obj: Object, colour: tuple):
    shapes.Rectangle(
        obj.position.x,
        obj.position.y,
        10 * mass_factor(obj.mass),
        10 * mass_factor(obj.mass),
        colour,
    ).draw()


def collisionDetection(obj1: Object, obj2: Object) -> bool:
    if obj1.position.x > obj2.position.x:
        raise ValueError("obj1 must be to the left of obj2")
    W1 = 10 * mass_factor(obj1.mass)

    if (obj2.position.x <= obj1.position.x + W1) or (
        obj2.position.x <= obj1.position.x + W1
    ):
        return True

    return False
