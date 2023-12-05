from window import PygletOverride
from pyglet.math import Vec2
from elasticCollisionSolver import Object, elastic_collision_solver
from utility import (
    mass_factor,
    collisionDetection,
    draw_object,
    updateObject,
    draw_text,
)
from time import perf_counter

pygletHandle = PygletOverride("Prototype 2", Vec2(800, 600))


digits = 7
timestep = 10 ** (digits - 1)
obj1 = Object(1, 0, Vec2(50, 200), 10 * int(mass_factor(1)))
obj2 = Object(
    100 ** (digits - 1),
    -1 / timestep,
    Vec2(200, 200),
    10 * int(mass_factor(100 ** (digits - 1))),
)

obj1Colour = (255, 255, 0)
obj2Colour = (0, 0, 255)


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


collisionCount = 0


def customDraw():
    global collisionCount
    # check for collisions and update velocities
    start = perf_counter()
    collisionCount += computation()
    end = perf_counter()
    print(f"Time taken: {end - start} seconds")

    # draw the objects
    draw_object(obj1, obj1Colour)
    draw_object(obj2, obj2Colour)
    draw_text(f"Collision: {collisionCount}", 0, 0)


pygletHandle.drawHandler = customDraw
pygletHandle.run()
