from utility import draw_object
from window import PygletOverride
from pyglet.math import Vec2
from elasticCollisionSolver import Object
import pyglet

window = PygletOverride("Tests for boxes", Vec2(1920, 1080))


boxes = [
    [Object(1, 0, Vec2(400, 600)), (255, 255, 0)],
    [Object(1, 0, Vec2(400, 600)), (0, 0, 255)],
    [Object(1, 0, Vec2(200, 700)), (0, 0, 255)],
    [Object(100000, 0, Vec2(800, 300)), (0, 0, 255)],
]


counter = 0


def customDraw():
    draw_object(boxes[counter][0], boxes[counter][1])


def customInput(key, modifiers):
    global counter

    if key == pyglet.window.key.RIGHT:
        counter += 1
        if counter >= len(boxes):
            counter = 0


window.drawHandler = customDraw
window.keyboardInputHandler = customInput
window.run()
