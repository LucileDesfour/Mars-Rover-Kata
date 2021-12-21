
from Direction import Direction
from Exceptions import UnknowDirection
import unittest


class DirectionTest(unittest.TestCase):
    def test_should_return_W_when_direction_is_W(self):
        direction = Direction("W")
        self.assertEquals(direction.direction,"W")

    def test_should_return_E_when_direction_is_E(self):
        direction = Direction("E")
        self.assertNotEquals(direction.direction,"W")

    def test_sould_raise_UnknowException_when_direction_is_U(self):
        self.assertRaises(UnknowDirection, Direction, "U")

if __name__ == '__main__':
    unittest.main()
