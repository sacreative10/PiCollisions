import unittest

from pyglet.shapes import Vec2

from elasticCollisionSolver import Object
from utility import collisionDetection


class collisionDetectionTest(unittest.TestCase):
    def test_no_collision(self):
        obj1: Object = Object(1, 0, Vec2(0, 0))
        obj2: Object = Object(1, 0, Vec2(25, 0))
        self.assertFalse(collisionDetection(obj1, obj2))

    def test_collision(self):
        obj1: Object = Object(1, 0, Vec2(0, 0))
        obj2: Object = Object(1, 0, Vec2(20, 0))
        self.assertTrue(collisionDetection(obj1, obj2))

    def test_collision_with_offset(self):
        obj1: Object = Object(1, 0, Vec2(0, 0))
        obj2: Object = Object(1, 0, Vec2(0, 0))
        self.assertTrue(collisionDetection(obj1, obj2))


if __name__ == "__main__":
    unittest.main(verbosity=3)
