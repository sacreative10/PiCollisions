import dataclasses
from pyglet.math import Vec2


@dataclasses.dataclass
class Object:
    mass: int
    velocity: float
    position: Vec2


def elastic_collision_solver(obj1: Object, obj2: Object) -> tuple[float, float]:
    """
    This function takes two objects and returns their velocities after an elastic collision.
    """

    v1 = ((obj1.mass - obj2.mass) / (obj1.mass + obj2.mass)) * obj1.velocity + (
        (2 * obj2.mass) / (obj1.mass + obj2.mass)
    ) * obj2.velocity

    v2 = ((obj2.mass - obj1.mass) / (obj1.mass + obj2.mass)) * obj2.velocity + (
        (2 * obj1.mass) / (obj1.mass + obj2.mass)
    ) * obj1.velocity

    return v1, v2
