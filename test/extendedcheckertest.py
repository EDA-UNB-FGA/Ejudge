# !/usr/bin/python
# -*- coding: iso-8859-1 -*-
from ccompiler import *
from cppcompiler import *
from extendedchecker import *
import unittest

class ExtendedCheckerTest(unittest.TestCase):

	def setUp(self):
		self.checker = ExtendedChecker()

	def test_valid(self):
		compiler = CCompiler()
		compiler.compile('6_1234.c')
		self.assertTrue(self.checker.check('6'))

	def test_without_needed_files(self):
		self.assertRaises(CheckerException, self.checker.check, '7')

	def test_with_invalid_output(self):
		compiler = CppCompiler()
		compiler.compile('8_1234.cpp')
		self.assertRaises(CheckerException, self.checker.check, '8')


if __name__ == '__main__':
	unittest.main()

