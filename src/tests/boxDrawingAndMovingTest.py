from utility import draw_object, updateObject
from window import PygletOverride
from pyglet.math import Vec2
from elasticCollisionSolver import Object
import pyglet

window = PygletOverride("Tests for boxes", Vec2(800, 600))


boxes = [
    [Object(20, 100, Vec2(100, 500)), (255, 255, 0)],
    [Object(10, 20, Vec2(200, 400)), (0, 0, 255)],
]


counter = 0


def customDraw():
    # update positions
    for box in boxes:
        pyglet.clock.schedule_once(updateObject, 1 / 144, box[0])
    # draw the boxes
    for box in boxes:
        draw_object(box[0], box[1])


window.drawHandler = customDraw
window.run()
