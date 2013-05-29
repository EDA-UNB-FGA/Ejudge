# !/usr/bin/python
# -*- coding: iso-8859-1 -*-
from namevalidator import *
import unittest

class NameValidatorTest(unittest.TestCase):

	def setUp(self):
		self.validator = NameValidator()

	def test_invalid_number(self):
		self.assertRaises(ValidatorException, self.validator.check, 'a_1234.cpp')

	def test_invalid_name(self):
		self.assertRaises(ValidatorException, self.validator.check, '1_abcd.cpp')

	def test_invalid_number_and_name(self):
		self.assertRaises(ValidatorException, self.validator.check, 'a_abcd.cpp')

	def test_valid(self):
		self.assertTrue(self.validator.check('1_1234.py'))

	def test_missing_extension(self):
		self.assertRaises(ValidatorException, self.validator.check, '1_1234')

	def test_missing_separator(self):
		self.assertRaises(ValidatorException, self.validator.check, '1234.c')

	def test_multiple_separators(self):
		self.assertRaises(ValidatorException, self.validator.check, '1_2_1234.c')

	def test_non_alphanumeric_chars(self):
		self.assertRaises(ValidatorException, self.validator.check, '$_#%.-')


if __name__ == '__main__':
	unittest.main()

