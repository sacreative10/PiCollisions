import unittest
import os, sys

from elasticCollisionSolver import *


def customOutput(obj1, obj2, expect, real):
    print(
        f"\n Input: Object 1({obj1.mass}, {obj1.velocity}), Object 2({obj2.mass}, {obj2.velocity})"
    )
    print("Expected: " + str(expect))
    print("Real: " + str(real))


class TestElasticCollisionSolver(unittest.TestCase):
    def test_collision_with_equal_mass(self):
        obj1 = Object(mass=1, velocity=2)
        obj2 = Object(mass=1, velocity=-3)
        result = elastic_collision_solver(obj1, obj2)
        self.assertAlmostEqual(result[0], -3, places=2)
        self.assertAlmostEqual(result[1], 2, places=2)
        customOutput(obj1, obj2, [-3, 2], result)

    def test_collision_with_different_mass(self):
        obj1 = Object(mass=2, velocity=4)
        obj2 = Object(mass=1, velocity=-3)
        result = elastic_collision_solver(obj1, obj2)
        self.assertAlmostEqual(result[0], -0.6667, places=2)
        self.assertAlmostEqual(result[1], 6.333, places=2)
        customOutput(obj1, obj2, [-0.6667, 6.333], result)

    def test_collision_with_one_stationary_object(self):
        obj1 = Object(mass=2, velocity=0)
        obj2 = Object(mass=1, velocity=-3)
        result = elastic_collision_solver(obj1, obj2)
        self.assertAlmostEqual(result[0], -2, places=2)
        self.assertAlmostEqual(result[1], 1, places=2)
        customOutput(obj1, obj2, [-2, 1], result)

    def test_collision_with_opposite_directions(self):
        obj1 = Object(mass=1, velocity=2)
        obj2 = Object(mass=1, velocity=3)
        result = elastic_collision_solver(obj1, obj2)
        self.assertAlmostEqual(result[0], 3, places=2)
        self.assertAlmostEqual(result[1], 2, places=2)
        customOutput(obj1, obj2, [3, 2], result)

    def test_collision_with_same_directions(self):
        obj1 = Object(mass=1, velocity=2)
        obj2 = Object(mass=1, velocity=2)
        result = elastic_collision_solver(obj1, obj2)
        self.assertAlmostEqual(result[0], 2, places=2)
        self.assertAlmostEqual(result[1], 2, places=2)
        customOutput(obj1, obj2, [2, 2], result)

    def test_collision_with_large_mass_difference(self):
        obj1 = Object(mass=100, velocity=5)
        obj2 = Object(mass=1, velocity=-3)
        result = elastic_collision_solver(obj1, obj2)
        self.assertAlmostEqual(result[0], 4.842, places=2)
        self.assertAlmostEqual(result[1], 12.842, places=2)
        customOutput(obj1, obj2, [4.842, 12.842], result)

    def test_collision_with_zero_velocity(self):
        obj1 = Object(mass=2, velocity=0)
        obj2 = Object(mass=1, velocity=0)
        result = elastic_collision_solver(obj1, obj2)
        self.assertAlmostEqual(result[0], 0, places=2)
        self.assertAlmostEqual(result[1], 0, places=2)
        customOutput(obj1, obj2, [0, 0], result)


if __name__ == "__main__":
    # verbosity=2 shows detail test result
    unittest.main(verbosity=2)
