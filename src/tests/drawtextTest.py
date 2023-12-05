from utility import draw_text
from window import PygletOverride
from pyglet.math import Vec2

pygletHandle = PygletOverride("Prototype 2_1", Vec2(800, 600))


def customDraw():
    # test 1
    # draw_text("xyz", 0, 0)
    # test 2
    draw_text(
        "123",
        int(pygletHandle.windowHandle.width / 2),
        int(pygletHandle.windowHandle.height / 2),
    )


pygletHandle.drawHandler = customDraw
pygletHandle.run()
