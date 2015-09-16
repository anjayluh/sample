import unittest
import sys
sys.path.append ("C:\Users\compro\Desktop\calculator\calc")

from calculator import Calculator

class Calculator_test(unittest.TestCase):
	def test_add(self):
		calculator = Calculator()
		result = calculator.add(3,2)
		self.assertEqual(5, result)
		
	def test_wrong(self):
		calculator = Calculator()
		result = calculator.add(3,2)
		self.assertEqual(11, result)
	def test_subtract(self):
		calculator = Calculator()
		result = calculator.subtract(3,5)
		self.assertEqual(2, result)
	def test_multiply(self):
		calculator = Calculator()
		result = calculator.multiply(3,2)
		self.assertEqual(6, result)

	def test_divide(self):
		calculator = Calculator()
		result = calculator.divide(2,6)
		self.assertEqual(3, result)

suite = unittest.TestLoader().loadTestsFromTestCase(Calculator_test)
unittest.TextTestRunner(verbosity=2).run(suite)
