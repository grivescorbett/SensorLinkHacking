import unittest
import widget
from struct import *

class TestBaseConverter(unittest.TestCase):
	def test1(self):
		result = widget.base10ToBase127(128)
		self.assertEqual(result, pack('BBB', 0, 1, 1))

	def test2(self):
		result = widget.base10ToBase127(53)
		self.assertEqual(result, pack('BBB', 0, 0, 53))

	def test3(self):
		result = widget.base10ToBase127(16130)
		self.assertEqual(result, pack('BBB', 1, 0, 1))

class TestAppendSensorNumber(unittest.TestCase):
	def test(self):
		result = widget.appendSensorNumber(pack('BBB', 1, 0, 1), 1)
		self.assertEqual(result, pack('BBBB', 1, 0, 1, 0x81))


if __name__ == '__main__':
    unittest.main()