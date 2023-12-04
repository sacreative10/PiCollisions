from window import PygletOverride
from pyglet.math import Vec2
from elasticCollisionSolver import Object, elastic_collision_solver
from utility import collisionDetection, draw_object, updateObject

pygletHandle = PygletOverride("Prototype 2", Vec2(800, 600))


digits = 5
timestep = 10 ** (digits - 1)
obj1 = Object(1, 0, Vec2(50, 200))
obj2 = Object(100 ** (digits - 1), -1 / timestep, Vec2(700, 200))

obj1Colour = (255, 255, 0)
obj2Colour = (0, 0, 255)


collisionCount = 0


def customDraw():
    global collisionCount
    # check for collisions and update velocities
    for i in range(0, timestep):
        if collisionDetection(obj1, obj2):
            collisionCount += 1
            obj1.velocity, obj2.velocity = elastic_collision_solver(obj1, obj2)

        if obj1.position.x <= 0:
            obj1.velocity *= -1
            collisionCount += 1

        # update positions
        updateObject(1, obj1)
        updateObject(1, obj2)

    # draw the objects
    draw_object(obj1, obj1Colour)
    draw_object(obj2, obj2Colour)
    print(collisionCount)


pygletHandle.drawHandler = customDraw
pygletHandle.run()
