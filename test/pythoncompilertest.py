# !/usr/bin/python
# -*- coding: iso-8859-1 -*-
from pythoncompiler import *
import unittest

class PythonCompilerTest(unittest.TestCase):

	def setUp(self):
		self.compiler = PythonCompiler()

	def test_valid(self):
		self.assertTrue(self.compiler.compile('inputs/1_1234.py'))

	def test_file_not_exist(self):
		self.assertRaises(CompilerException, self.compiler.compile, 
			'inputs/2_1234.py')

if __name__ == '__main__':
	unittest.main()

