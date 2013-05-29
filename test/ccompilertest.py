# !/usr/bin/python
# -*- coding: iso-8859-1 -*-
from ccompiler import *
import unittest

class CCompilerTest(unittest.TestCase):

	def setUp(self):
		self.compiler = CCompiler()

	def test_valid(self):
		self.assertTrue(self.compiler.compile('inputs/1_1234.c'))

	def test_warning(self):
		self.assertRaises(CompilerException, self.compiler.compile, 
			'inputs/2_1234.c')

	def test_error(self):
		self.assertRaises(CompilerException, self.compiler.compile, 
			'inputs/3_1234.c')

	def test_blank(self):
		self.assertRaises(CompilerException, self.compiler.compile, 
			'inputs/4_1234.c')

	def test_missing_includes(self):
		self.assertRaises(CompilerException, self.compiler.compile, 
			'inputs/5_1234.c')

if __name__ == '__main__':
	unittest.main()

