import pyglet
import pyglet.math as pmath


class PygletOverride:
    def __init__(
        self,
        windowName: str = "Pyglet Window",
        windowSize: pmath.Vec2 = pmath.Vec2(500, 500),
        keyboardInputHandler: callable = None,
        drawHandler: callable = None,
    ):
        self.windowName: str = windowName
        self.windowSize: pmath.Vec2 = windowSize
        self.windowHandle: pyglet.window.Window = None
        self.keyboardInputHandler: callable = keyboardInputHandler
        self.drawHandler: callable = drawHandler

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
        if self.keyboardInputHandler is not None:
            self.keyboardInputHandler(key, modifiers)

    def on_draw(self):
        window.clear()
        if self.drawHandler is not None:
            self.drawHandler()

    def run(self):
        pyglet.app.run()


testWindow = PygletOverride()

testWindow.startUp()
testWindow.run()
