import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        some_obj_1 = Runner('Mark')
        for i in range(10):
            some_obj_1.walk()
        self.assertEqual(some_obj_1.distance, 50)

    def test_run(self):
        some_obj_2 = Runner('Tom')
        for i in range(10):
            some_obj_2.run()
        self.assertEqual(some_obj_2.distance, 100)

    def test_challenge(self):
        some_obj_3 = Runner('Nil')
        some_obj_4 = Runner('Nail')
        for i in range(10):
            some_obj_3.run()
            some_obj_4.walk()
        self.assertNotEqual(some_obj_3.distance, some_obj_4.distance)




