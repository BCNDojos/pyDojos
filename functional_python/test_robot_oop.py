import unittest
from robot_oop import Robot


class RobotTests(unittest.TestCase):

    def test_position(self):
        robot = Robot(1, 1, 'North')
        self.assertEqual(robot.position, (1, 1, 'North'))

    def test_turn_right(self):
        robot = Robot(1, 1, 'North')
        robot.move('R')
        self.assertEqual(robot.position, (1, 1, 'East'))
        robot.move('R')
        self.assertEqual(robot.position, (1, 1, 'South'))
        robot.move('R')
        self.assertEqual(robot.position, (1, 1, 'West'))
        robot.move('R')
        self.assertEqual(robot.position, (1, 1, 'North'))

    def test_turn_left(self):
        robot = Robot(1, 1, 'North')
        robot.move('L')
        self.assertEqual(robot.position, (1, 1, 'West'))
        robot.move('L')
        self.assertEqual(robot.position, (1, 1, 'South'))
        robot.move('L')
        self.assertEqual(robot.position, (1, 1, 'East'))
        robot.move('L')
        self.assertEqual(robot.position, (1, 1, 'North'))

    def test_advance(self):
        robot = Robot(1, 1, 'North')
        robot.move('A')
        self.assertEqual(robot.position, (1, 2, 'North'))

    def test_movements(self):
        robot = Robot(7, 3, 'North')
        robot.execute_movements('RAALAL')
        self.assertEqual(robot.position, (9, 4, 'West'))


if __name__ == '__main__':
    unittest.main()
