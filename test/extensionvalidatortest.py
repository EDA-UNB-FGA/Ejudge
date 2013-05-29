# !/usr/bin/python
# -*- coding: iso-8859-1 -*-
from extensionvalidator import *
import unittest

class ExtensionValidatorTest(unittest.TestCase):

	def setUp(self):
		self.validator = ExtensionValidator()

	def test_c(self):
		self.assertTrue(self.validator.check('main.c'))

	def test_cpp(self):
		self.assertTrue(self.validator.check('main.cpp'))

	def test_java(self):
		self.assertTrue(self.validator.check('main.java'))

	def test_py(self):
		self.assertTrue(self.validator.check('main.py'))

	def test_invalid(self):
		self.assertRaises(ValidatorException, self.validator.check, 'main.bmp')

	def test_noExtension(self):
		self.assertRaises(ValidatorException, self.validator.check, 'main')


if __name__ == '__main__':
	unittest.main()

