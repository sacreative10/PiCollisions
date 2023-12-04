from elasticCollisionSolver import Object, elastic_collision_solver
from utility import collisionDetection, draw_object, updateObject
from window import PygletOverride
from pyglet.math import Vec2

pygletHandle = PygletOverride("Prototype 2_1", Vec2(800, 600))


obj1 = Object(1, 0, Vec2(50, 200))
obj2 = Object(100**3, -50, Vec2(300, 200))


collisionCount = 0
timestep = 1 / 144


def customDraw():
    global collisionCount

    if collisionDetection(obj1, obj2):
        obj1.velocity, obj2.velocity = elastic_collision_solver(obj1, obj2)
        collisionCount += 1

    if obj1.position.x < 0:
        obj1.velocity *= -1
        collisionCount += 1

    updateObject(timestep, obj1)
    updateObject(timestep, obj2)

    draw_object(obj1, (255, 0, 0))
    draw_object(obj2, (0, 0, 255))

    print("Collision Count: " + str(collisionCount))


pygletHandle.drawHandler = customDraw
pygletHandle.run()
