# !/usr/bin/python
# -*- coding: iso-8859-1 -*-
from dotvalidator import *
import unittest

class DotValidatorTest(unittest.TestCase):

	def setUp(self):
		self.validator = DotValidator()

	def test_withdot(self):
		self.assertTrue(self.validator.check('main.cpp'))

	def test_withoutdot(self):
		self.assertRaises(ValidatorException, self.validator.check, 'main')

if __name__ == '__main__':
	unittest.main()

