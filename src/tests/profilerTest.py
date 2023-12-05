from elasticCollisionSolver import *
from utility import collisionDetection, updateObject, mass_factor
import cProfile


digits = 7
timestep = 10 ** (digits - 1)
obj1 = Object(1, 0, Vec2(50, 200), 10 * int(mass_factor(1)))
obj2 = Object(
    100 ** (digits - 1),
    -1 / timestep,
    Vec2(700, 200),
    10 * int(mass_factor(100 ** (digits - 1))),
)

obj1Colour = (255, 255, 0)
obj2Colour = (0, 0, 255)


collisionCount = 0


def computation():
    collisionCount = 0
    pos1 = obj1.position.x
    pos2 = obj2.position.x
    vel1 = obj1.velocity
    vel2 = obj2.velocity
    width1 = obj1.width
    width2 = obj2.width
    mass1 = obj1.mass
    mass2 = obj2.mass

    for _ in range(0, timestep):
        # if obj1.position.x + obj1.width >= obj2.position.x:
        #     collisionCount += 1
        #     obj1.velocity, obj2.velocity = elastic_collision_solver(obj1, obj2)
        # elif obj1.position.x <= 0:
        #     collisionCount += 1
        #     obj1.velocity = -obj1.velocity
        #
        # # update positions
        # obj1.position.x += obj1.velocity
        # obj2.position.x += obj2.velocity
        if pos1 + width1 >= pos2:
            collisionCount += 1
            vel1, vel2 = elastic_collision_solver(
                Object(mass1, vel1, Vec2(pos1)), Object(mass2, vel2, Vec2(pos2))
            )
        elif pos1 <= 0:
            collisionCount += 1
            vel1 = -vel1

        # update positions using local variables
        pos1 += vel1
        pos2 += vel2

    #    update the objects
    obj1.position.x = pos1
    obj2.position.x = pos2
    obj1.velocity = vel1
    return collisionCount


if __name__ == "__main__":
    cProfile.run("computation()")
