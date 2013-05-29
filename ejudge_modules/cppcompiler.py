# -*- coding: iso-8859-1 -*-
import string
import subprocess
from compiler import *
from compilerexception import *

class CppCompiler(Compiler):
	def __init__(self):
		extension = 'cpp'
		Compiler.__init__(self, extension)

		self.compiler = 'g++'
		self.flags = '-W -Wall -pedantic -ansi'
		self.libs = '-lm'
		self.includes = '-I.'
		self.outputName = '-o prog'

	def compile(self, filename):
		program = self.compiler
		args = [program]
		args.extend(string.split(self.flags))
		args.extend(string.split(self.outputName))
		args.append(filename)
		args.extend(string.split(self.includes))
		args.extend(string.split(self.libs))

		process = subprocess.Popen(args, stdout=subprocess.PIPE, 
			stderr=subprocess.PIPE)
		[response, error] = process.communicate()

		if 'error' in error or 'undefined reference' in error:
			self.message = 'Erro encontrado'
			self.sugestion = 'Consulte o professor sobre a possível solução'
			raise CompilerException(self.printError)

		if 'warning' in error:
			self.message = 'Warning encontrado'
			self.sugestion = 'Consulte o professor sobre a possível solução'
			raise CompilerException(self.printError)

		return True
