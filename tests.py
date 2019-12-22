import unittest

from rover import Rover


class TestRover(unittest.TestCase):

    def test_rotate_left(self):
        """Testing rover.rotate"""
        rover = Rover(0, 0, 'N')
        rover.rotate('L')
        self.assertEqual(rover.direction, 'W')

    def test_rotate_right(self):
        """Testing rover.rotate"""
        rover = Rover(0, 0, 'N')
        rover.rotate('R')
        self.assertEqual(rover.direction, 'E')

    def test_move_forward(self):
        """Testing rover.move_forward"""
        rover = Rover(0, 0, 'N')
        rover.move_forward()
        self.assertEqual((rover.x, rover.y), (0, 1))


if __name__ == '__main__':
    unittest.main()
