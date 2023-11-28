import unittest

from pyglet.math import Vec2
from utility import updateObject
from elasticCollisionSolver import Object


class TestUpdateObject(unittest.TestCase):
    def test_positive_velocity(self):
        obj = Object(5, 5, Vec2(10, 0))
        updateObject(0.1, obj)
        self.assertAlmostEqual(obj.position.x, 10.5, places=2)

    def test_negative_velocity(self):
        obj = Object(3, -3, Vec2(15, 0))
        updateObject(0.2, obj)
        self.assertAlmostEqual(obj.position.x, 14.4, places=2)

    def test_zero_velocity(self):
        obj = Object(0, 0, Vec2(20, 0))
        updateObject(0.5, obj)
        self.assertAlmostEqual(obj.position.x, 20, places=2)

    def test_large_time_step(self):
        obj = Object(4, 4, Vec2(25, 0))
        updateObject(2.0, obj)
        self.assertAlmostEqual(obj.position.x, 33, places=2)

    def test_zero_velocity_zero_time_step(self):
        obj = Object(0, 0, Vec2(10))
        updateObject(0.0, obj)
        self.assertAlmostEqual(obj.position.x, 10, places=2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
