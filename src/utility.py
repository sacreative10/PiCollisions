from pyglet import font, shapes, text
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
        obj.width,
        obj.width,
        colour,
    ).draw()


def collisionDetection(obj1: Object, obj2: Object) -> bool:
    if obj1.position.x > obj2.position.x:
        raise ValueError("obj1 must be to the left of obj2")

    return obj1.position.x + obj1.width >= obj2.position.x


def draw_text(prompt: str, textX: int, textY=int):
    label_ = text.Label(prompt, font_name="Arial", font_size=16, x=textX, y=textY)

    label_.draw()

    del label_
