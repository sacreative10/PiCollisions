import pyglet
import pyglet.math as pmath
from typing import Callable


class PygletOverride:
    def __init__(
        self,
        windowName: str = "Pyglet Window",
        windowSize: pmath.Vec2 = pmath.Vec2(800, 600),
        keyboardInputHandler: Callable = None,
        drawHandler: Callable = None,
    ):
        self._windowName: str = windowName
        self._windowSize: pmath.Vec2 = windowSize
        self._windowHandle: pyglet.window.Window = None
        self._keyboardInputHandler: Callable = keyboardInputHandler
        self._drawHandler: Callable = drawHandler

    @property
    def windowName(self) -> str:
        return self._windowName

    @windowName.setter
    def windowName(self, value: str):
        self._windowName = value

    @property
    def windowSize(self) -> pmath.Vec2:
        return self._windowSize

    @windowSize.setter
    def windowSize(self, value: pmath.Vec2):
        self._windowSize = value

    @property
    def windowHandle(self) -> pyglet.window.Window:
        return self._windowHandle

    @windowHandle.setter
    def windowHandle(self, value: pyglet.window.Window):
        self._windowHandle = value

    @property
    def keyboardInputHandler(self) -> Callable:
        return self._keyboardInputHandler

    @keyboardInputHandler.setter
    def keyboardInputHandler(self, value: Callable):
        self._keyboardInputHandler = value

    @property
    def drawHandler(self) -> Callable:
        return self._drawHandler

    @drawHandler.setter
    def drawHandler(self, value: Callable):
        self._drawHandler = value

    def createWindow(self) -> bool:
        self.windowHandle = pyglet.window.Window(
            width=self.windowSize.x,
            height=self.windowSize.y,
            caption=self.windowName,
        )
        return True if self.windowHandle is not None else False

    def startUp(self):
        self.createWindow()

    def handleKeyboard(self, key, modifiers):
        if key == pyglet.window.key.ESCAPE:
            self.windowHandle.close()
        if self._keyboardInputHandler is not None:
            self._keyboardInputHandler(key, modifiers)

    def on_draw(self):
        self.windowHandle.clear()
        if self._drawHandler is not None:
            self._drawHandler()

    def run(self, frameTime: float = 1 / 60):
        self.startUp()

        @self.windowHandle.event
        def on_draw():
            self.on_draw()

        @self.windowHandle.event
        def on_key_press(key, modifiers):
            self.handleKeyboard(key, modifiers)

        pyglet.app.run(frameTime)
