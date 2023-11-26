import dataclasses


@dataclasses.dataclass
class Object:
    mass: int
    velocity: float


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


# test cases

# test case 1
obj1 = Object(5, 3)
obj2 = Object(5, -3)
print(elastic_collision_solver(obj1, obj2))
