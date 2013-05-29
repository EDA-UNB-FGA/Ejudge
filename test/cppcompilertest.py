# !/usr/bin/python
# -*- coding: iso-8859-1 -*-
from cppcompiler import *
import unittest

class CppCompilerTest(unittest.TestCase):

	def setUp(self):
		self.compiler = CppCompiler()

	def test_valid(self):
		self.assertTrue(self.compiler.compile('inputs/1_1234.cpp'))

	def test_warning(self):
		self.assertRaises(CompilerException, self.compiler.compile, 
			'inputs/2_1234.cpp')

	def test_error(self):
		self.assertRaises(CompilerException, self.compiler.compile, 
			'inputs/3_1234.cpp')

	def test_blank(self):
		self.assertRaises(CompilerException, self.compiler.compile, 
			'inputs/4_1234.cpp')

	def test_missing_includes(self):
		self.assertRaises(CompilerException, self.compiler.compile, 
			'inputs/5_1234.cpp')

if __name__ == '__main__':
	unittest.main()

